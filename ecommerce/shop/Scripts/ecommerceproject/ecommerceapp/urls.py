from django.urls import path
from . import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]