# myapp/admin.py
from django.contrib import admin
from .models import UserProfile, Payment

admin.site.register(UserProfile)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payer', 'amount', 'date_paid')
    list_filter = ('payer', 'split_equally', 'date_paid')
    search_fields = ('payer__username', 'recipients__username')

    def display_recipients(self, obj):
        return ', '.join([recipient.username for recipient in obj.recipients.all()])
    
    display_recipients.short_description = 'Recipients'