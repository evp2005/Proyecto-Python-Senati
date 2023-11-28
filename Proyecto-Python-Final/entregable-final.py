import json
import os
from datetime import datetime


global data, path, hora_actual, fecha_actual

path = os.getcwd()
print(path,"/data.json")

# Obtener la fecha actual
fecha_actual = datetime.now().date()

# Obtener la hora actual
hora_actual = datetime.now().time()

class Ticket:
    def __init__(self):
        
        self.data:dict = {
                "id": None,
                "nombre": None,
                "precio": None,
                "categoria": None,
                "stock": None
            }


    def USD_to_PEN_conversion(self, amount:float) -> float:
        PEN:float = 3.70

        return amount * PEN

    def get_data(self):
        with open(f"{path}/data.json", "r") as f:
            data = json.load(f)
        return data


    def request_data(self):
        # INICIAMOS EL SEGUNDO BUCLE
        global aux
        aux = False
        while not aux:
            # PEDIMOS DATOS
            cliente:str = input("Ingrese su nombre: ")
            payment_method:str = input("Metodo de Pago: ")
            DNI:int = input("Ingrese su DNI: ")
            product:int = input("Ingrese el producto: ")
            qty:int = int(input("Cuantas unidades se va a llevar: "))

            # SI EXISTE EL PRODUCTO
            # TENEMOS QUE TRAER EL METODO get_data() de la clase Ticket


            # affirmation = [i["nombre"]==product for i in self.tk.get_data() ]
            # print(affirmation)



            for i in self.get_data():
                if i["nombre"] == product:
                    self.data["id"] = i["id"]
                    self.data["nombre"] = i["nombre"]
                    self.data["precio"] = i["precio"]
                    self.data["categoria"] = i["categoria"]
                    self.data["stock"] = i["stock"]

            # cf = "El producto existe" if True in affirmation else break

            if self.data["nombre"] == product and self.data["stock"] >= qty:
                # TENGO QUE HACER LA CONVERSION Y LLEVAR A CABO LA OPERACION
                UxP = self.USD_to_PEN_conversion(self.data["precio"])
                # MULTIPLICO LA CANTIDAD CON EL PRECIO DEL PRODUCTO EN SOLES
                total_price_of_the_product = qty * UxP
                # HALLO EL IGV CON LA FORMULA
                IGV = (total_price_of_the_product / 100) * 18
                # SACO LA SUMA TOTAL
                total = total_price_of_the_product + IGV

                question = input("Desea generar una boleta yes/no: ").lower()

                if question == "yes":
                    print("""
                -------------------------------------
                :::::::::Ferretería Leonardo:::::::::
                ::---------------------------------::
                :: Datos                           ::
                ::---------------------------------::
                :: Fecha: %s               ::
                :: Hora : %s          ::
                ::---------------------------------::
                :: Cajero        : %s         ::
                :: Cliente       : %s        ::
                :: DNI           : %s       ::
                :: Metodo de Pago: %s         ::
                ::---------------------------------::
                :: Operaciones                     ::
                ::---------------------------------::
                :: Precio del Producto: %s      ::
                :: IGV                : %s     ::
                :: Total              : %s    ::
                -------------------------------------
                    """ %(fecha_actual, hora_actual, "unknown", cliente, DNI, payment_method, self.data["precio"], str(round(IGV, 2)), str(round(total, 2))))
                    print("Gracias por su compra")
                    
                    exit()
                elif question == "no":
                    
                    exit()
                else:
                    print("Selecione una opcion valida")
                    
                    exit()
                exit()
            else:
                break


    def generate_ticket(self):
        while not False:
            print("""
                    ::::::::::::::::::::::::::::::::::::::::::
                    :: No Tiene Seleccionado Algun Producto ::
                    ::::::::::::::::::::::::::::::::::::::::::
                """)
            option = input("Desea Seleccionar algun product yes/no: ").lower()

            if option == "yes":
                self.request_data()
            elif option == "no":
                break
            else:
                break
                
    def search_product(self):
        while not False:
            search = input("Buscar un Producto: ")

            for i in self.get_data():
                if i["nombre"] == search:
                    self.data["id"] = i["id"]
                    self.data["nombre"] = i["nombre"]
                    self.data["precio"] = i["precio"]
                    self.data["categoria"] = i["categoria"]
                    self.data["stock"] = i["stock"]

            if search in self.data["nombre"]:
                print("""
                      :::::::::::::::::::::::::::
                      ::: Producto Encontrado :::
                      :::::::::::::::::::::::::::

               ||----------------------------------------||
               ||ID |Nombre  |Precio |Categoria   |Stock ||
               ||----------------------------------------||
               ||%s  |%s|%s  |%s|%s    ||
               ||----------------------------------------||
                      """ %(self.data["id"], self.data["nombre"], self.data["precio"], self.data["categoria"], self.data["stock"]))
            # print("""
            #         ::::::::::::::::::::::::::::
            #         ::    🔍 Search Products    ::
            #         ::::::::::::::::::::::::::::
                    
            #         ub

            #         ||-------------------------------------||
            #         ||ID |Nombre |Precio |Categoria |Stock ||
            #         ||-------------------------------------||
            #         ||%s |%s     |%s     |%s        |%s    ||
            #         ||-------------------------------------||
            #       """ %())
            else:
                print("""
                      :::::::::::::::::::::::::::
                      ::: Producto No Encontrado :::
                      :::::::::::::::::::::::::::
                """)

            
            ex = input("Desea seguir buscando yes/no: ").lower()
            if ex == "yes":
                pass
            else:
                exit()
                 
            
                
    def see_product_catalog(self):
        
        while not False:

            # for i in self.get_data():

            #     print("""
            #    ||----------------------------------------||
            #    ||ID |Nombre  |Precio |Categoria   |Stock ||
            #    ||----------------------------------------||
            #    ||%s  |%s|%s  |%s|%s    ||
            #    ||----------------------------------------||
            #           """ %(i["id"], i["nombre"], i["precio"], i["categoria"], i["stock"]))
            print("""
               ||----------------------------------------------||
               ||ID  |Nombre       |Precio |Categoria   |Stock ||
               ||----------------------------------------------||
               ||%s  |%s      |%s  |%s|%s    ||
               ||----------------------------------------------||
               ||%s  |%s     |%s   |%s  |%s   ||
               ||----------------------------------------------||
               ||%s  |%s|%s   |%s|%s    ||
               ||----------------------------------------------||
               ||%s  |%s       |%s  |%s    |%s    ||
               ||----------------------------------------------||
               ||%s  |%s|%s   |%s|%s    ||
               ||----------------------------------------------||
                """ %(self.get_data()[0]["id"], self.get_data()[0]["nombre"], self.get_data()[0]["precio"], self.get_data()[0]["categoria"], self.get_data()[0]["stock"], self.get_data()[1]["id"], self.get_data()[1]["nombre"], self.get_data()[1]["precio"], self.get_data()[1]["categoria"], self.get_data()[1]["stock"], self.get_data()[2]["id"], self.get_data()[2]["nombre"], self.get_data()[2]["precio"], self.get_data()[2]["categoria"], self.get_data()[2]["stock"], self.get_data()[3]["id"], self.get_data()[3]["nombre"], self.get_data()[3]["precio"], self.get_data()[3]["categoria"], self.get_data()[3]["stock"],self.get_data()[4]["id"], self.get_data()[4]["nombre"], self.get_data()[4]["precio"], self.get_data()[4]["categoria"], self.get_data()[4]["stock"]))
            # print(self.get_data()[0]["nombre"])

            exit()

