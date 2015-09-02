from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return "Autor: " + self.name + "\n" + "Edad: " + str(self.age)


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

    def __str__(self):
        return "Editorial: " + self.name + "\n Número de premios: " + str(self.num_awards)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)  # we only need to write this sentence in one place.
    publisher = models.ForeignKey(Publisher)  # one to one relationship.
    # publisher = models.OneToOneField(Publisher)  # it's equivalent to the one before, but, when you will
    # be adding the new element, it won't let you add it until you create the publisher object and you associated.
    pubdate = models.DateField()

    def __str__(self):
        return "Nombre libro: " + self.name + " \n  " + "Editoriales: " + str(
            self.publisher) + "Autores: "  # + self.authors.all()

    def my_authors(self):
        for author in self.authors.all():
            print(author)


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
