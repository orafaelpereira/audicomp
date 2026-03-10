from django.contrib import admin # type: ignore
from .models import Auditoria, Item, Resposta


@admin.action(description="Criar itens padrão")
def criar_itens(modeladmin, request, queryset):

    dados = [
        ("REAÇÃO DAS PESSOAS","MUDANDO DE POSIÇÃO"),
        ("REAÇÃO DAS PESSOAS","PARANDO O SERVIÇO"),
        ("REAÇÃO DAS PESSOAS","AJUSTANDO EPI"),
        ("REAÇÃO DAS PESSOAS","ADEQUANDO O SERVIÇO"),
        ("REAÇÃO DAS PESSOAS","BATER CONTRA/SER ATINGIDO POR"),
        ("REAÇÃO DAS PESSOAS","FICAR PRESO"),
        ("REAÇÃO DAS PESSOAS","RISCO DE QUEDA"),
        ("REAÇÃO DAS PESSOAS","RISCO DE QUEIMADURA"),
        ("REAÇÃO DAS PESSOAS","RISCO DE CHOQUE ELÉTRICO"),
        ("REAÇÃO DAS PESSOAS","INALAR CONTAMINANTES"),
        ("REAÇÃO DAS PESSOAS","ABSORVER CONTAMINANTES"),
        ("REAÇÃO DAS PESSOAS","INGERIR CONTAMINANTES"),
        ("REAÇÃO DAS PESSOAS","POSTURA INADEQUADA"),
        ("REAÇÃO DAS PESSOAS","ESFORÇO INADEQUADO"),

        ("EPI´S","CABEÇA"),
        ("EPI´S","SISTEMA RESPIRATÓRIO"),
        ("EPI´S","OLHOS E ROSTO"),
        ("EPI´S","OUVIDOS"),
        ("EPI´S","MÃOS E BRAÇOS"),
        ("EPI´S","TRONCO"),
        ("EPI´S","PÉS E PERNAS"),

        ("FERRAMENTAS E EQUIPAMENTOS","IMPRÓPRIAS PARA O SERVIÇO"),
        ("FERRAMENTAS E EQUIPAMENTOS","USADOS INCORRETAMENTE"),
        ("FERRAMENTAS E EQUIPAMENTOS","EM CONDIÇÕES INSEGURAS"),

        ("PROCEDIMENTOS","INADEQUADOS"),
        ("PROCEDIMENTOS","NÃO EXISTEM PROCEDIMENTOS ESCRITOS"),
        ("PROCEDIMENTOS","ADEQUADOS E NÃO SEGUIDOS"),

        ("ORDEM, LIMPEZA E ARRUMAÇÃO","LOCAL SUJO"),
        ("ORDEM, LIMPEZA E ARRUMAÇÃO","LOCAL DESORGANIZADO"),
        ("ORDEM, LIMPEZA E ARRUMAÇÃO","LOCAL COM VAZAMENTOS E POLUIÇÃO"),
    ]

    for g, d in dados:
        Item.objects.get_or_create(grupo=g, descricao=d)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    actions = [criar_itens]


admin.site.register(Auditoria)
admin.site.register(Resposta)