from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import generate_titles

@csrf_exempt
def suggest_titles(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if not content:
            return JsonResponse({"status": "error", "message": "Content is required"}, status=400)
        try:
            titles = generate_titles(content)
            return JsonResponse({"status": "success", "titles": titles})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)