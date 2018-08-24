from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.root),
	url(r'^register$', views.register),
	url(r'^home$', views.index),
	url(r'^add_course$', views.add_course),
	url(r'^remove/(?P<course_id>\d+)$', views.remove),
	url(r'^delete/(?P<course_id>\d+)$', views.delete),
	url(r'^join_uni$', views.join_uni),
]