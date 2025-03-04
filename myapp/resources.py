from import_export import resources
from .models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'name', 'lname', 'age')  # Fields to include in the export
        export_order = ('id', 'name', 'lname', 'age')  # Order of columns in the exported file