class Cliente:
    def __init__(self) -> None:
        self.tk = Ticket()

    def option_menu(self):
        print("""
              ||----------------------------||
              ||OPCIONES DEL MENU           ||
              ||----------------------------||
              ||1.-Ingresar Datos           ||
              ||----------------------------||
              ||2.-Generar un Ticket        ||
              ||----------------------------||
              ||3.-Buscar Producto          ||
              ||----------------------------||
              ||4.-Ver Catalogo de Productos||
              ||----------------------------||
              ||5.-Salir                    ||
              ||----------------------------||
              """)
        
        try:
            option:int = int(input("Ingrese el numero de su opcion requeridad: "))
        except ZeroDivisionError as e:
            print("No se aceptan ceros")

        while not False:
            if option == 1:
                self.tk.request_data()
                
            elif option == 2:
                self.tk.generate_ticket()
            elif option == 3:
                self.tk.search_product()
            elif option == 4:
                self.tk.see_product_catalog()
            elif option == 5:
                break
                exit()
            else:
                print("No existe la opcion", option)
        
    def run(self):
        self.option_menu()

if __name__ == "__main__":
    # tk = Ticket
    # print(tk.get_data())
    cl = Cliente()
    cl.run()
    # cl.USD_to_PEN_conversion(1000)
    