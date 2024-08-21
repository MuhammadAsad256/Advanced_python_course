import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from functools import reduce

@csrf_exempt
def calculate_total(request):
    data = json.loads(request.body)
    numbers = data.get('numbers')
    
    # total_sum = sum(numbers)
    
    total_sum = reduce(lambda x, y: x + y, numbers)
    return JsonResponse({'numbers':total_sum})



def calculate_average(request):
    data = json.loads(request.body)
    numbers = data.get('numbers')
    
    # average = sum(numbers) / len(numbers)
    
    average = reduce(lambda x, y: x + y, numbers) / len(numbers)
    return JsonResponse({'numbers': average})


def calculate_product(request):
    data = json.loads(request.body)
    numbers = data.get('numbers')

    # total_product = 1

    # for number in numbers:
    #     total_product = total_product * number

    total_product = reduce(lambda x, y: x * y, numbers)
    return JsonResponse({'numbers':total_product})
