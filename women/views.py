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
        serializer.save() #Этот метод вызовет функцию create из serializers
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = WomenSerializer(data=request.data, instance=instance) # Если в сериализаторе передавать сразу
        # данные для модели и при этом ещё строку из модели, то в сериализаторе будет вызван update
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exist"})

        return Response({"post": "deleted post" + str(pk)})

# class WomenAPIView(generics.ListAPIView):
    # queryset = Women.objects.all()
    # serializer_class = WomenSerializer
