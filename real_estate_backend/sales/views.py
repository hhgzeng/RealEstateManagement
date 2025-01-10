from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from houses.models import House
from accounts.models import User

@csrf_exempt
def add_house(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        price = data.get('price')
        area = data.get('area')
        floor = data.get('floor')
        salesperson_id = data.get('salesperson_id')
        salesperson = User.objects.filter(id=salesperson_id, role='salesperson').first()
        if not salesperson:
            return JsonResponse({'message': 'Invalid salesperson'}, status=400)
        House.objects.create(price=price, area=area, floor=floor, salesperson=salesperson)
        return JsonResponse({'message': 'House added successfully'})
