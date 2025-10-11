from django.contrib import admin, messages
from .models import Category, Product
from .models import Order, OrderItem
from .emails import send_order_ready_email, send_order_delivered_email  # ✅ import functions


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'review')
    list_filter = ('category',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username')
    inlines = [OrderItemInline]

    actions = ['mark_ready', 'mark_delivered']

    def mark_ready(self, request, queryset):
        for order in queryset:
            order.status = 'Ready'
            order.save()
            send_order_ready_email(order.user, order)
        self.message_user(request, "Selected orders have been marked as Ready and emails sent.", messages.SUCCESS)

    def mark_delivered(self, request, queryset):
        for order in queryset:
            order.status = 'Delivered'
            order.save()
            send_order_delivered_email(order.user, order)
        self.message_user(request, "Selected orders have been marked as Delivered and emails sent.", messages.SUCCESS)


admin.site.register(Order, OrderAdmin)
