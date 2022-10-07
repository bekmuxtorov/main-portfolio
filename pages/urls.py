from django.urls import path
from .views import HomePageView, WorksListView, WorkDetailView, ContactView

urlpatterns = [
    path('', HomePageView, name = 'home'),
    path('works/', WorksListView.as_view(), name = 'works' ),
    path('works/<int:pk>/', WorkDetailView.as_view(), name='works_detail'),
    path('works/contact/', ContactView.as_view(), name='contact')

]
