from django.db import models
from django.utils import timezone
import re
import datetime

class Purchase(models.Model):
    file_name       = models.CharField('Nom de fichier', max_length=200, unique=True)
    supplier_name   = models.CharField('Nom du fournisseur', null=True, blank=True, default='', max_length=200)
    order_number    = models.CharField('Numéro de commande', max_length=200)
    description     = models.TextField('Description', blank=True, default='')
    purchase_date   = models.DateTimeField('Date de commande', default=timezone.now)
    published_date  = models.DateTimeField('Date d\'ajout', default=timezone.now)
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
    RUB = 'RUB'
    CURRENCY_CHOICE = (
        (EUR,'EUR'),
        (USD,'USD'),
        (GBP,'GBP'),
        (RUB,'RUB'),
    )
    currency = models.CharField(
        max_length  = 3,
        choices     = CURRENCY_CHOICE,
        default     = EUR,
        )
    net_paid            = models.DecimalField('Net payé', max_digits=14, decimal_places=5)
    included_vat        = models.DecimalField('dont TVA', max_digits=13, decimal_places=5)
    currency_to_EUR_rate= models.DecimalField('Taux de change pour 1 EUR', default=1,max_digits=19, decimal_places=10)
    vat_rate            = models.DecimalField('Taux TVA', default=0.2,max_digits=6, decimal_places=5)
    class Meta:
        verbose_name = 'Achat'
        verbose_name_plural = 'Achats'

    def get_data_from_file_name(self):
        match = re.match(r"([^\.\-\s]+)[\.\-\s]+(\d+T\d+)[\.\-\s]+(.*)", self.file_name)
        if match:
            if not self.supplier_name:
                self.supplier_name = match.group(1)
            pattern = '%Y%m%d'
            if 13 <= len(match.group(2)):
                pattern = pattern+'T%H%M'
            if 15 <= len(match.group(2)):
                pattern = pattern+'%S'
            if not self.purchase_date:
                self.purchase_date = datetime.datetime.strptime(match.group(2), pattern)
            if not self.supplier_name:
                self.description = match.group(3)

    def save(self, *args, **kwargs):
        self.get_data_from_file_name()
        super(Purchase, self).save(*args, **kwargs)

    def __str__(self):
        return self.file_name

class PurchaseLine(models.Model):
    description         = models.CharField('Description', max_length=2048)
    quantity            = models.DecimalField('Quantité', max_digits=6, decimal_places=3)
    unit_price          = models.DecimalField('Prix unitaire', max_digits=14, decimal_places=5)
    purchase            = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Ligne achat'
        verbose_name_plural = 'Lignes achat'

    def __str__(self):
        return self.description
