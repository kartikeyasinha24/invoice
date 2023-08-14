from rest_framework import viewsets as vs
from .models import invoice, invoicedetail
from .serializers import InvoiceSerializer, InvoicedetSerializer
from rest_framework.response import Response




class invoiceViewSet(vs.ModelViewSet):
    queryset=invoice.objects.all()
    serializer_class=InvoiceSerializer
    http_method_names = ['get','post','retrieve','put','patch']
  		



    



    
