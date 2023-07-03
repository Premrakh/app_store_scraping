
from django.contrib import admin
from django.urls import path,include
from datascrap.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_scrape/<str:pk>',AppData.as_view())
]
