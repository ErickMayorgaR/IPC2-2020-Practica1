

class ManejaInfo:
    carreras = []
    sol_totales = []
    solicitudes = []
    una_linea = []

    def separarcarreras(self):
        for persona in self.solicitudes:
            if persona[4] not in self.carreras:
                self.carreras.append(persona[4])
        print(self.carreras)

        




    def manejador(self, datos):
        solaux = []
        separadorsalto = datos.split("\n")
        repetido = False

        for solicitud in separadorsalto:
            unasolaux = solicitud.split(",")
            if unasolaux[0].upper() != "ID":
                solaux.append(unasolaux)

        for unasol in solaux:
            for i in range(len(self.solicitudes)):
                if unasol[0] == self.solicitudes[i][0]:
                    repetido = True

            if repetido == False:
                self.solicitudes.append(unasol)
            elif repetido == True:
                repetido = False
                continue


        print(self.solicitudes)






