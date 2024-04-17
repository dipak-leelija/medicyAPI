
from django.contrib import admin
from django.urls import path
# from landing.views import fetch_plans  

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('fetch-plans/', fetch_plans, name='fetch_plans'),
]
