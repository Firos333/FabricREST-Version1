from django.urls import path
from.import views


urlpatterns = [
        path('', views.index,name='index'),
        path('meter',views.meter,name='meter'),
        path('yawn',views.yawn,name='yawn'),
        path('sizing',views.sizing,name='sizing'),
        path('weaver',views.weaver,name='weaver'),



]
