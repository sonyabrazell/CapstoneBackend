from django.db import models
from django.db.models.fields import BooleanField
from authentication.models import User

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
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_isbn = models.IntegerField()
    book_cover = models.CharField(max_length=100)
    read_status = models.BooleanField(default=False)
    book_format = models.CharField(max_length=50, choices = FormatChoices)
    book_genre = models.CharField(max_length=50, choices =  GenreChoices)
    book_series = models.BooleanField(default=False)
    special_edition = BooleanField(default=False)
    first_edition = BooleanField(default=False)
    signed = BooleanField(default=False)
    
    class Meta:
        ordering = ['book_author']
        
    def __str__(self):
        return f'book_title: {self.book_title}, book_author: {self.book_author}, book_cover: {self.book_cover}, book_format: {self.book_format}, book_genre: {self.book_genre}'
    
class BookTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_date_read = models.DateField()
    
    class Meta:
        ordering = ['book_date_read']
        

class NonTradTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_title = models.CharField(max_length=50)
    work_author = models.CharField(max_length=50)
    word_count = models.IntegerField()
    work_date_read = models.DateField()
    work_link = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['work_date_read']
        
    def __str__(self):
        return f'work_title: {self.work_title}, work_author: {self.work_author}, work_link: {self.work_link}'

class Wishlist (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['wishlist_book']
    
    
