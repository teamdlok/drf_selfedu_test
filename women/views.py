from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women
from women.serializers import WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        """Преобразовываем model данные в json byte string и отправляем пользователю"""
        women = Women.objects.all()

        return Response({'posts': WomenSerializer(women, many=True).data})

    def post(self, request):
        """Преобразовываем json byte string полученный от пользователя в model данные и добавляем в БД"""
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #Добавляем в БД сериализованные данные
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': WomenSerializer(post_new).data})


# class WomenAPIView(generics.ListAPIView):
    # queryset = Women.objects.all()
    # serializer_class = WomenSerializer
