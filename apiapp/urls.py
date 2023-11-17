from django.urls import path
from apiapp import views

urlpatterns = [
    path('studentapi/', views.StudentListView.as_view(), name="studentapi")
    
]
