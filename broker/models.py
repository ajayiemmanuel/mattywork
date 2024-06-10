from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models

# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return str(self.name)


class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    capital_balance = models.CharField (max_length = 200, default = "0.00",)
    btc = models.CharField (max_length = 200,  null = True, default = "0.00",)
    usd = models.CharField (max_length = 200, default = "0.00",)
    bonus_usd = models.CharField (max_length = 200, default = "0.00",)
    plan = models.CharField (max_length = 200, default = "Silver",)
    verify = models.CharField (max_length = 200, default = "Unverified",)
    currency = models.CharField (max_length = 200, default = "$",)



    def __str__(self):
        return str(self.name)


class Profile (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)


    def __str__(self):
        return str(self.name)


class Account (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    account_number = models.CharField (max_length = 200,  null = True, default = "",)
    account_name = models.CharField (max_length = 200, default = " ",)
    bank_name = models.CharField (max_length = 200, default = " ",)
    swift_code = models.CharField (max_length = 200, default = " ",)
    bitcoin_address = models.CharField (max_length = 200,  null = True, default = " ",)
    ethereum_address = models.CharField (max_length = 200, default = " ",)
    cashapp_tag = models.CharField (max_length = 200, default = " ",)
    paypal_email = models.CharField (max_length = 200, default = " ",)


    def __str__(self):
        return str(self.name)


class Wiretransfer(models.Model):
    class Meta:
        verbose_name = 'Wiretransfer'
        verbose_name_plural = 'Wiretransfers'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    bank = models.CharField(max_length=254, null=True, blank=True)
    accountnumber = models.CharField(max_length=254, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    swift = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.CharField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Banktransfer(models.Model):
    class Meta:
        verbose_name = 'Banktransfer'
        verbose_name_plural = 'Banktransfers'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    bank = models.CharField(max_length=254, null=True, blank=True)
    accountnumber = models.CharField(max_length=254, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    swift = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.CharField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Bitcoin(models.Model):
    class Meta:
        verbose_name = 'Bitcoin'
        verbose_name_plural = 'Bitcoins'
        
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    wallet = models.CharField(max_length=250, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.CharField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Kyc(models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    first_name = models.CharField (max_length = 200,  null = True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=254, null=True, blank=True)
    country_code = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)
    month = models.CharField(max_length=250, null=True, blank=True)
    day = models.CharField(max_length=250, null=True, blank=True)
    valid_id_front = models.ImageField (null = True, blank = True)
    valid_id_back = models.ImageField ( null = True, blank = True)

    def __str__(self):
        return str(self.name)

class Wallet (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    btc = models.CharField (max_length = 200, default = "4",)
    eth = models.CharField (max_length = 200, default = "-",)
    usdt = models.CharField (max_length = 200, default = "-",)
    usdc = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return str(self.name)



class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)


class Report (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    Report = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return str(self.name)