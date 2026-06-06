from django.urls import path
from . import views

urlpatterns = [
    path('create-student/', views.create_student_view, name='create'),
    path('display-students/', views.display_students_view, name='display'),
    path('delete-student/<int:id>/', views.delete_student_view, name='delete'),
    path('update-student/<int:id>/', views.update_student_view, name='update'),
]