# from django.shortcuts import render
from django.http import JsonResponse
# from .models import Plan

# def fetch_plans(request):
#     plans = Plan.objects.all()

#     plan_data = []
#     for plan in plans:
#         plan_data.append({
#             'name': plan.name,
#             'price': plan.price,
#             'duration': plan.duration,
#             'status': plan.status
#         })

#     return JsonResponse({'plans': plan_data})  
