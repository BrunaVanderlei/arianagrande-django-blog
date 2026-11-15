#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "from blog.models import Category; Category.objects.get_or_create(name='Álbuns de Estúdio', defaults={'description': 'Coletânea dos álbuns de estúdio oficiais lançados por Ariana Grande, explorando suas diferentes fases musicais, sonoridades e identidades visuais.'}); Category.objects.get_or_create(name='Notícias', defaults={'description': 'Atualizações sobre lançamentos, bastidores de produção, turnês, colaborações e os principais acontecimentos recentes da carreira de Ariana Grande.'}); Category.objects.get_or_create(name='Prêmios', defaults={'description': 'Registros das principais conquistas, indicações e reconhecimentos recebidos por Ariana Grande em premiações como o Grammy Awards, Billboard Music Awards e MTV Video Music Awards.'})"