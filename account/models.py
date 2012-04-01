from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User as DjangoUser

class User(DjangoUser):
    username = models.CharField(_('username'), max_length=200, unique=True,
        help_text=_('Required. Letters, numbers and '
                    '@/./+/-/_ characters'), validators=[EmailValidator, ])
    email = models.EmailField(_('e-mail address'))

    @property
    def name(self):
        return u"%s %s" % self.first_name, self.last_name
