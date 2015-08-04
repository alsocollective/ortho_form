from django.db import models
from django.conf import settings
import os
from django.template.defaultfilters import slugify

class Application(models.Model):
	def location(self,title):
		slug = slugify(self.fullName)
		directory = "%s/%s"%(settings.MEDIA_ROOT,slug)
		
		print directory

		if not os.path.exists(directory):
			os.makedirs(directory)

		title = title.rsplit(".",1)
		return "%s/%s.%s"%(slug,slugify(title[0]),title[1])

	uploaded = models.DateTimeField(auto_now=True)
	fullName = models.CharField(max_length=500)
	email = models.CharField(max_length=500,blank=True)
	phone = models.CharField(max_length=500,blank=True)

	statement = models.TextField(max_length=1000,blank=True)

	cv = models.FileField(upload_to=location,blank=True)
	portrait = models.FileField(upload_to=location,blank=True)
	reference_1 = models.FileField(upload_to=location,blank=True)
	reference_2 = models.FileField(upload_to=location,blank=True)
	reference_3 = models.FileField(upload_to=location,blank=True)

	## FOR Deploy so we need all the files! :D
	# email = models.CharField(max_length=500)
	# phone = models.CharField(max_length=500)

	# statement = models.TextField(max_length=1000)

	# cv = models.FileField(upload_to=location)
	# portrait = models.FileField(upload_to=location)
	# reference_1 = models.FileField(upload_to=location)
	# reference_2 = models.FileField(upload_to=location)
	# reference_3 = models.FileField(upload_to=location)	

	def __unicode__(self):
		return "%s %s"%(self.fullName,self.uploaded)