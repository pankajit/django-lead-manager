from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset => allows us to create a full CRUD API without having to
#   specify explicit methods for the functionality
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all() # Gets all the leads
    permission_classes = [
        permissions.AllowAny # allows anyone to access your leads
    ]
    serializer_class = LeadSerializer # the serializer that we created