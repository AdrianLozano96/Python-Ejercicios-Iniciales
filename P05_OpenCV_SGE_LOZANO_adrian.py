#Para poder utilizar cv2 instalar antes opencv con pip install opencv-python
import cv2

camara = cv2.VideoCapture(0)

salir = False
while(salir == False):

    grabar, filtro = camara.read()
    wb = cv2.cvtColor(filtro, cv2.COLOR_RGB2GRAY)
    wbr = cv2.cvtColor(filtro, cv2.COLOR_BGR2XYZ)
    filtro1 = cv2.imshow("Imagen Blanco y Negro", wb)
    filtro2 = cv2.imshow("Imagen Blanco y Negro con Rojo", wbr)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        salir = True

camara.release()
cv2.destroyAllWindows()
