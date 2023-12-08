from django.db import models

class DBFTable(models.Model):
    madre = models.CharField(max_length=10)
    hija = models.CharField(max_length=10)
    # Agrega otros campos según la estructura de tu tabla DBF
