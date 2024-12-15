import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_notification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')

        if status == 'start':
            pass
        elif status == 'end':
            pass

        return JsonResponse({'status': 'Notification received'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

