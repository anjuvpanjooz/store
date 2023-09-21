from detailapp import views
from django.urls import path
app_name='detailapp'
urlpatterns=[
    path('detail/<id>',views.detail,name='detail'),
    path('new/',views.new,name='new'),
    path('add',views.add,name='add'),
    ]