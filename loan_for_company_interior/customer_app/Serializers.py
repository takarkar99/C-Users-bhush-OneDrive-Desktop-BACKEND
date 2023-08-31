from rest_framework import serializers
from .models import Enquiry

class EnquirySerializers(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
        
    def create(self, validated_data):
        return Enquiry.objects.create(**validated_data)
    
    def validate_first_name(self, value):
        import re 
        pattern = '^[A-Z]{1}[a-z]{1,50}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("First letter must be capital")
        return value

    def validate_last_name(self, value):
        import re 
        pattern = '^[A-Z]{1}[a-z]{1,50}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("First letter must be capital")
        return value  

    def validate_message(self, value):
        if len(value) < 5 or len(value) > 200:
            raise serializers.ValidationError(' must contain 3 to 20 charecters')
        return value
    
    def validate_email(self, value):
       import re 
       pattern = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
       if not  re.match(pattern, value):
           raise serializers.ValidationError('Please Maintain the Email Pattern Correctly')
       return value
   
    def validate_mobile(self,value):
        import re
        pattern ='^[+0-9+0-9]'
        if not re.match(pattern, value):
           raise serializers.ValidationError("Plese Insert Correct Mobile Number.")
        return value
