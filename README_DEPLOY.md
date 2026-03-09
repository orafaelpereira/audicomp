Deploy rápido (GitHub -> Render)

1) Commit e push para seu repositório GitHub
   git init
   git add .
   git commit -m "Prepare app for deploy"
   git branch -M main
   git remote add origin https://github.com/<seu-usuario>/<seu-repo>.git
   git push -u origin main

2) Criar serviço no Render:
   - New -> Web Service -> Connect to GitHub -> Escolha o repo
   - Branch: main
   - Build Command: pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput
   - Start Command: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT

3) Variáveis de ambiente (Settings -> Environment):
   - DJANGO_SECRET_KEY: (uma chave segura)
   - DJANGO_DEBUG: False
   - DJANGO_ALLOWED_HOSTS: <dominio_render>, or leave blank to allow all during testing

4) Crie um superuser (pelo terminal local ou pelo dashboard do Render via "Run Command"):
   python manage.py createsuperuser

Notas:
- Não use runserver em produção.
- Antes de deploy em produção, ajuste DEBUG=False e ALLOWED_HOSTS corretamente.
