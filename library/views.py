from django.http import JsonResponse
from .models import Book

def book_list_view(request):
    """
    Fetches and returns a JSON response of all books in the library.
    """
    try:
        books = Book.objects.all().values("title", "author", "published_date", "isbn", "available_copies")

        if not books:
            return JsonResponse({"message": "No books found"}, status=404)

        return JsonResponse(list(books), safe=False)

    except Exception as e:
        return JsonResponse({"error": "Something went wrong", "details": str(e)}, status=500)
