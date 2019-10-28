from django.db import models

class Article(models.Model):
    article_title = models.CharField('Назва статті', max_length = 200)
    article_text = models.TextField('Текст статті')
    pub_date = models.DateTimeField('Дата публікації')

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField("Ім'я автора", max_length = 50)
    comment_text = models.CharField('Текст коментаря', max_length = 200)
