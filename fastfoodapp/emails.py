from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponse


def test_email(request):
    send_mail(
        "Test Email",
        "This is a test",
        "noreply@feastfastfood.com",
        ["your_email@gmail.com"],
    )
    return HttpResponse("Test email sent")


# 1 Welcome Email
def send_welcome_email(user):
    subject = "Welcome to Feast Fast Food 🍔"
    context = {"user": user}
    html_message = render_to_string("emails/welcome_email.html", context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
    )


# 2️ Order Confirmation Email
def send_order_confirmation(user, order, items):
    subject = f"Order #{order.id} Confirmed 🍕"
    context = {"user": user, "order": order, "items": items}
    html_message = render_to_string("emails/order_confirmation.html", context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
    )


# 3️ Order Ready Email
def send_order_ready_email(user, order):
    subject = f"Your Order #{order.id} is Ready 🍟"
    context = {"user": user, "order": order}
    html_message = render_to_string("emails/order_ready.html", context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
    )


# 4️ Order Delivered Email
def send_order_delivered_email(user, order):
    subject = f"Your Order #{order.id} is Delivered 🚚"
    context = {"user": user, "order": order}
    html_message = render_to_string("emails/order_delivered.html", context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
    )


def send_contact_emails(name, email, message_text):
    """
    Sends 2 emails:
    1️ To admin (user’s message)
    2️ To user (confirmation)
    """

    # --- Email to Admin ---
    admin_subject = f"📩 New Contact Message from {name}"
    admin_context = {"name": name, "email": email, "message": message_text}
    admin_html = render_to_string("emails/contact_admin.html", admin_context)
    admin_plain = strip_tags(admin_html)
    send_mail(
        admin_subject,
        admin_plain,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_HOST_USER],  # admin email
        html_message=admin_html,
    )

    # --- Email to User ---
    user_subject = "Thanks for contacting Feast Fast Food 🍔"
    user_context = {"name": name}
    user_html = render_to_string("emails/contact_user.html", user_context)
    user_plain = strip_tags(user_html)
    send_mail(
        user_subject,
        user_plain,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=user_html,
    )
