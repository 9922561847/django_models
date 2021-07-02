from django.urls import path
from custom_model_field_app import views

urlpatterns =[
    path('customfield/',views.customview,name="customfield"),
]