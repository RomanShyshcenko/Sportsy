from django.contrib import admin

from subscription import models
# Register your models here.


admin.site.register(models.Subscription)
admin.site.register(models.UserSubscription)
