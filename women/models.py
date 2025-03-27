from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255) # Заголовок
    content = models.TextField(blank=True) # Описание женщины
    time_create = models.DateTimeField(auto_now_add=True)
    tipe_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Category(models.Model):
        name = models.CharField(max_length=100, db_index=True) #Определяет кто эта женщина, например певица или актриса

        def __str__(self):
            return self.name
