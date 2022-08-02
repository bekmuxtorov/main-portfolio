from django.urls import path
from .views import HomePageView, WorksListView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('works/', WorksListView.as_view(), name = 'works' )
]
