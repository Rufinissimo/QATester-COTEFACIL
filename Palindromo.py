"""
    Teste de Palíndromo.
        ...
        O programa Teste de Palíndromo tem como objetivo testar uma palavra de modo que ela seja igual ao ler ao contrário.
"""


class Palindromo:
    """
        Classe responsável por gerar as funções de inicialização e de execução do programa.

        
        Não exige parâmetros.
    """

    def __init__(self):
        """
            Função para inicialização do programa.

            
            Não exige parâmetros.
        """
        pass

    def teste(self):
        """
            Função para a execução do teste.
                
            
            Será gerado ao usuário um input do tipo string, aceitando apenas uma palavra para o teste.

            Usando uma estrutura de loop, o programa irá analisar o input de entrada.
                ...
                Caso a entrada contenha mais de um valor ou não seja do tipo string, o programa emite uma mensagem de erro ao usuário.
                Ao inserir 'sair', será permitida a opção de saída ao usuário, encerrando o programa.
                Qualquer entrada do tipo string diferente de 'sair' será aceita e o teste será inicializado.
                    ...
                    Será gerada uma variável auxiliar que recebe a palavra inserida e a inverte, de trás para frente.
                    Se a palavra de entrada for igual a varíavel auxiliar, o programa identifica o palíndromo e emite uma mensagem de confirmação ao usuário.
                    Se a palavra de entrada for diferente da varíavel auxiliar, o programa desconhece o palíndromo e emite uma mensagem de negação ao usuário.
                        
            Não exige parâmetros.
        """
        while True:
            entrada = input("\nInsira uma palavra para o teste de palíndromo (ou 'sair' para encerrar o programa): ").lower()
            if entrada == 'sair':
                print("Programa encerrado.")
                exit()
            if entrada.isalpha() and len(entrada.split()) == 1:
                reverso = entrada[::-1]
                print(f"A palavra {entrada.upper()} é um palíndromo." if entrada == reverso else f"A palavra {entrada.upper()} não é um palíndromo.")
            else:
                print("Entrada inválida. Insira apenas uma palavra com caracteres alfabéticos.")


"""
    Instruções para execução do programa.
        
    
    Deve-se criar uma variável que receba uma instância da classe Palindromo.
    Para a execução do teste, deve-se chamar o método teste() na instância criada.
        ...
        Exemplo de uso:
            
            palavra = Palindromo()
            palavra.teste()
        
    Para importar a classe, deve-se criar um novo arquivo e mantê-lo no mesmo diretório do arquivo Palindromo.
        ...
        Exemplo de uso:
            
            from Palindromo import Palindromo
"""
