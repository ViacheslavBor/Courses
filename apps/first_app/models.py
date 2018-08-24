from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
class University(models.Model):
	name = models.CharField(max_length=255)
	courses = models.ManyToManyField(Course, related_name = "universities")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	uni = models.ForeignKey(University, related_name = 'students', null = True)
	courses = models.ManyToManyField(Course, related_name = 'users')

# All students of a specific university
# University.objects.first().students.all()
# User.objects.filter(uni = University.objects.first())