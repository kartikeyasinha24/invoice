from rest_framework import serializers
from .models import invoice, invoicedetail




class InvoicedetSerializer(serializers.ModelSerializer):

    class Meta:
        model = invoicedetail
        fields= ['description','quantity','unitprice']



class InvoiceSerializer(serializers.ModelSerializer):  
    invoice_details=InvoicedetSerializer(many=True)
    
    class Meta:
        model = invoice
        fields= ['name','inv_number','invoice_details']

    def create(self, validated_data):
        invoice_details = validated_data.pop('invoice_details')
        profile_instance = invoice.objects.create(**validated_data)
        for iv in invoice_details:
            invoicedetail.objects.create(inv=profile_instance,**iv)
        return profile_instance



 