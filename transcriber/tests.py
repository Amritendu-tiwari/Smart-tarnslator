from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import transcribe

class TranscriberTests(TestCase):
    def test_invalid_audio_format(self):
        file = SimpleUploadedFile("test.txt", b"not an audio file", content_type="text/plain")
        response = self.client.post('/transcribe/', {'audio': file})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')