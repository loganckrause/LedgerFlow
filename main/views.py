from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Transaction, Category, Account, Budget
from .serializers import (
    TransactionSerializer,
    CategorySerializer,
    AccountSerializer,
    BudgetSerializer,
)
from .utils import categorize_transaction


# First view
def index(request):
    return HttpResponse("Hello, welcome to LedgerFlow!")


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
