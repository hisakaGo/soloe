from django.contrib import admin
from cms.models import List


class ListAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'creatorName', 'createdOn',)
  list_display_links = ('id', 'title',)


admin.site.register(List, ListAdmin)

