from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class c_groups(models.Model):
	name =models.CharField(max_length=200, null=False)
	cuser = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
	cdate = models.DateTimeField(auto_now_add=True, null=True)
	remember = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class c_cards(models.Model):
	class levels(models.IntegerChoices):
		Normal = 1
		Middle = 2
		High = 3
	group_id = models.ForeignKey(c_groups, null=False, on_delete= models.CASCADE)
	title =models.CharField(max_length=50, null=True)
	body =models.CharField(max_length=200, null=True)
	cdate = models.DateTimeField(auto_now_add=True, null=True)
	cuser = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
	importancy=models.IntegerField(choices=levels.choices)
	remember=models.BooleanField(default=False)
	times =models.IntegerField(default=1)
	def __str__(self):
		return self.title + " " + self.body