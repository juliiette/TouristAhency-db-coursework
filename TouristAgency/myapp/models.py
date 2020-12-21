from django.db import models


class Tourists(models.Model):
    tourist_id = models.AutoField('Tourist ID', primary_key=True)
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    dob = models.DateField('Date of birth')
    phone_number = models.CharField('Last name', max_length=50)
    address = models.CharField('Address', max_length=150)
    passport = models.CharField('Passport', max_length=15)
    itn = models.IntegerField('ITN', max_length=12)

    class Meta:
        verbose_name = 'Tourist'
        verbose_name_plural = 'Tourists'

    def __str__(self):
        return self.last_name


