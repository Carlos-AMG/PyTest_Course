from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from api.coronavstech.companies.models import Company
from api.coronavstech.companies.serializers import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.request import Request
from fibonacci.naive import fibonacci_naive


# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request: Request):
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="carlosaamg6@gmail.com",
        recipient_list=["carlosaamg6@gmail.com"],
    )
    return Response(
        {"status": "success", "info": "email sent successfully"}, status=200
    )


@api_view(http_method_names=["GET"])
def get_fibonacci_number(request: Request):
    n = int(request.GET.get("n"))
    res = fibonacci_naive(n)
    return Response({"n": n, "fibonacci": res})
