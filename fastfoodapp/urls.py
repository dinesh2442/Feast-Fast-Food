from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("combooffer/", views.combooffer, name="combooffer"),
    path("veg/", views.veg, name="veg"),
    path("nonveg/", views.nonveg, name="nonveg"),

    # Generic handler for all other categories
    path("menu/<str:category_name>/", views.category, name="category"),

    # --- CART URLS ---
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/clear/", views.clear_cart, name="clear_cart"),
    path("cart/update/<int:product_id>/<str:action>/", views.update_cart, name="update_cart"),
    # Checkout / Order URLs
    path("checkout/", views.checkout, name="checkout"),  # Checkout creates order & shows order details
    path("my-orders/", views.my_orders, name="my_orders"),  # List of user orders
    # search bar url
    path("search/", views.search, name="search"),
    path("contact/", views.contact_footer, name="contact_footer"),

]
