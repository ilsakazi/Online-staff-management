from django.urls import path
from .views import *
from leaves.views import *

urlpatterns = [
    path('leaves/',leaves),
    path('readleaves/',readleaves),
    path('updateleaves/<int:id>/',updateleaves),
    path('deleteleaves/<int:id>/',deleteleaves),
]