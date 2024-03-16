import math
from colorama import init, Fore


class Polygon:
    
    
    def __init__(self):
        
 
    
        def calcular_area(self, altura, comprimento):
            raise NotImplementedError("Método não implementado na classe filha")
            
        def calcular_volume(self, altura, comprimento, largura):
            raise NotImplementedError("Método não implementado na classe filha")
        
        

class Quadrilatero(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self, altura, comprimento):
        return altura*comprimento
        
        
class Triangulo(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self, altura, comprimento):
        return (altura*comprimento) / 2
        
        
class Circulo(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self, raio):
        return raio*raio*math.pi
        
        
class Pentagono(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self, comprimento, altura):
        return 5*comprimento*altura
        
class Hexagono(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self, comprimento):
        return (3*math.sqrt(3)*math.pow(comprimento,2))/2
        

class Paralelepipedo(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_volume(self, comprimento, altura, largura):
        return comprimento * altura * largura

class Piramide(Polygon):
    def __init__(self):
        self.quadrilatero = Quadrilatero()
        super().__init__()
    
    def calcular_volume(self, altura, comprimento, largura):
        return (1/3) * self.quadrilatero.calcular_area(comprimento,largura) * altura;

class Cilindro(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_volume(self, raio, altura):
        return math.pi * math.pow(raio,2) * altura


class Cone(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_volume(self, raio, altura):
        return ((1/3) * math.pi) * math.pow(raio,2) * altura


class Esfera(Polygon):
    def __init__(self):
        super().__init__()
    
    def calcular_volume(self, raio):
        return ((4/3) * math.pi) * math.pow(raio,3)

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


def main():
    escolha = ...

    while(escolha!=0):

        escolha = menu()

        if escolha == 1:
            try:
                altura = float(input(Fore.YELLOW + "Digite a altura do quadrilátero: "))
                comprimento = float(input("Digite o comprimento do quadrilátero: "))
                print(Fore.CYAN + "Área do quadrilátero:", Quadrilatero().calcular_area(altura, comprimento))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 2:
            try:
                altura = float(input(Fore.YELLOW + "Digite a altura do triângulo: "))
                comprimento = float(input("Digite o comprimento da base do triângulo: "))
                print(Fore.CYAN + "Área do triângulo:", Triangulo().calcular_area(altura, comprimento))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 3:
            try:
                raio = float(input(Fore.YELLOW +"Digite o raio do círculo: "))
                print(Fore.CYAN + "Área do círculo:", Circulo().calcular_area(raio))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 4:
            try:
                comprimento = float(input(Fore.YELLOW +"Digite o comprimento do pentágono: "))
                altura = float(input("Digite a altura do pentágono: "))
                print(Fore.CYAN + "Área do pentágono:", Pentagono().calcular_area(comprimento, altura))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 5:
            try:
                lado = float(input(Fore.YELLOW +"Digite o comprimento do lado do hexágono: "))
                print(Fore.CYAN + "Área do hexágono:", Hexagono().calcular_area(lado))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 6:
            try:
                comprimento = float(input(Fore.YELLOW +"Digite o comprimento do paralelepípedo: "))
                altura = float(input("Digite a altura do paralelepípedo: "))
                largura = float(input("Digite a largura do paralelepípedo: "))
                print(Fore.CYAN + "Volume do paralelepípedo:", Paralelepipedo().calcular_volume(comprimento, altura, largura))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 7:
            try:
                altura = float(input(Fore.YELLOW +"Digite a altura da pirâmide: "))
                comprimento = float(input("Digite o comprimento da base da pirâmide: "))
                largura = float(input("Digite a largura da base da pirâmide: "))
                print(Fore.CYAN + "Volume da pirâmide:", Piramide().calcular_volume(altura, comprimento, largura))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 8:
            try:
                raio = float(input(Fore.YELLOW +"Digite o raio do cilindro: "))
                altura = float(input("Digite a altura do cilindro: "))
                print(Fore.CYAN + "Volume do cilindro:", Cilindro().calcular_volume(raio, altura))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 9:
            try:
                raio = float(input(Fore.YELLOW +"Digite o raio do cone: "))
                altura = float(input("Digite a altura do cone: "))
                print(Fore.CYAN + "Volume do cone:", Cone().calcular_volume(raio, altura))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

        elif escolha == 10:
            try:
                raio = float(input(Fore.YELLOW +"Digite o raio da esfera: "))
                print(Fore.CYAN + "Volume da esfera:", Esfera().calcular_volume(raio))
            except ValueError:
                print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")
        
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

if __name__ == "__main__":
    main()



    