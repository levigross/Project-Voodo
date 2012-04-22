from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User as DjangoUser

class User(DjangoUser):
    username = models.CharField(_('username'), max_length=200, unique=True,
        help_text=_('Required. Email address'), validators=[EmailValidator, ])
    email = models.EmailField(_('e-mail address'), required=True)

    @property
    def name(self):
        return u"%s %s" % self.first_name, self.last_name
