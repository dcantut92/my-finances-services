# Django
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    description = models.CharField(max_length=250, blank=False, null=False)
    ammount = models.FloatField(blank=True, null=True, default=0)

    updated_on = models.DateTimeField(auto_now=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'account'


class PeriodicityConfig(models.Model):
    description = models.CharField(max_length=250, blank=False, null=False)
    value = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'account_periodicity_config'


class TransactionConfig(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    description = models.CharField(max_length=250, blank=False, null=False)
    ammount = models.FloatField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    repeat = models.BooleanField(default=False)
    repeat_until = models.DateTimeField(blank=True)
    periodicity_config = models.ForeignKey(PeriodicityConfig)

    updated_on = models.DateTimeField(auto_now=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'account_transaction_config'


class Transaction(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    transaction_config = models.ForeignKey(TransactionConfig, models.DO_NOTHING)
    description = models.CharField(max_length=250, blank=False, null=False)
    ammount = models.FloatField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True)

    updated_on = models.DateTimeField(auto_now=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'account_transaction'

