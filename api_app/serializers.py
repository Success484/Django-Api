from rest_framework import serializers, exceptions
from .models import Category, Product
from django.contrib.auth.models import User

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=4)

    def validate(self, attrs):
        name = attrs.get('name')
        if name == 'acid':
            raise exceptions.ValidationError('Please note that acid is made up of H2SO4.')
        return attrs

    def create(self, validated_data):
        return Category.objects.create(name=validated_data['name'])
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'category', 'prod_date', 'exp_date', 'ratings', 'dis_price']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'dis_price', 'category', 'exp_date']


class UserCreationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=68, min_length=3, write_only=True)
    password = serializers.CharField(max_length=68, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        user = User.objects.filter(username=attrs.get('username'))
        if user.exists():
            raise exceptions.ValidationError("Username already exists.")

        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise exceptions.ValidationError("The two passwords must be the same.")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )