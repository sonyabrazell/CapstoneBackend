from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Book(models.Model):
    
    ActionAdventure = 'Action/Adventure'
    BioAuto = 'Biography/Autobiography'
    Children = 'Childrens'
    Contemporary = 'Contemporary'
    Fantasy = 'Fantasy'
    GeneralFiction = 'General Fiction'
    HistoricalFiction = 'Historical Fiction'
    History = 'History'
    Horror = 'Horror'
    LiteraryFiction = 'Literary Fiction'
    MysterySuspense = 'Mystery/Suspense'
    Poetry = 'Poetry'
    Reference = 'Reference'
    Romance = 'Romance'
    ScienceFiction = 'Science Fiction'
    SelfHelp = 'SelfHelp'
    TrueCrime = 'TrueCrime'
    
    GenreChoices = [
        (ActionAdventure, 'Action/Adventure'),
        (BioAuto, 'Biography/Autobiography'),
        (Children, 'Childrens'),
        (Contemporary, 'Contemporary'),
        (Fantasy, 'Fantasy'),
        (GeneralFiction, 'General Fiction'),
        (HistoricalFiction, 'Historical Fiction'),
        (History, 'History'),
        (Horror, 'Horror'),
        (LiteraryFiction, 'Literary Fiction'),
        (MysterySuspense, 'Mystery/Suspense'),
        (Poetry, 'Poetry'),
        (Reference, 'Reference'),
        (Romance, 'Romance'),
        (ScienceFiction, 'Science Fiction'),
        (SelfHelp, 'SelfHelp'),
        (TrueCrime, 'TrueCrime'),
    ]
    
    Hardback = 'Hardback'
    Paperback = 'Paperback'
    eBook = 'eBook'
    Audiobook = 'Audiobook'
    
    FormatChoices = [
        (Hardback, 'Hardback'),
        (Paperback, 'Paperback'),
        (eBook, 'eBook'),
        (Audiobook, 'Audiobook'),
    ]
    
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_isbn = models.IntegerField()
    book_cover = models.CharField(max_length=100)
    read_status = models.BooleanField(default=False)
    book_format = models.CharField(max_length=50, max_choices = 1, choices = FormatChoices)
    book_genre = models.CharField(max_length=50, choices =  GenreChoices)
    book_series = models.BooleanField(default=False)
    special_edition = BooleanField(default=False)
    first_edition = BooleanField(default=False)
    signed = BooleanField(default=False)
    
class BookTracker(models.Model):
    book_title = ForeignKey(Book, related_name = 'book_title', on_delete=models.CASCADE)
    book_author = ForeignKey(Book, related_name= 'book_author')
    book_cover = ForeignKey(Book, related_name = 'book_cover')
    date_read = models.DateField()

class NonTradTracker(models.Model):
    work_title = models.CharField(max_length=50)
    work_author = models.CharField(max_length=50)
    word_count = models.IntegerField()
    date_read = models.DateField()
    work_link = models.CharField(max_length=100)

class Wishlist (models.Model):
    book_title = ForeignKey(Book, related_name = 'book_title', on_delete=models.CASCADE)
    book_author = ForeignKey(Book, related_name = 'book_author')
    book_cover = ForeignKey(Book, related_name = 'book_cover')
    
    
