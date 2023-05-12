from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # if not title.isalpha():
        #     raise ValidationError({
        #         "status": False,
        #         "message": "Book name can't contain numbers"
        #     })


        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                "status": False,
                "message": "This book exists in database already!"
            })

        return data

    def validate_price(self, price):
        if price<=0 or price>999999:
            raise ValidationError({
                "status": False,
                "message": "Invalid price"
            })
        return price

    def validate_isbn(self, isbn):
        flag=True
        for i in isbn:
            if not i.isnumeric() and i!="-":
                flag=False

        if flag==False:
            raise ValidationError({
                "status": False,
                "message": "isbn can't contain letters"
            })
        return isbn
