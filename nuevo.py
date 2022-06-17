class Tablero():
    def __init__(self):
        self.tablero = [["t_1" , "c_1" , "a_1" , "q_1" , "k_1" , "a_2" , "c_2" , "t_2"],
                        ["p_1" , "p_2" , "p_3" , "p_4" , "p_5" , "p_6" , "p_7" , "p_8"],
                        ["   " , "   " , "   " , "   " , "   " , "   " , "   " , "   "],
                        ["   " , "   " , "   " , "   " , "   " , "   " , "   " , "   "],
                        ["   " , "   " , "   " , "   " , "   " , "   " , "   " , "   "],
                        ["   " , "   " , "   " , "   " , "   " , "   " , "   " , "   "],
                        ["P_1" , "P_2" , "P_3" , "P_4" , "P_5" , "P_6" , "P_7" , "P_8"],
                        ["T_1" , "C_1" , "A_1" , "Q_1" , "K_1" , "A_2" , "C_2" , "T_2"]]

    def mostrartablero(self):
        for i in self.tablero:
            print(i)

    def pedirpieza(self):
        print("""Piezas:
        P_1, P_5, T_1, A_1
        P_2, P_6, T_2, A_2
        P_3, P_7, C_1, Q_1
        p_4, P_8, C_2, K_1""")
        
        #Pedir coordenadas para seleccionar la pieza
        self.piezax = input("Seleccine la fila: ")
        print("Ha seleccionado la fila: ",self.piezax)
        
        self.piezay = input("Seleccine la columna: ")
        print("Ha seleccionado la columna: ",self.piezay) 

        #Imprimir La Pieza seleccionada por el usuario
        #si existe la pieza 
        self.cdadepieza =(self.tablero[int(self.piezax)][int(self.piezay)])
        if self.cdadepieza == "   ":
            print ("Pieza no Existente")
            self.pedirpieza()

        elif self.cdadepieza != "   ":
            print (self.cdadepieza) 
            self.moverpieza()
        
        #Funcion para saber si el usuario quiere continuar o no
        self.validar = input("Si quiere continuar presione S y si no presione N (solo MAYUSCULAS): ")
        if self.validar == "N":
            tablero1.pedirpieza()


    def moverpieza(self):
        #Pedir coordenadas para colocar la pieza
        self.piezacorx=int(input("seleccione una fila para mover su pieza "))
        print("la fila seleccionada es:",self.piezacorx)

        self.piezacory=int(input("seleccione una columna para mover su pieza "))
        print("la columna seleccionada es:",self.piezacory)

        #Funcion para mover la pieza

        self.tablero [int(self.piezax)] [int(self.piezay)] = "   " 

        self.tablero [self.piezacorx] [self.piezacory] = self.cdadepieza

        self.validar1 = input("Si quiere continuar presione S y si no presione N (solo MAYUSCULAS): ")

        #Funcion para saber si el usuario quiere continuar o no
        if self.validar1 == "N":

            self.moverpieza()
        elif self.validar1 !="N":

         for i in self.tablero:
            print(i)
    #---------------------------------------------------------#
    def random(self):

        self.xrandom= random.randrange(0,8)
        self.yrandom= random.randrange(0,8)
        self.movimientox= random.randrange(0,8)
        self.movimientoy= random.randrange(0,8)
    #----------------------------------------------------------#

tablero1 = Tablero()

tablero1.mostrartablero()
tablero1.pedirpieza()
