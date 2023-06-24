from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _

from toro.models.brand import Brand


class DisplayingOrder(models.TextChoices):
    RANDOM = 'random', _('Random')
    ALPHABETICAL = 'alphabetical', _('Alphabetical')


class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Vendor Name')
    logo = models.BinaryField(blank=True, null=True, editable=True, verbose_name='Logo')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vendor'

    @classmethod
    def register(cls):
        auditlog.register(cls, exclude_fields=['updated_at', 'created_at'])

    @classmethod
    def unregister(cls):
        auditlog.unregister(cls)


class VendorHasBrand(models.Model):
    client = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Created At')

    class Meta:
        db_table = 'vendor_has_states'


Vendor.register()
