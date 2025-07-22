from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import transcribe_audio
import os

@csrf_exempt
def transcribe(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        file_path = os.path.join('media', audio_file.name)
        with open(file_path, 'wb') as f:
            f.write(audio_file.read())
        try:
            result = transcribe_audio(file_path)
            os.remove(file_path)
            return JsonResponse({"status": "success", "data": result})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)