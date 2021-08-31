from django.db import models

# Create your models here.

class AcountInfo(models.Model):
    user_id=models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Incomes (models.Model):
    date = models.DateField()
    income_type = ('Salary', 'Dividends', 'Freelance', 'Rental Income',  'Other')
    income_source = models.CharField
    income_amount = models.DecimalField(max_digits=10,decimal_places=2)
    user_id = models.ForeignKey(AcountInfo, on_delete=models.CASCADE)


class Expenses (models.Model):
    date = models.DateField()
    expense_type = ('Mortgage',
                    'Rent',
                    'Insurance',
                    'Taxes',
                    'Medical',
                    'Utilities',
                    'Gasoline',
                    'Car',
                    'Loan',
                    'Other')
    expense_source = models.CharField
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(AcountInfo, on_delete=models.CASCADE)

