from django.shortcuts import redirect, render
from employee_app.models import employees
from employee_app.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
import logging
logger = logging.getLogger(__name__)
from employee_REST_API import ins_logger
import sys
import json

# Create your views here.
class EmployeeAPI(APIView):
    def get(self, request, regid=None):
        if regid:
            # details of employee correspondong to given regid
            insEmployees = employees.objects.filter(regid = regid).values()
        else:
            # details of all employee
            insEmployees = employees.objects.values()

        if insEmployees.exists():
            msg = "employee details found"
        else:
            msg = "employee details not found"

        responseData = {
                "message":msg,
                "success":True,
                "employees":insEmployees
            }
        return Response(responseData, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            # checking whether employee with email already exists
            email = request.data.get('email')
            if email and employees.objects.filter(email=email).exists():
                return Response({"message":"employee already exists","success":False}, status=status.HTTP_200_OK)
            
            # using serializer for validating data
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                # using serializer to create employee
                msg = serializer.save()
                return Response(msg, status=status.HTTP_200_OK)
            
            # logging the specific error into log/error.log file
            ins_logger.logger.error(json.dumps(serializer.errors), extra={'details':'serializer errors'})

            return Response({"message":"invalid body request","sucess":False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = sys.exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})

            return Response({"message":"employee created failed","sucess":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def put(self, request):
        try:
            # checking whether the given regid id valid or not
            regid = request.data.get('regid')
            try:
                employee = employees.objects.get(regid=regid)
            except employees.DoesNotExist:
                return Response({"error": "no employee found with this regid"}, status=status.HTTP_404_NOT_FOUND)
            
            # using serializer for validating data
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                # updating employee
                msg = serializer.save()
                return Response(msg, status=status.HTTP_200_OK)
            
            # logging the specific error into log/error.log file
            ins_logger.logger.error(json.dumps(serializer.errors), extra={'details':'serializer errors'})

            return Response({"message":"invalid body request","sucess":False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = sys.exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})

            return Response({"message":"employee updation failed","sucess":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, regid=None):
        try:
            # checking whether the given regid id valid or not
            try:
                if not regid:
                    ins_logger.logger.error("regid not found", extra={'details':'input json format error'})
                    return Response({"message":"invalid body request","sucess":False}, status=status.HTTP_400_BAD_REQUEST)
                employee = employees.objects.get(regid=regid)
            except employees.DoesNotExist:
                return Response({"error": "no employee found with this regid"}, status=status.HTTP_404_NOT_FOUND)

            # deleting employee
            employee.delete()

            return Response({"message": "Employee deleted successfully", "regid": regid, "success": True})
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = sys.exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})

            return Response({"message":"employee deletion failed","sucess":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)