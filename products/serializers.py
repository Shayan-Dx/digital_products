from .models import Category, Product, File
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title', 'file')


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    file_set = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'avatar', 'categories', 'file_set')