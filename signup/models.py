from django.db import models

class Signup(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pw = models.CharField(('password'), max_length=8, help_text=("Please enter maximun 8 characters"))
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
    	return self.name





