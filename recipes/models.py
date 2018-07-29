from django.db import models
from django.utils.text import slugify
from django.template.defaultfilters import pluralize

from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Recipe(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(
        unique=True
    )
    ingredients = HTMLField('Ingredients')
    instructions = HTMLField('Instructions')
    spiel = HTMLField('Spiel', blank=True)
    time_in_mins = models.PositiveSmallIntegerField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/recipes/{slug}'.format(slug=self.slug)

    @property
    def preptime(self):
        """Returns hour/minutes, or just hour, or just minutes"""
        if self.time_in_mins < 60:
            return '{} minute{}'.format(
                self.time_in_mins,
                pluralize(self.time_in_mins)
            )
        else:
            hours, minutes = divmod(self.time_in_mins, 60)
            if minutes == 0:
                return '{} hour{}'.format(hours, pluralize(hours))
            else:
                return '{} hour{}, {} minute{}'.format(
                    hours,
                    pluralize(hours),
                    minutes,
                    pluralize(minutes)
                )

    @property
    def searchterms(self):
        """Returns a list of search keywords"""
        tags = [x.name.casefold() for x in self.tags.all()]
        tags.append(self.title.casefold())
        return ' '.join(tags)

    # https://fazle.me/auto-generating-unique-slug-in-django/
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Recipe.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('title',)
