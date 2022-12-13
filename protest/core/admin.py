# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from .task import send_email_users
#
#
# class UserAdmin(UserAdmin):
#
#     actions = ['send_email_action']
#
#     def send_email_action(self, request, queryset):
#         send_email_users.delay()
#         updated_fields = queryset.update(is_staff=True)
#         return True
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
