from rest_framework import serializers

class HelloSerializer(serializers.Serializer): # The second one is the class name, so it's the class name
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10) # create a name field, allow to input any text in the computer
    
