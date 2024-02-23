from django.contrib import admin
from django.urls import path
from constructionapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
]