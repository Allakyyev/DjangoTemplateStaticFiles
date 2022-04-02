from django.urls import path
from second_app import views
urlpatterns = [
    path('page1/', views.index, name="Page1"),
]
