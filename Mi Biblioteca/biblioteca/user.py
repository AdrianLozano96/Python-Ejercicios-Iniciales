#Tienen DNI, nombre, correo electrónico, teléfono, domicilio, lista de libros en prestamo
#import Book as book
class User:

    def __init__(self, dni="", name="", email="", phone=0, address=""):
        self.__dni = dni
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address
        #self.books = book.Book() #Lo asocio solo en libro para evitar problemas
        #Para saber los libros en prestamo que tiene este usuario se empezo ha realizar un método en esta clase,
        #pero se decidio hacerlo mejor en la clase de Biblioteca


    #Getters con decoradores
    @property
    def dni(self):
        return self.__dni
    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    #Getters clasicos
    def get_phone(self):
        return self.__phone
    def get_address(self):
        return self.__address
    #def get_books(self):
    #    return self.books
    
    #Setters con decoradores
    @dni.setter
    def dni(self,d):
        self.__dni = d
    @name.setter
    def name(self,name):
        self.__name = name
    @email.setter
    def email(self, email):
        self.__email = email
    #Setters clasicos
    def set_phone(self, phone):
        self.__phone = phone
    def set_address(self, address):
        self.__address = address
    #def set_books(self, books):
    #    self.books.append(books)
    
    #ToString
    def print_user(self):
        print("Usuario: "+"D.N.I.: "+self.__dni+" Name: "+self.__name+" Email: "+self.__email+" Phone: "+str(self.__phone)+
        " Address: "+self.__address
        #+ " Book: "+self.books.isbn()+" "+self.books.title()
              + "\n")
    #ToString Verdadero
    def __repr__(self):
        return str("User: "+"D.N.I.: "+self.__dni+" Name: "+self.__name+" Email: "+self.__email+" Phone: "+str(self.__phone) +
                   " Address: "+self.__address 
                   #+ " Book: "+self.books.isbn()+" "+self.books.title()
                   +"\n")
                   
