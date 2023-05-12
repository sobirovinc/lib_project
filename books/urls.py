from django.urls import path
from .views import BookListApiView, BookDetailView, BookDeleteApiView, BookUpdateApiView, BookCreateApiView, \
    BookListCreateApiView, BookUpdateDeleteApiView, BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('', BookListApiView.as_view(), name='booklistapi'),
    # path('booklistcreate', BookListCreateApiView.as_view()),
    # path('bookud/<int:pk>', BookUpdateDeleteApiView.as_view(), name='book_upd_dlt'),
    # path('books/create', BookCreateApiView.as_view(), name='create'),
    # path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    # path('books/<int:pk>/update', BookUpdateApiView.as_view(), name='book_update'),
    # path('books/<int:pk>/delete', BookDeleteApiView.as_view(), name='book_delete'),


]

urlpatterns = urlpatterns + router.urls

