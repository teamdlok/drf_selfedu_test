from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from women.models import Women, Category
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from women.serializers import WomenSerializer



class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )



# Автоматически создаёт представление для обработки url, позволяет делать всё что указано в mixins (которые объединены
# В GenerivViewSet, который мы просто разобрали на части.
# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     @action(methods=['get'], detail=False)
#     def category(selfself, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})

#







# Тут мы можем ручками создавать представления для запросов, где для каждого типа запроса индивидуально проводить
# свои определенные операции
# class WomenAPIView(APIView):
#     def get(self, request):
#         """Преобразовываем model данные в json byte string и отправляем пользователю"""
#         women = Women.objects.all()
#
#         return Response({'posts': WomenSerializer(women, many=True).data})
#
#     def post(self, request):
#         """Преобразовываем json byte string полученный от пользователя в model данные и добавляем в БД"""
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() #Этот метод вызовет функцию create из serializers
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance) # Если в сериализаторе передавать сразу
#         # данные для модели и при этом ещё строку из модели, то в сериализаторе будет вызван update
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exist"})
#
#         return Response({"post": "deleted post" + str(pk)})

# class WomenAPIView(generics.ListAPIView):
    # queryset = Women.objects.all()
    # serializer_class = WomenSerializer
