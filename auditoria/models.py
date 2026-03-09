from django.db import models

from django.conf import settings

class Auditoria(models.Model):
    num_relatorio = models.IntegerField()
    local = models.CharField(max_length=200)
    auditor = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    data = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    grupo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)

class Resposta(models.Model):
    auditoria = models.ForeignKey(Auditoria, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    STATUS = [
        ("C", "Conforme"),
        ("NC", "Não Conforme"),
        ("NA", "Não Aplica")
    ]

    status = models.CharField(max_length=2, choices=STATUS)
    motivo_nc = models.TextField(blank=True)
    tratativa = models.TextField(blank=True)