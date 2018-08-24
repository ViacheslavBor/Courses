from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages 
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def root(request):
	return render(request, 'courses/reg.html')

def register(request):
	if request.method != "POST":
		return redirect('/')
	error = False
	if len(request.POST['name']) < 3:
		messages.error(request, "Name must be 3 or more characters")
		error = True
	if len(request.POST['password']) < 3:
		messages.error(request, "Password must be 3 or more characters")
		error = True
	if request.POST['password'] != request.POST['confirm']:
		messages.error(request, "PW and PW confirm dont match")
		error = True
	if not request.POST['name'].isalpha():
		messages.error(request, "Choose a better name")
		error = True
	if not EMAIL_REGEX.match(request.POST['email']):
		messages.error(request, "Provide a better email")
		error = True
	if error:
		return redirect('/')

	hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
	user = User.objects.create(name = request.POST['name'], email = request.POST['email'], password = request.POST['password'])
	request.session['id'] = user.id
	return redirect('/home')

def index(request):
	if not 'id' in request.session:
		messages.error(request, "OUT!")
		return redirect('/')
	context = {
		'user': User.objects.get(id = request.session['id']),
		'all_courses': Course.objects.all(), 
		'all_universities': University.objects.all(),
	}
	return render(request, 'courses/main.html', context)

def add_course(request):
	university = University.objects.get(id = request.POST['university'])
	course = Course.objects.create(name=request.POST['name'], 
	description=request.POST['description'])
	university.courses.add(course)
	return redirect('/home')

def remove(request, course_id):
	context ={
		'course': Course.objects.get(id=course_id)
	}
	return render(request, 'courses/delete.html', context)

def delete(request, course_id):
	Course.objects.get(id = course_id).delete()
	return redirect('/home')

def join_uni(request):
	user = User.objects.get(id = request.session['id'])
	university = University.objects.get(id = request.POST['university'])
	user.uni = university
	user.save()
	return redirect('/home')

