from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="accounts"
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateField()
    description = models.TextField()
    auto_categorize = models.BooleanField(default=False)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="transactions"
    )
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="transactions"
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )

    def __str__(self):
        return f"{self.description} - {self.amount}"


class Budget(models.Model):
    PERIOD_LENGTHS = [
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ]

    period = models.CharField(max_length=7, choices=PERIOD_LENGTHS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="budgets"
    )
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="budgets"
    )

    def __str__(self):
        return f"{self.amount} {self.weekly}"
