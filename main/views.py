from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, Category, Account, Budget
from .serializers import (
    TransactionSerializer,
    CategorySerializer,
    AccountSerializer,
    BudgetSerializer,
)
from .utils import categorize_transaction

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()


# First view
def index(request):
    return HttpResponse("Hello, welcome to LedgerFlow!")


@api_view(["POST"])
def categorize_view(request):

    description = request.data.get("description", "")
    if not description:
        return Response(
            {"error": "Description required"}, status=status.HTTP_400_BAD_REQUEST
        )
    category = categorize_transaction(description, client)
    return Response({"category": category})


@api_view(["POST"])
def transaction_view(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        print("valid")
        serializer.save()
        print("saved")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    print("invalid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        description = self.request.data.get("description", "")
        category = categorize_transaction(description)  # Call the Gemini API
        serializer.save(category=category)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
