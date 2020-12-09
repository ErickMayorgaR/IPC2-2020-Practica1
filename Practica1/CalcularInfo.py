import json

class ManejaInfo:
    carreras = []

    solicitudes = []
    una_linea = []
    diccionarios = []

    def almacenardatosJSON(self):
        with open ('C:/Users/emayo/OneDrive/Desktop/Practica1/IPC2/Practica1/Resultados.json','w', encoding= 'utf-8') as file:
            json.dump(self.diccionarios, file, indent = 4)
            file.close()

    def creadiccionarioscarrera(self, nombre):
        nocandidatos = 0
        edades = 0
        pretension = 0
        datos = {}
        datos[nombre] = []
        di_candidatos = {'Candidatos':None, 'Edad Promedio':None, 'Pretension Salarial':None}

        for candidato in self.solicitudes:
            if candidato[4] == nombre:
                nocandidatos += 1
                edades += float(candidato[3])
                pretension += float(candidato[5])

        di_candidatos['Candidatos'] = nocandidatos
        di_candidatos['Edad Promedio'] = (edades/nocandidatos)
        di_candidatos['Pretension Salarial'] = pretension/nocandidatos
        datos[nombre].append(di_candidatos)

        self.diccionarios.append(datos)

    def separarcarreras(self):
        for persona in self.solicitudes:
            if persona[4] not in self.carreras:
                self.carreras.append(persona[4])

        for carrera in self.carreras:
            self.creadiccionarioscarrera(carrera)



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









