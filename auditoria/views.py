from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Auditoria, Item, Resposta


def inicio(request):
    auditorias = Auditoria.objects.all().order_by('-data')[:5]
    return render(request, "inicio.html", {"auditorias": auditorias})


@login_required
def nova_auditoria(request):

    ultimo = Auditoria.objects.all().order_by('-num_relatorio').first()

    if ultimo:
        proximo = ultimo.num_relatorio + 1
    else:
        proximo = 1

    if request.method == "POST":
        num_relatorio = int(request.POST.get("num_relatorio"))
        local = request.POST.get("local")
        auditor = request.POST.get("auditor") or request.user.get_full_name() or request.user.username

        auditoria = Auditoria.objects.create(
            num_relatorio=num_relatorio,
            local=local,
            auditor=auditor,
            user=request.user
        )

        return redirect(f"/itens/{auditoria.id}/")

    return render(request, "nova_auditoria.html", {"proximo": proximo})


@login_required
def itens(request, auditoria_id):
    auditoria = Auditoria.objects.get(id=auditoria_id)
    itens = Item.objects.all().order_by('grupo')

    if request.method == "POST":
        for item in itens:
            status = request.POST.get(f"item_{item.id}")
            if status:
                motivo = request.POST.get(f"motivo_{item.id}", "")
                tratativa = request.POST.get(f"tratativa_{item.id}", "")
                Resposta.objects.create(
                    auditoria=auditoria,
                    item=item,
                    status=status,
                    motivo_nc=motivo,
                    tratativa=tratativa
                )

        return redirect("/finalizado/")

    return render(request, "itens.html", {"itens": itens, "auditoria": auditoria})


def finalizado(request):
    return render(request, "finalizado.html")


def historico(request):
    auditorias = Auditoria.objects.all().order_by('-data')
    return render(request, 'auditorias.html', {'auditorias': auditorias})


def auditoria_detail(request, auditoria_id):
    auditoria = Auditoria.objects.get(id=auditoria_id)
    ncs = Resposta.objects.filter(auditoria=auditoria, status='NC').select_related('item')
    return render(request, 'auditoria_detail.html', {'auditoria': auditoria, 'ncs': ncs})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')