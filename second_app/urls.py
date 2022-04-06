from django.urls import path
from second_app import views
urlpatterns = [
    path('page1/', views.page1, name="page1"),

]
