# -*- coding: UTF-8 -*-
from django import forms

from portfolio.models import Project


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'is_public', 'blurb']
