from rest_framework import serializers
from .models import Student

# Model serializers                                                     # Ture Code

# validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should be start with R') # Ture Code

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)                      # Ture Code
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']                           # Ture Code
        # extra_kwargs = {'name':{'read_only':True}}                    # Ture Code

    # Field Level Validation                                            # Ture Code
    # def validate_roll(self, value):
    #     if value>= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value                                                  # Ture Code
    
    # Object Level Validation
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'denish' and ct.lower() != 'rajkot':
    #         raise serializers.ValidationError('City must be Rajkot')
    #     return data

# Non-Model serializers                                             # Ture Code
# # validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should be start with R')

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators = [start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
    
#     # Field Level Validation
#     def validate_roll(self, value):
#         if value>= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value
    
#     # Object Level Validation
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'denish' and ct.lower() != 'rajkot':
#             raise serializers.ValidationError('City must be Rajkot')
#         return data