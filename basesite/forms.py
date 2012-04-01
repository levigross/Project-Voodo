# -*- coding: UTF-8 -*-
from django import forms
from django.forms.widgets import Textarea

class ContactUs(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=Textarea)
