from .models import Category, Product, File
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title', 'file', 'file_type')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'files', 'url')