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
        
        self.piezax = input("Seleccine la casilla del eje x: ")
        print("Ha seleccionado ",self.piezax)
        
        self.piezay = input("Seleccine la casilla del eje y: ")
        print("Ha seleccionado ",self.piezay) 
        
        self.validar = input("Si quiere continuar presione S y si no presione N: ")
        if self.validar == "N":
            tablero1.pedirpieza()

    def verificarpieza(self):
        for fila in self.tablero:
            for elemento in fila:
                if elemento == self.pieza:
                    print(elemento)
                    print("Existe la pieza")
                    return True
        
    """def pos(self):
        for i in range(0,8):
            self.indice = self.tablero[i].index(self.pieza)
            print(self.indice)"""
        
        

tablero1 = Tablero()

tablero1.mostrartablero()
tablero1.pedirpieza()
retorno = tablero1.verificarpieza()
#tablero1.pos()
