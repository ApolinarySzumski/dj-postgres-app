from django.urls import path
from .views import UsersViewset

urlpatterns = [
    path('myusers/', UsersViewset.as_view()),
    path('myusers/<int:id>', UsersViewset.as_view())
]
