from django.urls import path
from .views import *
from onlineservice.views import *

urlpatterns = [
    path('addfaculty/',addfaculty),
    path('read/',read),
    path('todolist/',todolist),
    path('read1/',read1),
    path('register/',register),
    path('Login/',Login),
    path('Logout/',Logout),
    path('base/',base),
    path('emailsend/',emailsend),
    path('pdfcreate/',pdfcreate),
    path('delete/<int:id>/',delete),
    path('update/<str:slug>/',update),
    path('profile/',profile),
    path('p1/',p1),
    path('p2/',p2),
    path('p3/',p3),
    path('dash/',dash),
]