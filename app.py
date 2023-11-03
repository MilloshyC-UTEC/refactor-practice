import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# región,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append( fila)
        return data

    def calcularvotosporcandidato(self, data):
        votosxcandidato = {}
        for fila in data:
            if not fila[4] in votosxcandidato:
                votosxcandidato[fila[4]] = 0
            if fila[5] == '1':
                votosxcandidato[fila[4]] = votosxcandidato[fila[4]] + 1
        return votosxcandidato
    def verificardni(self, data):
        total=0
        for fila in data:
            if len(fila[3])==8:
                total+=1
        return total

    
    def calculaganador(self,data):
        votos = sorted(data.items(), key=lambda x: x[1], reverse=True)
        votos= votos[:2]
        for candidato in votos:
            porcentaje = self.verificardni(data)
            if votos[0][1] > 0.5*porcentaje:
                return [votos[0][0]]
            elif votos[0][1] == 0.5*porcentaje and votos[1][1]== 0.5*porcentaje:
                return [votos[0][0]]
            else:
                return [votos[0][0],votos[1][0]]
            

    


c = CalculaGanador()
data=c.calcularvotosporcandidato(c.leerdatos())
print(c.calculaganador(data))

