import math #Biblioteca para cálculos matemáticos
from colorama import init, Fore #Biblioteca para adicionar cores ao programa

#######################################################################

#SuperClasse Polygon

class Polygon:
    #Construtor
    def __init__(self):
        pass
    
    """
    Método responsável por capturar os inputs do usuário.
    Este método também valida o tipo de dado de input.
    A mensagem do parâmetro é passada por argumento nas classes filhas.
    """
    def get_input(self, message):
        while True:
            try:
                value = float(input(message))
                if value <= 0:
                    print(Fore.RED + "O valor deve ser positivo.")
                else:
                    return value
            except ValueError:
                print(Fore.RED + "Por favor, insira um número válido.")

    """
    Este método recebe uma mensagem (vinda por argumento no método main) e concatena com o resultado obtido 
    dos métodos das classes filhas
    """
    def display_result(self, result_message, result):
        print(Fore.CYAN + result_message, result)

#Métodos a serem implementados nas classes filhas
        
    def calcular_area(self):
        raise NotImplementedError("Método não implementado na classe filha")
            
    def calcular_volume(self):
        raise NotImplementedError("Método não implementado na classe filha")   
    
################################################################################################

#Classes FILHAS:

"""
    As classes filhas implementam os métodos calcular_area e calcular_volume.
    Obtém os inputs através do método get_input vindo da superclasse.

"""
class Quadrilatero(Polygon):
    def calcular_area(self):
        altura = self.get_input(Fore.YELLOW + "Digite a altura do quadrilátero: ")
        comprimento = self.get_input("Digite o comprimento do quadrilátero: ")
        return altura * comprimento
        
        
class Triangulo(Polygon):
    def calcular_area(self):
        altura = self.get_input(Fore.YELLOW + "Digite a altura do triângulo: ")
        comprimento = self.get_input("Digite o comprimento da base do triângulo: ")
        return (altura * comprimento) / 2
        
        
class Circulo(Polygon):
    
    def calcular_area(self):
        raio = self.get_input(Fore.YELLOW + "Digite o raio do círculo: ")
        return raio*raio*math.pi
        
        
class Pentagono(Polygon):
    
    def calcular_area(self):
        altura = self.get_input(Fore.YELLOW + "Digite a altura do pentagono: ")
        comprimento = self.get_input("Digite o comprimento da base do pentagono: ")
        return 5*comprimento*altura
        
class Hexagono(Polygon):
    
    def calcular_area(self):
        comprimento = self.get_input(Fore.YELLOW + "Digite o comprimento do lado do hexágono: ")
        return (3*math.sqrt(3)*math.pow(comprimento,2))/2
        

class Paralelepipedo(Polygon):
    
    def calcular_volume(self):
        comprimento = self.get_input(Fore.YELLOW + "Digite o comprimento do paralelepípedo: ")
        altura = self.get_input("Digite a altura do paralelepípedo: ")
        largura = self.get_input("Digite a largura do paralelepípedo: ")
        return comprimento * altura * largura

class Piramide(Polygon):
    
    def calcular_volume(self):
        altura = self.get_input(Fore.YELLOW + "Digite a altura da pirâmide: ")
        comprimento = self.get_input("Digite o comprimento da base da pirâmide: ")
        largura = self.get_input("Digite a largura da base da pirâmide: ")
        return (1/3) * (comprimento * largura) * altura

class Cilindro(Polygon):
    
    def calcular_volume(self):
        raio = self.get_input(Fore.YELLOW + "Digite o raio do cilindro: ")
        altura = self.get_input("Digite a altura do cilindro: ")
        return math.pi * math.pow(raio,2) * altura


class Cone(Polygon):
    
    def calcular_volume(self):
        raio = self.get_input(Fore.YELLOW + "Digite o raio do cone: ")
        altura = self.get_input("Digite a altura do cone: ")
        return ((1/3) * math.pi) * math.pow(raio,2) * altura


class Esfera(Polygon):
    
    def calcular_volume(self):
        raio = self.get_input(Fore.YELLOW + "Digite o raio da esfera: ")
        return ((4/3) * math.pi) * math.pow(raio,3)
    
##############################################################################

#Método MENU 

"""
Obtém o input para escolha do polígono
"""
def menu():
    
    print(Fore.YELLOW + "Escolha um polígono:\n")
    print(Fore. RESET + "1. Quadrilátero")
    print("2. Triângulo")
    print("3. Círculo")
    print("4. Pentágono")
    print("5. Hexágono")
    print("6. Paralelepípedo")
    print("7. Pirâmide")
    print("8. Cilindro")
    print("9. Cone")
    print("10. Esfera")
    print(Fore.RED + "0. SAIR\n")
    try:
        escolha = int(input(Fore.GREEN + "Digite o número correspondente ao polígono desejado: "))
        return escolha
    except ValueError:
        print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

#####################################################################################
        
#Método MAIN
        
"""
Analisa a escolha do usuário (entre as opções de polígonos).
Instancia os objetos correspondentes a escolha.
Obtém o resultado da área ou volume através dos métodos nas classes filhas.
Exibe o resultado.
Repete a operação até que o usuário digite '0' ou 'q'
"""

def main():
    escolha = ...

    while(escolha!=0):

        escolha = menu()

        if escolha == 1:
            quadrilatero = Quadrilatero()
            area = quadrilatero.calcular_area()
            quadrilatero.display_result("Área do quadrilátero:", area)

        elif escolha == 2:
            triangulo = Triangulo()
            area = triangulo.calcular_area()
            triangulo.display_result("Área do triângulo:", area)

        elif escolha == 3:
            circulo = Circulo()
            area = circulo.calcular_area()
            circulo.display_result("Área do círculo:", area)

        elif escolha == 4:
            pentagono = Pentagono()
            area = pentagono.calcular_area()
            pentagono.display_result("Área do pentágono:", area)

        elif escolha == 5:
            hexagono = Hexagono()
            area = hexagono.calcular_area()
            hexagono.display_result("Área do hexágono:", area)

        elif escolha == 6:
            paralelepipedo = Paralelepipedo()
            volume = paralelepipedo.calcular_volume()
            paralelepipedo.display_result("Volume do paralelepípedo:", volume)

        elif escolha == 7:
            piramide = Piramide()
            volume = piramide.calcular_volume()
            piramide.display_result("Volume da pirâmide:", volume)

        elif escolha == 8:
            cilindro = Cilindro()
            volume = cilindro.calcular_volume()
            cilindro.display_result("Volume do cilindro:", volume)

        elif escolha == 9:
            cone = Cone()
            volume = cone.calcular_volume()
            cone.display_result("Volume do cone:", volume)

        elif escolha == 10:
            esfera = Esfera()
            volume = esfera.calcular_volume()
            esfera.display_result("Volume da esfera:", volume)
        
        elif escolha == 0:
            print(Fore.RED + "\nBye bye!\n")
            Fore.RESET
            break

        else:
            print(Fore.RED + "\nOpção inválida!\n")

        continuar = input(Fore.RESET + "\nPressione qualquer tecla para continuar ou 'q' para sair: \n")
        if continuar.lower() == 'q':
            print("\nBye bye!\n")
            Fore.RESET
            break


"""
Como o programa é executado diretamente (e não chamado como um módulo),
o método main() será chamado logo de início
"""

if __name__ == "__main__":
    main()



    