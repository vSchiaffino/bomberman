class Celda():
    """
    Clase que se utiliza para referirse a una porción
    de la pantalla de determinados pixeles, que tiene
    contenidos. Esta separación sirve para generar las colisiones.
    """
    def __init__(self, contenido, fila, columna, ppc):
        self.contenidos = []
        self.contenidos.append(contenido)
        self.fila = fila
        self.columna = columna
        self.ppc = ppc

    def set_em(self, em):
        """
        Función que sirve para que las celdas
        conozcan al Event Manager.
        Devuelve None
        """
        self.em = em
        for contenido in self.contenidos:
            contenido.set_em(em)

    def get_middle_pos(self):
        """
        Función que sirve para obtener la posición central
        de la celda.
        Devuelve una lista de dos int.
        """
        ppc = self.ppc
        return [self.columna*ppc - ppc/2, self.fila*ppc - ppc/2]

    def ser_explotado(self):
        """
        Función que se utiliza para avisar a los contenidos de la celda
        que están siendo explotados. Los contenidos reaccionarán a esto
        según su comportamiento específico.
        Devuelve None
        """
        for contenido in self.contenidos:
            # El contenido le responde que hay que hacer al explotarlo
            # True: Eliminarlo
            # False: Dejarlo
            # Contenido: Eliminarlo y appendear otro contenido
            if contenido == None:
                self.contenidos.remove(contenido)
            else:
                respuesta = contenido.ser_explotado()
            if respuesta != False:
                # Lo saco porque si o si tengo que sacarlo
                self.eliminar_contenido(contenido)
                if respuesta != True:
                    # agrego otro contenido, porque no es ni true ni false
                    self.contenidos.append(respuesta)
                    
    def ser_caminado(self, caminador):
        """
        Función que se utiliza para avisar a los contenidos de la celda
        que están siendo caminados. Los contenidos reaccionarán a esto
        según su comportamiento específico.
        Devuelve None
        """
        # El contenido responde que hay que hacer cuando es caminado
        # True : Eliminarlo
        # False : Dejarlo
        caminador.entraste_a_mi(self)
        for contenido in self.contenidos:
                if contenido.ser_caminado(caminador):
                    self.eliminar_contenido(contenido)

    def agregar_caminador(self, caminador):
        """
        Función que sirve para que la celda agregue al
        caminador cuando este la camine.
        Devuelve None
        """
        if not(caminador in self.contenidos):
            self.contenidos.append(caminador)

    def agregar_contenido(self, contenido):
        """
        Función que sirve para agregar un contenido a los
        contenidos.
        Devuelve None
        """
        self.contenidos.append(contenido)

    def poner_bomba(self, bomba):
        """
        Función que sirve para agregar una bomba a los contenidos.
        Devuelve None
        """
        self.contenidos.append(bomba)

    def puedo_poner_bomba(self):
        """
        Función que sirve para que la celda le pregunte
        a los contenidos si alguno tiene problema con que
        pongan una bomba.
        Devuelve:
            True: si se puede poner bomba
            False: si no se puede
        """
        for contenido in self.contenidos:
            if contenido.sos_bomba(): return True
        return False

    def comprobar_mov(self):
        """
        Función que sirve para que la celda le pregunte
        a sus contenidos si pueden caminar sobre ellos.
        Devuelve:
        True: Puede ser caminada
        False: No puede ser caminada 
        """
        for contenido in self.contenidos:
            if not contenido.comprobar_mov():
                return False
        return True

    def agregar_explosion(self, explosion):
        """
        Función que sirve para agregar una explosión a la
        lista de contenidos.
        Devuelve None
        """
        self.contenidos.append(explosion)

    def get_pos(self):
        """
        Función que sirve para obtener la posición del extremo
        superior izquierdo de la celda.
        Devuelve: una lista de dos ints.
        """
        pos_x = (self.columna - 1) * self.ppc
        pos_y = (self.fila - 1) * self.ppc
        return [pos_x, pos_y]

    def get_ruta_contenido(self):
        """
        Función que sirve para generar una lista de todas las keys
        de los contenidos para que la vista las cargue.
        Devuelve: Una lista de strings.
        """
        rutasContenidos = []
        for contenido in self.contenidos:
            if contenido == None:
                self.contenidos.remove(contenido)
            else:
                rutasContenidos.append(contenido.get_ruta())   
        return rutasContenidos
    
    def personaje_entro_a_celda(self):
        """
        Función que sirve para notificar a los contenidos
        que un personaje entro a la celda.
        Devuelve None.
        """
        for contenido in self.contenidos:
            contenido.personaje_entro_a_celda()

    def eliminar_contenido(self, contenido):
        """
        Función que sirve para eliminar un contenido de la lista
        de contenidos de la celda.
        Devuelve None.
        """
        if contenido in self.contenidos:
            self.contenidos.remove(contenido)

    def sacar_bomba(self, bomba):
        """
        Saca una bomba de los contenidos.
        Devuelve none.
        """
        self.contenidos.remove(bomba)