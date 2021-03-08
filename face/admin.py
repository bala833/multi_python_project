# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ImageToText


@admin.register(ImageToText)
class ImageToTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'text')
