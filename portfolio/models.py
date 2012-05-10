import datetime
from hashlib import sha1

from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.auth.models import User


__all__ = ['Project', 'Tag', 'Video', 'Image', 'Category']

class UserContent(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    public_id = models.CharField(max_length=11)

    class Meta:
        abstract = True


class Project(UserContent):
    created_by = models.ForeignKey(User, unique=True, related_name="projects", null=True, blank=True)
    title = models.CharField(max_length=100)
    blurb = models.CharField(max_length=300, blank=True)
    thumbnail = models.ForeignKey('Image', unique=True, related_name='thumbnail', blank=True, null=True)
    content = models.TextField(blank=True)
    tag = models.ManyToManyField('Tag', related_name="tags", blank=True, null=True)
    video = models.ManyToManyField('Video', related_name="videos", blank=True, null=True)
    image = models.ManyToManyField('Image', related_name="images", blank=True, null=True)
    category = models.ForeignKey('Category', unique=True, related_name="category", blank=True, null=True)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.public_id is None:
            self.public_id = sha1(settings.SECRET_KEY + self.title +
                                  datetime.datetime.utcnow()).hexdigest()[:11]
        super(Project, self).save(force_insert, force_update, using)


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.tag


class Video(UserContent):
    owned_by = models.ForeignKey(User, unique=True, related_name="videos")
    video = models.URLField(max_length=1000)
    resolution = models.CommaSeparatedIntegerField(max_length=100)

    def __unicode__(self):
        return self.video


class Image(UserContent):
    owned_by = models.ForeignKey(User, unique=True, related_name="images")
    image = models.FileField(upload_to='images/')
    resolution = models.CommaSeparatedIntegerField(max_length=100)

    def __unicode__(self):
        return self.image


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.category

