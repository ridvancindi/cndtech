from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = "agenda"

urlpatterns = [
    path('detail/<url>',views.detail,name = "detail"),
    path('',views.index,name = "index"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   