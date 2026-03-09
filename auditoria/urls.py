from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("nova/", views.nova_auditoria, name="nova_auditoria"),
    path("itens/<int:auditoria_id>/", views.itens, name="itens"),
    path("finalizado/", views.finalizado, name="finalizado"),
    path("historico/", views.historico, name="historico"),
    path("auditoria/<int:auditoria_id>/", views.auditoria_detail, name="auditoria_detail"),
]