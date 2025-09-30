from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, CategoryViewSet, AccountViewSet, BudgetViewSet

from . import views

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"budgets", BudgetViewSet)

urlpatterns = [
    path("categorize/", views.categorize_view, name="categorize"),
    path("transactions/", views.transaction_view, name="transaction"),
    path("", include(router.urls)),
]
