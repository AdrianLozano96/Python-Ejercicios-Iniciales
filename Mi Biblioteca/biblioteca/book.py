#Tienen ISBN, titulo, autor, genero, portada, sinopsis, ejemplares, 
# usuario que ha recibido el libro en prestamo y fecha de prestamo.
import user as u
class Book:
    
    def __init__(self, isbn="", title="", author="", gender="", cover="", synopsis="", copies=0, 
    date=0):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.gender = gender
        self.cover = cover
        self.synopsis = synopsis
        self.copies = copies
        self.user = u.User() #Me interesa saber del libro el usuario que lo tiene
        self.date = date
        self.prestado = False    #Booleano para saber si el libro es prestado o ha sido devuleto 1º no esta prestado
    
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, isbn):
        self.isbn = isbn
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    def get_gender(self):
        return self.gender
    def set_gender(self, gender):
        self.gender = gender
    def get_cover(self):
        return self.cover
    def set_cover(self, cover):
        self.cover = cover
    def get_synopsis(self):
        return self.synopsis
    def set_synopsis(self, synopsis):
        self.synopsis = synopsis
    def get_copies(self):
        return self.copies
    def set_copies(self, copies):
        self.copies = copies
    def get_user(self):
        return self.user
    def set_user(self, user):
        self.user = user
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    def get_prestado(self):
        return self.prestado
    def set_prestado(self, prestado):
        self.prestado = prestado

    def print_book(self):
        print("Libro -> "+ "I.S.B.N.: "+self.isbn+" Title: "+self.title+" Author: "+self.author+" Gender: "+self.gender+
        " Cover: "+self.cover+" Synopsis: "+self.synopsis+" Copies: "+str(self.copies)+
        " User: "+self.user.dni+" "+self.user.name+
              " Date: "+str(self.date)+" El libro esta prestado? "+str(self.prestado)+"\n")
    
    def __repr__(self):
        return str("Libro -> " + "I.S.B.N.: "+self.isbn+" Title: "+self.title+" Author: "+self.author+" Gender: "+self.gender +
                   " Cover: "+self.cover+" Synopsis: "+self.synopsis+" Copies: "+str(self.copies)+
                   " User: dni: "+self.user.dni+" name: "+self.user.name +
                   " Date: "+str(self.date)+" El libro esta prestado? "+str(self.prestado)+"\n")
                   