🗂️ Project Structure

```
fastfood/
├── accounts
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── assets
│   ├── admin
│   │   ├── css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   ├── img
│   │   │   ├── gis
│   │   └── js
│   │       ├── admin
│   │       ├── vendor
│   │       │   ├── jquery
│   │       │   ├── select2
│   │       │   │   ├── i18n
│   │       │   └── xregexp
│   ├── css
│   ├── resources
│   │   ├── Chicken Dishes
│   │   ├── combo offer
│   │   ├── non-veg
│   │   ├── veg
├── fastfood
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── fastfoodapp
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_rename_rating_product_review.py
│   │   ├── 0003_alter_product_options_product_position.py
│   │   ├── 0004_alter_product_options_remove_product_position.py
│   │   ├── 0005_alter_product_options_product_sort_order.py
│   │   ├── 0006_alter_product_sort_order.py
│   │   ├── 0007_alter_product_options_remove_product_sort_order.py
│   │   ├── 0008_order_orderitem.py
│   │   ├── 0009_alter_order_status_alter_order_total_and_more.py
│   │   └── __init__.py
│   ├── static
│   │   ├── css
│   │   └── resources
│   │       ├── Chicken Dishes
│   │       ├── combo offer
│   │       ├── non-veg
│   │       ├── veg
│   ├── templates
│   │   ├── accounts
│   │   ├── emails
│   │   ├── __init__.py
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── cart_extras.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── emails.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media
│   └── products
├── __init__.py
├── manage.py
```