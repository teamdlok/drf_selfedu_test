import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = ("__all__")




#Старая схема сериализатора, где всё прописано вручную

# class WomenSerializer(serializers.Serializer):
#     """Указываем какие строки в нашей модели принадлежат к какому типу данных"""
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)#Чтобы не возникала ошибка при POST запросе, делаем readonly
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data): #Если в сериализатор указать только данные для таблицы, то save
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):  #Если указать данные для таблицы и строку из таблицы, то update
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

#
# def encode():
#     """Тут мы сделали базовое преобразование информации из базы данных в json байтовую строку"""
#     model = WomenModel('Angelina Jolie', 'Text for Agnelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     """Тут мы докедируем байтовую json строку преобразуя в словарь python"""
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Text for Agnelina Jolie"}')
#     data = JSONParser().parse(stream=stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)