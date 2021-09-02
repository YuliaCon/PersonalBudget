from django.contrib import admin

# Register AccountInfo model.
from .models import AccountInfo
admin.site.register(AccountInfo)

# Register Incomes model
from .models import Income
admin.site.register(Income)

#Register Expenses model

from  .models import Expense
admin.site.register(Expense)
