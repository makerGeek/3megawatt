from django.urls import path
from .views import *
urlpatterns = [
    path('', SitesList.as_view()),
    path('sites/', SitesList.as_view()),
    path('sites/<int:site_id>', OperationsList.as_view()),
]
