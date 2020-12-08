

class ManejaInfo:
    sol_totales = []
    solicitudes = []
    una_linea = []

    def elminar_repetidas(self, solicitud):
        print("")

    def manejador(self, datos):

        solaux = datos.split("\n")



        for unasol in solaux:
            if unasol not in self.solicitudes[][0]:
                self.solicitudes.append(unasol)

            #for solicitud in self.sol_totales:
             #   if solicitud[0] == unasol[0]:
                    #print(solicitud + "   " + unasol)
              #      self.sol_totales.pop(self.sol_totales.index(solicitud))


        print(self.solicitudes)






