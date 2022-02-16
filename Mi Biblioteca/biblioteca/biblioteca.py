#Tiene una lista de usuarios y libros
#import User as us
#import Book as bo

class Biblioteca:

    #my_users:us = []
    #my_books:bo = []
    prestados = []
    #devueltos = []


    def __init__(self, users = [], books = []):
        self.my_users = users
        self.my_books = books
        

    def get_users(self):
        return self.my_users
    def set_users(self, users):
        self.my_users = users

    def add_users(self, user):
        self.my_users.append(user)
    def del_users(self, id):
        for use in self.my_users:
            if(use.dni == id):      
                self.my_users.remove(use)
    def print_users(self):
        print("Users list: "+str(self.my_users))
        

    def get_book(self):
        return self.my_books
    def set_books(self, books):
        self.my_books = books

    def add_books(self, book): 
        self.my_books.append(book)
    def del_books(self, id):
        for boo in self.my_books:
            if(boo.isbn == id):
                self.my_books.remove(boo)
    def print_books(self):
        print("Books list: "+str(self.my_books))
    

    def print_prestados(self):
        print("Libros prestados: "+str(self.prestados))
    #def print_devueltos(self):
        #print("Libros devuletos: "+str(self.devueltos))


    #Añado los libro que han sido prestados a este usuario
    def user_books(self, id_user):
        books_prestamo = [] #Libros que tiene un usuario en prestamo
        for book in self.prestados:
            if(book.user.dni == id_user):
                books_prestamo.append(book.title)
        print("Libros prestados a este usuario: "+str(books_prestamo))
    

    def to_string(self):
        print("Users List: "+self.my_users+" Books List: "+self.my_books)