
from django.contrib import admin
from django.urls import path
# from landing.views import plans  

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('plans/', plans, name='plans'),
]
