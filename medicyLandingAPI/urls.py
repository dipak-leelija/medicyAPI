
from django.contrib import admin
from django.urls import path
from landing.views import plans , plans_features

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plans/', plans, name='plans'),
     path('plansFeatures/',  plans_features, name=' plansFeatures'),
]
