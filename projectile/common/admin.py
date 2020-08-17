from django.contrib import admin

from reversion.admin import VersionAdmin

from common.models import SoftDeleteFilter


# Register your models here.
class SoftDeleteAdmin(VersionAdmin):
    actions = ('delete', 'restore', 'hard_delete')
    # list_filter = (SoftDeleteFilter,)

    def get_list_filter(self, request):
        list_filter = super(SoftDeleteAdmin, self).get_list_filter(request)
        if request.user.is_superuser:
            return (SoftDeleteFilter,) + list_filter
        return list_filter

    def get_queryset(self, request):
        qs = super(SoftDeleteAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_deleted=False)

    def hard_delete(self, request, queryset):
        for item in queryset:
            item.hard_delete()

    def delete(self, request, queryset):
        for item in queryset:
            item.delete()

    def restore(self, request, queryset):
        for item in queryset:
            item.restore()

    def get_actions(self, request):
        actions = super(SoftDeleteAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['restore']
            del actions['hard_delete']
        return actions
