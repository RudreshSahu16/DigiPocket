
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('signout/',views.SignOut, name="signout"),
    path('doc-page/<str:mode_select>/',views.selectPage, name="selectPage"),
    path('upload-page/<str:doc_select>/',views.uploadPreview, name="upload-page"),
    path('remove/<str:texts>/',views.deleteFile, name="deletefile")

    
]
