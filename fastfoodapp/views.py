from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from .models import Product, Category, Order, OrderItem
from .emails import send_order_confirmation
from .emails import send_contact_emails


def landing(request):
    categories = Category.objects.prefetch_related("products").all()
    category_data = []

    for cat in categories:
        if cat.name.lower() == "combo offer":
            products = cat.products.all()
        else:
            products = cat.products.all()[:4]

        category_data.append({
            "id": cat.id,
            "name": cat.name,
            "products": products
        })

    cart = request.session.get('cart', {})

    return render(request, "landing.html", {
        "categories": category_data,
        "cart": cart
    })


# -----------------------
# Fixed category views
# -----------------------
def combooffer(request):
    products = Product.objects.filter(category__name="Combo Offer")
    return render(request, "combo.html", {"title": "Combo Offer", "products": products})


def veg(request):
    products = Product.objects.filter(category__name="Veg")
    cart = request.session.get("cart", {})
    return render(request, "veg.html", {"title": "Veg", "products": products, "cart": cart})


def nonveg(request):
    products = Product.objects.filter(category__name="Non-Veg")
    cart = request.session.get("cart", {})
    return render(request, "nonveg.html", {"title": "Non-Veg", "products": products, "cart": cart})


# -----------------------
# Generic category handler
# -----------------------
def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    cart = request.session.get("cart", {})
    products = Product.objects.filter(category=category)

    # Only handle categories OTHER than Veg, Non-Veg, Combo Offer
    if category_name in ["Veg", "Non-Veg", "Combo Offer"]:
        # Redirect them to their specific views instead
        if category_name == "Veg":
            return veg(request)
        elif category_name == "Non-Veg":
            return nonveg(request)
        elif category_name == "Combo Offer":
            return combooffer(request)

    # For all other categories → use category.html
    return render(
        request,
        "category.html",
        {
            "title": category.name,
            "category": category,
            "products": products,
            "cart": cart,
        },
    )


# --- CART VIEWS ---

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1
    else:
        cart[str(product_id)] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": 1,
        }

    request.session["cart"] = cart
    next_url = request.GET.get("next")
    if next_url:
        return HttpResponseRedirect(next_url)
    return redirect("landing")


def view_cart(request):
    cart = request.session.get("cart", {})
    total = sum(item["quantity"] * item["price"] for item in cart.values())
    item_count = sum(item["quantity"] for item in cart.values())

    return render(request, "cart.html", {
        "cart": cart,
        "total": total,
        "item_count": item_count
    })


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session["cart"] = cart
    return redirect("view_cart")


def clear_cart(request):
    request.session["cart"] = {}
    return redirect("view_cart")


def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        if action == 'increment':
            cart[product_id]['quantity'] += 1
        elif action == 'decrement':
            cart[product_id]['quantity'] -= 1
            if cart[product_id]['quantity'] <= 0:
                del cart[product_id]
    request.session['cart'] = cart
    # redirect to the page the user came from
    return redirect(request.GET.get('next', 'landing'))


# @login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('landing')

    total = sum(item['price'] * item['quantity'] for item in cart.values())

    # Save the order
    order = Order.objects.create(user=request.user, total=total)

    items = []  # store all items for email
    for item in cart.values():
        order_item = OrderItem.objects.create(
            order=order,
            product_name=item['name'],
            price=item['price'],
            quantity=item['quantity']
        )
        items.append(order_item)

    # ✅ Send confirmation email
    send_order_confirmation(request.user, order, items)

    # Clear cart
    request.session['cart'] = {}
    messages.info(request, 'Order was Confirmed')
    return redirect('my_orders')


def my_orders(request):
    if not request.user.is_authenticated:
        # Just render a template with login message
        return render(request, "my_orders.html", {
            "orders_data": None,
            "not_logged_in": True
        })

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    orders_data = []
    for order in orders:
        items = []
        for item in order.items.all():
            subtotal = item.price * item.quantity
            items.append({
                'product_name': item.product_name,
                'price': item.price,
                'quantity': item.quantity,
                'subtotal': subtotal
            })
        orders_data.append({
            'order': order,
            'items': items
        })

    return render(request, "my_orders.html", {
        "orders_data": orders_data,
        "not_logged_in": False
    })


def search(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)

    # Get cart from session (or your cart logic)
    cart = request.session.get('cart', {})  # If you store cart in session

    return render(request, "search_results.html", {
        "query": query,
        "results": results,
        "cart": cart
    })


def contact_footer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            messages.error(request, "All fields are required.")
            return redirect(request.META.get('HTTP_REFERER', 'landing'))

        # Send emails (admin + user)
        send_contact_emails(name, email, message)

        messages.success(request, "Message sent successfully! Check your email for confirmation.")
        return redirect(request.META.get('HTTP_REFERER', 'landing'))

    return redirect('landing')
