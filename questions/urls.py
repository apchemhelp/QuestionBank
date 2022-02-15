from django.urls import path
from . import views

urlpatterns = [
	path("add/", views.add_question),
	path("get/", views.get_questions),
]