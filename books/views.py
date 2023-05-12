from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#this is how does it work
# class BookListApiView(APIView):
#
#     def get(self, request):
#         books = Book.objects.all()
#         serialized_data = BookSerializer(books, many=True).data
#         data = {
#             "status" : f"Returned {len(books)} books",
#             "books" : serialized_data
#         }
#
#         return Response(data)

class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookCreateApiView(APIView):
#
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "status": "Book saved to the database",
#                 "books": data
#             }
#             else:
#                 return Response(
#                     {"status": False,
#                      "message": "Serializer is not valid", status=status.HTTP_400_BAD_REQUEST}
#                 )


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDetailApiView(APIView):
#
#     def get(self, request, pk):
#         try:
#             book = BookListApiView.objects.get(id=pk)
#             serialized_data = BookSerializer(books).data
#
#             data = {
#                 'status': 'Succesfull!',
#                 'book': serialized_data
#             }
#
#             return Response(data, status=status.HTTP_200_OK)
#         except Exception:
#             return Response(
#                 {'status': "False",
#                  'message': 'Book does not exists'}, status=status.HTTP_404_NOT_FOUND
#             )

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDeleteApiView(APIView):
#
#     def delete(self, request, pk):
#         try:
#             book = Book.objects.all()
#             book.delete()
#             return Response({
#                 "status": True,
#                 "message": "Successfully deleted"
#             }, status=status.HTTP_200_OK)
#         except Exception:
#             return Response({
#                 "status": False,
#                 "message": "Book isn't found"
#             }, status=status.HTTP_400_BAD_REQUEST)

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookUpdateApiView(APIView):
#
#     def put(self, request, pk):
#         book = get_object_or_404(Book.objets.all(), id=pk)
#         data = request.data
#         serializer = BookSerializer(instance=book, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             book_saved = serializer.save()
#
#         return Response({
#             "status": True,
#             "message": f"Book {book_saved} saved successfully!"
#         })



class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



#function based view
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)