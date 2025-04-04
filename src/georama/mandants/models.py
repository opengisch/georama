from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "mandants"


class Domain(DomainMixin):

    class Meta:
        app_label = "mandants"
