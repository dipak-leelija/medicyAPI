# from django.shortcuts import render
from django.http import JsonResponse
from .models import Plans 
from .models import  PlansFeatures

# find plan #
def plans(request):
    plans = Plans.objects.all()

    plan_data = []
    for plan in plans:
        plan_features = PlansFeatures.objects.filter(plan_id=plan.id)
        features_d = []
        for plan_fet in plan_features:
            features_d.append({
                'id': plan_fet.id,
                'feature': plan_fet.features,
                'status': plan_fet.status
            })
        plan_data.append({
            'id': plan.id,
            'name': plan.name,
            'price': plan.price,
            'duration': plan.duration,
            'status': plan.status,
            'features':features_d
        })

    return JsonResponse({'plans': plan_data})  

# find the features #
def plans_features(request):
    features = PlansFeatures.objects.all()
    
    features_data=[]
    for plan_fet in features:
        features_data.append({
            'id'       :plan_fet.id,
            'plan_id'  :plan_fet.plan_id,
            'features' :plan_fet.features,
            'status'   :plan_fet.status,
        })

    return JsonResponse({'features': features_data})     
         