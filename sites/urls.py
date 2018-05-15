from django.urls import path
from .views import *
urlpatterns = [
    path('', SitesList.as_view()),
    path('sites/', SitesList.as_view(), name='sites'),
    path('sites/<int:site_id>', OperationsList.as_view(), name='operations_list'),
    path('summary/', Summary.as_view(), name='summary'),
    path('summary-average', SummaryAverage.as_view(), name='summary-average'),
]
