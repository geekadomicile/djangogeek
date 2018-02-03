from django.db import models
from django.utils import timezone

class Purchase(models.Model):
    file_name           = models.CharField(max_length=200, unique=True)
    supplier_name       = models.CharField(max_length=200)
    order_number        = models.CharField(max_length=200)
    file_path           = models.CharField(blank=True,default='',max_length=2048)
    details             = models.TextField(blank=True,default='')
    purchase_date       = models.DateTimeField('date de commande',default=timezone.now)
    published_date      = models.DateTimeField('date d\'ajout',default=timezone.now)
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
    RUB = 'RUB'
    CURRENCY_CHOICE             = (
        (EUR,'EUR'),
        (USD,'USD'),
        (GBP,'GBP'),
        (RUB,'RUB'),
    )
    currency              = models.CharField(
        max_length  = 3,
        choices     = CURRENCY_CHOICE,
        default     = EUR,
        )
    net_paid            = models.DecimalField(max_digits=14, decimal_places=5)
    included_vat       = models.DecimalField(max_digits=13, decimal_places=5)
    currency_to_EUR_rate= models.DecimalField(default=1,max_digits=19, decimal_places=10)
    vat_rate            = models.DecimalField(default=0.2,max_digits=6, decimal_places=5)

    def __str__(self):
        return self.file_name

class PurchaseLine(models.Model):
    description         = models.CharField(max_length=2048)
    quantity            = models.DecimalField(max_digits=6, decimal_places=3)
    unit_price          = models.DecimalField(max_digits=14, decimal_places=5)
    purchase            = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
