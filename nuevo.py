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
        
        self.piezax = input("Seleccine la fila: ")
        print("Ha seleccionado la fila: ",self.piezax)
        
        self.piezay = input("Seleccine la columna: ")
        print("Ha seleccionado la columna: ",self.piezay) 

        #Imprimir La Pieza seleccionada por el usuario
        #si existe la pieza 
        cdadepieza =(self.tablero[int(self.piezax)][int(self.piezay)])
        if cdadepieza == "   ":
            print ("Pieza no Existente")
            self.pedirpieza()

        elif cdadepieza != "   ":
            print (cdadepieza) 
        

        self.validar = input("Si quiere continuar presione S y si no presione N (solo MAYUSCULAS): ")
        if self.validar == "N":
            tablero1.pedirpieza()

    #-----------------------------------------#

    """Hacer una funcion DEF con el nombre moverpieza en el cual contenga una funcion que
    le diga al usuario cuales seran las coordenadas X y coordenadas Y donde quiere mover la pieza """
    def moverpieza(self):
        self.piezacorx=input("seleccione una fila para mover su pieza")
        print("la fila seleccionada es:",self.piezacorx)

        self.piezacory=input("seleccione una columna para mover su pieza")
        print("la columna seleccionada es:",self.piezacory)


    #-----------------------------------------#

    """def verificarpieza(self):
        for fila in self.tablero:
            for elemento in fila:
                if elemento == self.pieza:
                    print(elemento)
                    print("Existe la pieza")
                    return True"""
        
    """def pos(self):
        for i in range(0,8):
            self.indice = self.tablero[i].index(self.pieza)
            print(self.indice)"""
        
        

tablero1 = Tablero()

tablero1.mostrartablero()
tablero1.pedirpieza()
#retorno = tablero1.verificarpieza()
#tablero1.pos()
