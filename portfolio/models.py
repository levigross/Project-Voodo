from django.db import models

__all__ = ['Project', 'Tag', 'Video', 'Image', 'Category']

class UserContent(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    public_id = models.CharField(max_length=40, required=True)

    class Meta:
        abstract = True

class Project(UserContent):
    created_by = models.ForeignKey('account.User', unique=True, related_name="projects")
    title = models.CharField(max_length=100)
    blurb = models.CharField(max_length=300, blank=True)
    thumbnail = models.ForeignKey('Image', unique=True, related_name='thumbnail', blank=True, null=True)
    content = models.TextField(blank=True)
    tag = models.ManyToManyField('Tag', related_name="tags", blank=True, null=True)
    video = models.ManyToManyField('Video', related_name="videos", blank=True, null=True)
    image = models.ManyToManyField('Image', related_name="images", blank=True, null=True)
    category = models.ForeignKey('Category', unique=True, related_name="category", blank=True, null=True)

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.tag	

class Video(UserContent):
    owned_by = models.ForeignKey('account.User', unique=True, related_name="videos")
    video = models.URLField(max_length=1000)
    resolution = models.CommaSeparatedIntegerField()

    def __unicode__(self):
        return self.video

class Image(UserContent):
    owned_by = models.ForeignKey('account.User', unique=True, related_name="images")
    image = models.FileField(upload_to='images/')
    resolution = models.CommaSeparatedIntegerField()

    def __unicode__(self):
        return self.image

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.category

