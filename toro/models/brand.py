from auditlog.registry import auditlog
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Brand Name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'State: {self.state.name} | Brand: {self.name}'

    class Meta:
        db_table = 'brand'

        constraints = [
            models.UniqueConstraint(fields=['state', 'name'],
                                    name='unique_name_in_state')
        ]

    @classmethod
    def register(cls):
        auditlog.register(cls, exclude_fields=['updated_at', 'created_at'])

    @classmethod
    def unregister(cls):
        auditlog.unregister(cls)
