#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "from blog.models import Category; Category.objects.get_or_create(name='Álbuns de Estúdio', defaults={'description': 'Discografia oficial de estúdio de Ariana Grande.'}); Category.objects.get_or_create(name='Notícias', defaults={'description': 'Atualizações sobre lançamentos, turnês e acontecimentos recentes.'}); Category.objects.get_or_create(name='Prêmios', defaults={'description': 'Principais conquistas e reconhecimentos em premiações.'})"