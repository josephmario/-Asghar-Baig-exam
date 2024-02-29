# myapp/views.py
from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment, UserProfile

def user_profile_list(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'user_profile_list.html', {'user_profiles': user_profiles})

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()

    return render(request, 'make_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    for payment in payments:
        payment.per_person = payment.amount / payment.recipients.count() if payment.recipients.count() > 0 else None

    return render(request, 'payment_list.html', {'payments': payments})
