from django.db import models

# Create your models here.


class ImageToText(models.Model):
	image = models.ImageField(upload_to='images/')
	text = models.CharField(max_length =255,blank=True, null=True)

	class Meta:
		verbose_name = 'imagetotext'
		verbose_name_plural = 'imagetotexts'

	# def __str__(self):