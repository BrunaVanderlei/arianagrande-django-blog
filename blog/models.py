from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    content = models.TextField('Conteúdo')
    image = models.CharField(
        'Caminho ou URL da imagem',
        max_length=300,
        blank=True,
        help_text='Ex: /static/images/sweetener.webp ou link https://...'
    )
    color = models.CharField(
        'Cor de fundo (Hex)',
        max_length=7,
        blank=True,
        default='#ECDBE0',
        help_text='Ex: #EDDAC9, #AA96A4, #E2B1B6, #847C88, #708076, #9FB0A9, #B81016'
    )
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        blank=True,
        verbose_name='Categorias',
    )
    created_at = models.DateTimeField('Data de publicação', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Autor',
    )
    text = models.TextField('Comentário')
    created_at = models.DateTimeField('Data de postagem', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comentário de {self.author} em {self.post}'
  