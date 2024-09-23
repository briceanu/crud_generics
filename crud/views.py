from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework.exceptions import NotFound
 


class Book_All(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    lookup_field = 'book_id'





class BookView(CreateAPIView,ListAPIView,UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field is the field for finding the object you want to update
    lookup_field = 'book_id'
    


class GetOneBook(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """
    if you want to query the book from the url 
    you need to use the lookup_field  
    """
    # lookup_field = 'book_id'

    def get_object(self):
        book_id = self.request.query_params.get('book_id')
        if not book_id:
            raise NotFound(detail='book_id not provided')
        try :
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            raise NotFound(detail=f"book with id {book_id} not found")    


class BookViewDelete(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'


# to be able to remove a book using queryparamaters you have to use the get_object function

    def get_object(self):
        book_id = self.request.query_params.get('book_id')
        if not book_id:
            raise NotFound(detail="book_id query parameter is required")

        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            raise NotFound(detail=f"No book found with id {book_id}")    

