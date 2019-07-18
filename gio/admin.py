from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Import our custom widget and our model from where they're defined
from gio.models import PointOfInterest, Poll, Choice


admin.site.register(PointOfInterest)
admin.site.register(Poll, SimpleHistoryAdmin)
admin.site.register(Choice, SimpleHistoryAdmin)


