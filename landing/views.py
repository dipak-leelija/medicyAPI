# from django.shortcuts import render
from django.http import JsonResponse
from .models import Plans

def plans(request):
    plans = Plans.objects.all()

    plan_data = []
    for plan in plans:
        plan_data.append({
            'id': plan.id,
            'name': plan.name,
            'price': plan.price,
            'duration': plan.duration,
            'status': plan.status
        })

    return JsonResponse({'plans': plan_data})  
