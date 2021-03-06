from django.urls import path
from .views import HomePageView, AboutPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="pages_home"),
    path("about/", AboutPageView.as_view(), name="about_page"),
]
