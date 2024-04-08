from rest_framework import serializers
from .models import employees
from rest_framework.exceptions import ValidationError
from django.db.models import Max

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'

    def validate(self, data):
        
        expected_fields = [field.name for field in employees._meta.fields]
        for key, value in data.items():
            if key not in expected_fields:
                raise ValidationError(f"Invalid field: {key}")

        required_fields = ['name', 'email', 'age', 'gender', 'phoneNo', 'addressDetails', 'workExperience', 'qualifications', 'projects', 'photo']
        required_inner_fields = {}
        required_inner_fields['addressDetails'] = ['hno', 'street', 'city', 'state']
        required_inner_fields['qualifications'] = ['qualificationName', 'fromDate', 'toDate', 'percentage']
        required_inner_fields['workExperience'] = ['companyName', 'fromDate', 'toDate', 'address']
        required_inner_fields['projects'] = ['titile', 'description']

        for field in required_fields:

            # check required keys in data
            if field not in data:
                raise ValidationError(f"Missing required field: {field}")
            
            # check required keys in dictionary
            if field in ['addressDetails']:
                for i in required_inner_fields[field]:
                    if i not in data[field]:
                        raise ValidationError(f"Missing required field: {i}")
            
            # check required keys in list of dictionary
            if field in ['workExperience', 'qualifications', 'projects']:
                for i in required_inner_fields[field]:
                    for ins in data[field]:
                        if i not in ins:
                            raise ValidationError(f"Missing required field: {i}")

        return data
    
    def create(self, validated_data):

        # finding max id
        max_id = employees.objects.aggregate(max_id=Max('id'))['max_id']

        # coverting max_id +1 to required regid format (eg.EMP001)
        next_regid = f"EMP{max_id + 1:03}" if max_id else 1
        validated_data['regid'] = next_regid

        # creating employee
        employee = super().create(validated_data)
        
        return {"message":"employee created successfully","regid":str(employee.regid),"success":True}
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)
        instance.addressDetails = validated_data.get('addressDetails', instance.addressDetails)
        instance.workExperience = validated_data.get('workExperience', instance.workExperience)
        instance.qualifications = validated_data.get('qualifications', instance.qualifications)
        instance.projects = validated_data.get('projects', instance.projects)
        instance.photo = validated_data.get('photo', instance.photo)
        
        instance.save()
        
        return {"message": "employee details updated successfully", "regid": str(instance.regid), "success": True}
