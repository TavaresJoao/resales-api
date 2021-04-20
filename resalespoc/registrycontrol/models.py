from django.db import models


class Imobiliaria(models.Model):
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    other_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Imovel(models.Model):
    imobiliaria = models.ForeignKey(Imobiliaria, on_delete=models.CASCADE)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=128)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.address


