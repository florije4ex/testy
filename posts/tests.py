# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.


class PostTests(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test!')

    def test_text_response(self):
        post = Post.objects.get(id=1)
        expected_object_name = '{}'.format(post.text)
        self.assertEqual(expected_object_name, "just a test!")

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test!')
        self.assertTemplateUsed(response, 'posts.html')
