"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include("app1.appurls")),
    path('app2/',include("app2.appurls")),
    path('app3/',include('app3.appurls')),
    path('app4/',include("app4.appurls")),
    path('app5/',include("app5.appurls")),
    path('app6/',include("app6.appurls")),
    path('app7/',include("app7.appurls")),
    path('app8/',include("app8.appurls"))
]
