from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transcriber.utils import transcribe_audio
from blog_title_suggester.utils import generate_titles
import os
from django.conf import settings
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def home(request):
    transcription_result = None
    title_suggestions = None
    
    if request.method == 'POST':
        logger.debug(f"POST request received: {request.POST}, Files: {request.FILES}")
        if 'audio' in request.FILES:
            # Handle audio transcription
            audio_file = request.FILES['audio']
            logger.debug(f"Audio file received: {audio_file.name}")
            file_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
            try:
                with open(file_path, 'wb') as f:
                    f.write(audio_file.read())
                logger.debug(f"Audio file saved to: {file_path}")
                result = transcribe_audio(file_path)
                logger.debug(f"Raw transcription result: {result}")
                # Standardize result to match API format
                status_value = str(result["status"])
                if hasattr(result["status"], "value"):
                    status_value = result["status"].value
                transcription_result = {
                    "status": "success" if status_value == "completed" else "error",
                    "data": result if status_value == "completed" else None,
                    "message": result.get("error", "Unknown error") if status_value != "completed" else None
                }
                logger.debug(f"Formatted transcription result: {transcription_result}")
                os.remove(file_path)  # Clean up
            except Exception as e:
                logger.error(f"Transcription error: {str(e)}")
                transcription_result = {"status": "error", "message": str(e)}
        
        elif 'content' in request.POST or 'text_file' in request.FILES:
            # Handle title suggestions
            content = request.POST.get('content', '')
            if 'text_file' in request.FILES:
                text_file = request.FILES['text_file']
                try:
                    content = text_file.read().decode('utf-8')
                    logger.debug(f"Text file content: {content}")
                except Exception as e:
                    logger.error(f"Text file error: {str(e)}")
                    title_suggestions = ["Error reading text file"]
            if content:
                try:
                    title_suggestions = generate_titles(content)
                    logger.debug(f"Title suggestions: {title_suggestions}")
                except Exception as e:
                    logger.error(f"Title generation error: {str(e)}")
                    title_suggestions = ["Error generating titles"]
    
    return render(request, 'home.html', {
        'transcription_result': transcription_result,
        'title_suggestions': title_suggestions
    })