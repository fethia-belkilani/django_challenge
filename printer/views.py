from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from printer.serializers import PrinterSerializer
from printer.models import Printer

# Create your views here.
class ListPrinterAPIView(ListAPIView):
    """This endpoint list all of the available Printers from the database"""
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class CreatePrinterAPIView(CreateAPIView):
    """This endpoint allows for creation of a Printer"""
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class UpdatePrinterAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Printer by passing in the id of the Printer to update"""
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class DeletePrinterAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Printer from the database"""
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer
    