from django.shortcuts import render
from .models import Purchase
from .forms import PurchaseForm
from django.utils import timezone

def list_purchases(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchases/list_purchases.html', {'purchases':purchases})

def new_purchase(request):
    if request.method == "POST":
        form = PurchaseFormSet(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.published_date = timezone.now()
            purchase.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = PurchaseForm()
    return render(request, 'purchases/new_purchase.html', {'form':form})
