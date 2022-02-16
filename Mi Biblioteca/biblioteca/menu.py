#Opciones Alta de socio, Baja de socio, Alta de libro, Baja de libro, 
#Prestar libro, Devolver libro
#Consultar libros, Consultar prestamos, Consultar usuarios y salir.

#1º importo los módulos que necesite
import biblioteca as my_biblioteca
import book as my_book
import user as my_user

#2º Creo un objeto de cada módulo
biblioteca = my_biblioteca.Biblioteca()
#user = my_user.User()
#book = my_book.Book()

#3º Hacer una lista de cada elemento necesario
#user_list = []
#book_list = []

#4º Método para dar de alta un usuario, creandolo y meterlo en la biblioteca
def new_user():
    dni = input("Introduzca el dni: ")
    name = input("Introduzca el nombre: ")
    email = input("Introduzca el email: ")
    phone = int(input("Introduzca el número de teléfono: "))
    address = input("Introduzca la dirección: ")
    user = my_user.User(dni, name, email, phone, address)
    print("Dando de alta al usuario: ")
    user.print_user()
    #user_list.append(user)
    biblioteca.add_users(user)

#5º Método para dar de baja a un usuario, eliminadolo de la biblioteca
def del_user(id):
    biblioteca.del_users(id)

#6º Método para dar de alta un libro, creandolo y meterlo en la biblioteca
def new_book():
    isbn = input("Introduzca el isbn: ")
    title = input("Introduzca el título: ")
    author = input("Introduzca el autor: ")
    gender = input("Introduzca el género: ")
    cover = input("Introduzca la portada: ")
    synopsis = input("Introduzca sinopsis: ")
    copies = input("Introduzca número de copias: ")
    date = input("Introduzca una fecha: ")
    book = my_book.Book(isbn, title, author, gender,
                        cover, synopsis, copies, date)
    print("Dando de alta el libro: "+str(book))
    #book_list.add(book)
    biblioteca.add_books(book)

#7º Método para dar de baja a un libro, eliminadolo de la biblioteca
def del_book(id):
    biblioteca.del_books(id)

#8º Método para realizar un prestamo
def prestar(id_user, id_book):
    user = my_user.User()
    for usbo in biblioteca.my_users:
        if(usbo.dni == id_user):
            #usbo.set_book = book
            user = usbo
    for pres in biblioteca.my_books:
        if(pres.isbn == id_book):
            pres.prestado = True
            pres.user = user    #Añado el usuario al libro
            biblioteca.prestados.append(pres)

#9º Método para realizar una devolucion
def devolver(id):
    for pres in biblioteca.my_books:
        if(pres.isbn == id):
            pres.prestado = False
            biblioteca.prestados.remove(pres)

#10º Método para consultar libros, devolviendo la lista de libros
def print_books():
    #print("My books list: "+book_list)
    biblioteca.print_books()

#11º Método para consultar prestamos, devolviendo la lista de prestamos
def print_prestamos():
    biblioteca.print_prestados()

#12º Método para consultar usuarios, devolviendo la lista de usuarios
def print_users():
    print("My Users list: ")  # +user_list)
    biblioteca.print_users()
    #print(user_list)

#13º Se crea un menu con las diferentes opciones y sus métodos correspondientes
def my_menu():
    salir = True
    while(salir):
        option = input("""
        Bienvenidos a Adrian's BookStore
        Indique su consulta
        1  Alta de socio
        2  Baja de socio
        3  Alta de libro
        4  Baja de libro
        5  Prestar libro
        6  Devolver libro
        7  Consultar libros
        8  Consultar prestamos 
        9  Consultar usuarios
        10 Salir
        \n \t \t \t \t""")
        if(option == "0"):  # Esta es la opción oculta (secreta) que permite ver los libros de un usuario
            biblioteca.user_books(
                input("Introduzca el id del usuario del que saber sus libros: "))
        if(option == "1"):
            new_user()
        if(option == "2"):
            del_user(input("Introduzca el id del usuario a eliminar: "))
        if(option == "3"):
            new_book()
        if(option == "4"):
            del_book(input("Introduzca el isbn del libro a eliminar: "))
        if(option == "5"):
            prestar(input("Introduzca el id del usuario que lo va a tener: "),
                    input("Introduzca el isbn del libro a prestar:  "))
        if(option == "6"):
            devolver(input("Introduzca el isbn del libro a devolver: "))
        if(option == "7"):
            print_books()
        if(option == "8"):
            print_prestamos()
        if(option == "9"):
            print_users()
        if(option == "10"):
            salir = False


#14º Si la clase que se ejecuta es esta se ejecutará el método my_menu
if __name__ == "__main__":
    my_menu()
