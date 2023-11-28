from django.urls import path
from .views import (
add_to_cart,
remove_from_cart,
update_cart,
view_cart,
Shop,
checkout,
)
app_name='shop'
urlpatterns=[
     path('shop', Shop, name='shop'),
     path('checkout/', checkout, name='checkout'),

     path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
     path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
     path('update_cart/<int:product_id>/', update_cart, name='update_cart'),
     path('view_cart', view_cart, name='view_cart'),

]