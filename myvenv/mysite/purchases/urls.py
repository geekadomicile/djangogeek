from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.list_purchases, name='list_purchases'),
    url(r'^new/$',views.new_purchase, name='new_purchase'),
    ]
