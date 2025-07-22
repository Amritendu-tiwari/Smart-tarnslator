from django.test import TestCase
from .views import suggest_titles

class BlogTitleSuggesterTests(TestCase):
    def test_title_suggestion(self):
        content = "This blog discusses AI in education, including personalized learning and automated grading."
        response = self.client.post('/suggest-titles/', {'content': content})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['titles']), 3)