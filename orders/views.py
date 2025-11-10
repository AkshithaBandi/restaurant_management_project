from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import coupon
from django.utils import timezone

class CouponValidationView(APIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        if not code:
            return Response({"error": "code is required"}, status = status.HTTP_400_BAD_REQUEST)
        
        try:
            coupon = Coupo.objects.get(code = code, 
            is_active = True, 
            valid_from__lte = timezone.now().date(),
            valid_until__gte = timezone.now().date()
            )
            return Response({"success": "coupon is valid", "discount_percentage": coupon.dscount_percentage}, status = status.HTTP_200_OK)
        except Coupo.DoesNotExist:
            return Response({"error" : "invalid or expired coupon"}, status = status.HTTP_400_BAD_REQUEST)
            