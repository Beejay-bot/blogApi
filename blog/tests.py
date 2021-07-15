from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category



class Test_create_post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="Python")
        test_user1 = User.objects.create_user(username='testUser1', password='123456')
        test_post  = Post.objects.create(category_id=1, title='test title', excerpt='Test excerpt', content="Test content",slug="test-title",author_id=1, status='published')

    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'testUser1')
        self.assertEqual(title, 'test title')
        self.assertEqual(content, 'Test content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "test title")
        self.assertEqual(str(cat), "Python")

