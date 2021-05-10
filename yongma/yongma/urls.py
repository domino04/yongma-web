"""yongma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),  # 인덱스 페이지
    path("introduction/<str:section>/", views.introduction,
         name="introduction"),  # 회사소개 페이지 (5)
    path("businessArea/<str:section>/", views.businessArea,
         name="businessArea"),  # 사업분야 페이지 (4)
    path("portfolio/<str:section>/", views.portfolio,
         name="portfolio"),  # 사업실적 페이지 (2)
    path("community/<str:section>/", views.community,
         name="community"),  # 커뮤니티 페이지 (3)
    path("recruiting/<str:section>/", views.recruiting,
         name="recruiting"),  # 채용안내 페이지 (2)
]
