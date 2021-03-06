from django.http import JsonResponse

from orders.models import ProductInBasket


def basket_adding(request):
     return_dict = dict()
     session_key = request.session.session_key
     data = request.POST
     product_id = data.get('product_id')
     nmb = data.get('nmb')
     new_product = ProductInBasket.objects.create(session_key=session_key, product_id=product_id, nmb=nmb)
     product_total_nmb = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
     return_dict['product_total_nmb'] = product_total_nmb
     return JsonResponse(return_dict)