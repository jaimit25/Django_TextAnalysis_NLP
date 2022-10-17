from django.urls import path
from . import views
# "." represents the current folder and views as we want to map the view functions 
#  this variable is used by django. so naming convcetion should be exact 
# it will configure the URL 
# [IMPORTANT] also we need to configure this urls.py into the main nlp_project urls.py file 
urlpatterns = [
    path('hello/',views.say_hello)
]



