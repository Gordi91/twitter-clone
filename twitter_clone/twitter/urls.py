from django.urls import path
from twitter import views

urlpatterns = [
    path('', views.SampleView.as_view(), name="sample_view"),
]
