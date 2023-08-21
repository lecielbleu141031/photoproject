# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 12:07:11 2023

@author: lecie
"""
from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model=PhotoPost
        fields=['category','title','comment','image1','image2']
