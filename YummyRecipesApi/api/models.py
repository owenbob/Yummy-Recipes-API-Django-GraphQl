from django.db import models


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=30)
    category_description = models.CharField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)
    date_modified =  models.DateField(auto_now=True)

    def __str__(self):
            return ("{}".format(self.category_title))


class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_title = models.CharField(max_length=30)
    recipe_description = models.CharField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
            return ("{}".format(self.recipe_title))