from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Category, Tag, Comment
from django.urls import reverse

class BlogTests(TestCase):
    def setUp(self):
        """Настройка тестовых данных."""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Тестовая категория')
        self.tag = Tag.objects.create(name='Тестовый тег')
        self.article = Article.objects.create(
            title='Тестовая статья',
            content='Это тестовая статья.',
            author=self.user,
            category=self.category
        )
        self.article.tags.add(self.tag)

    def test_article_creation(self):
        """Проверка создания статьи."""
        self.assertEqual(self.article.title, 'Тестовая статья')
        self.assertEqual(self.article.author.username, 'testuser')

    def test_home_page(self):
        """Проверка главной страницы."""
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая статья')