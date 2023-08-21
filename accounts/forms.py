# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:21:54 2023

@author: lecie
"""

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        
        model=CustomUser
        fields=('username','email','password1','password2')