from django.urls import path

from leads.views import home_page

urlpatterns = [
    path('', home_page)
]