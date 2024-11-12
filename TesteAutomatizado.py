"""
    Teste Automatizado - COTEFÁCIL
    ------------------------------
    O objetivo deste programa é automatizar ações do navegador e preencher um formulário de cadastro fictício, 
    com fins exclusivamente acadêmicos.

        
    IMPORTAÇÃO DE BIBLIOTECAS:
    --------------------------
    O programa utiliza a biblioteca Selenium juntamente com algumas ferramentas auxiliares.
    Para evitar conflitos com outros pacotes da instalação global do Python, recomenda-se a instalação das biliotecas em um ambiente virtual (opcional).

    
    CONFIGURAÇÕES DO NAVEGADOR:
    ---------------------------
    O navegador é configurado usando o WebDriver do Selenium e o ChromeDriverManager para garantir a compatibilidade com a versão mais recente do Chrome.
    O Service é utilizado para gerenciar o processo de inicialização do driver do navegador.

    Para acessar uma página específica, basta definir a URL completa do site a ser automatizado.
    Para usar outro navegador, como o Firefox ou o Edge, deve-se alterar o WebDriver e as configurações correspondentes (CONSULTAR).

    
    SITE E TELAS USADAS:
    ------
    Site: Demo Automation Testing, site fictício para estudos de automação.
    Login: Na tela de login, o programa preenche o campo de e-mail e simula a confirmação do login.
    Formulário: Na tela de formulário, o programa preenche todos os campos com dados pessoais do usuário, simulando um cadastro completo.

    Obs: Os dados inseridos pelo usuário não serão salvos na memória ou banco de dados do site.

    
    BUSCA PELO ELEMENTO HTML E AÇÕES EXECUTADAS:
    --------------------------------------------
    Para cada função criada, o programa localiza os elementos HTML da página e aguarda até que eles se tornem visíveis ou interativos, 
    dependendo da ação a ser executada.

    Cada elemento encontrado será manipulado com uma das ações especificadas abaixo, e o terminal exibirá uma mensagem 
    de confirmação. Caso o elemento não seja encontrado ou ocorra um erro de execução das ações, o terminal exibirá uma mensagem de erro.

    
    Métodos principais utilizados:
    ------------------------------
    'WebDriverWait().until(EC.presence_of_element_located((By.ELEMENTO)))': Aguarda até que o elemento esteja presente no DOM.
    'WebDriverWait().until(EC.visibility_of_element_located((By.ELEMENTO)))': Aguarda até que o elemento esteja visível.
    'WebDriverWait().until(EC.element_to_be_clickable((By.ELEMENTO)))': Aguarda até que o elemento esteja clicável.
    'find_element(By.ELEMENTO)': Localiza um elemento pelo tipo especificado.

    
    Tipos de elementos HTML:
    ------------------------
    'ID': Localiza elementos pelo atributo 'ID'.
    'XPATH': Localiza elementos usando a expressão 'XPATH'.
    'LINK_TEXT': Localiza links pelo texto visível na tela.

    
    Ações executadas nos elementos:
    -------------------------------
    'click()': Executa um clique no elemento.
    'send_keys()': Envia um texto determinado pelo usuário para um campo de entrada (input).
    'select_by_value()': Seleciona uma opção em um campo '<select>' com base no valor.
    'execute_script()': Executa código JavaScript no contexto da página.
"""


"""
    BIBLIOTECAS
    -----------
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import sys
from colorama import Fore, Style, init


"""
    CONFIGURAÇÕES
    -------------
"""

init(autoreset=True)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

url = "https://demo.automationtesting.in/Index.html" # Site fictício para testes automatizados.
navegador.get(url)

print(f"\n\nTeste Automatizado - {Fore.GREEN}Cotefácil\n\n")
print("_" * 60)


"""
    TELA DE LOGIN
    -------------
"""

def preencher_login(navegador, email_login):
    """
        Barra de login 'Email id for Sign Up'
        -------------------------------------
        Inserir e-mail do usuário.
        O input exige '@' e '.' como separadores de domínio, sem espaços.

            Exemplo: 'usuario@email.com'

        Parâmetros: Navegador, e-mail do usuário.
    """
    try:
        if not email_login:
            raise ValueError("O campo de e-mail não pode estar vazio.")
        
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_pattern, email_login):
            raise ValueError("Formato inválido. Exemplo de uso: usuario@email.com")
    
        input_email = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
        input_email.send_keys(email_login)
        print(f"{Fore.GREEN}\nE-mail{Style.RESET_ALL} '{email_login}' {Fore.GREEN}inserido com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o e-mail:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def confirmar_login(navegador):
    """
        Botão de envio
        --------------
        Clicar no botão de envio.

        Parâmetro: Navegador.
    """
    try:
        enviar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, 'enterimg')))
        enviar.click()
        print(Fore.GREEN + "\nLogin executado com sucesso.")

    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao executar o clique:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


"""
    TELA DE FORMULÁRIO
    ------------------
"""

def preencher_nome(navegador, nome):
    """
        Barra 'Full Name'
        -----------------
        Inserir o nome do usuário.
        O input não exige caracteres específicos.

        Parâmetros: Navegador, nome do usuário.
    """
    try:
        if not nome:
            raise ValueError("O campo de nome não pode estar vazio.")

        barra_nome = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input')))
        barra_nome.send_keys(nome)
        print(f"{Fore.GREEN}\nNome{Style.RESET_ALL} '{nome}' {Fore.GREEN}inserido com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o nome:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def preencher_sobrenome(navegador, sobrenome):
    """
        Barra 'Last Name'
        -----------------
        Inserir o sobrenome do usuário.
        O input não exige caracteres específicos.

        Parâmetros: Navegador, sobrenome do usuário.
    """
    try: 
        if not sobrenome:
            raise ValueError("O campo de sobrenome não pode estar vazio.")

        barra_sobrenome = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input')))
        barra_sobrenome.send_keys(sobrenome)
        print(f"{Fore.GREEN}\nSobrenome{Style.RESET_ALL} '{sobrenome}' {Fore.GREEN}inserido com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o sobrenome:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def preencher_endereco(navegador, endereco):
    """
        Barra 'Address'
        ---------------
        Inserir o endereço do usuário.
        O input não exige caracteres específicos.

        Parâmetros: Navegador, endereço do usuário.
    """
    try:
        if not endereco:
            raise ValueError("O campo de endereço não pode estar vazio.")    
    
        barra_endereco = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basicBootstrapForm"]/div[2]/div/textarea')))
        barra_endereco.send_keys(endereco)
        print(f"{Fore.GREEN}\nEndereço{Style.RESET_ALL} '{endereco}' {Fore.GREEN}inserido com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o endereço:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def preencher_email(navegador, email):
    """
        Barra 'Email address'
        ---------------------
        Inserir e-mail do usuário.
        O input exige '@' e '.' como separadores de domínio, sem espaços.

            Exemplo: 'usuario@email.com'

        Parâmetros: Navegador, e-mail do usuário.
    """
    try:
        if not email:
            raise ValueError("O campo de e-mail não pode estar vazio.")
    
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_pattern, email_login):
            raise ValueError("\nFormato inválido. Exemplo de uso: 'usuario@email.com'")

        barra_email = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="eid"]/input')))
        barra_email.send_keys(email)
        print(f"{Fore.GREEN}\nE-mail{Style.RESET_ALL} '{email}' {Fore.GREEN}inserido com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o e-mail:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def preencher_telefone(navegador, telefone):
    """
        Barra 'Phone'
        -------------
        Inserir número de telefone do usuário.
        O input exige 10 dígitos para preencher o telefone.

        Parâmetros: Navegador, número de telefone do usuário.
    """
    try:
        if not telefone:
            raise ValueError("O campo de telefone não pode estar vazio.")
        
        telefone_pattern = r'^\d{10}$'

        if not re.match(telefone_pattern, telefone):
            raise ValueError("\nFormato inválido. Insira 10 dígitos.")

        barra_telefone = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basicBootstrapForm"]/div[4]/div/input')))
        barra_telefone.send_keys(telefone)
        print(f"{Fore.GREEN}\nTelefone{Style.RESET_ALL} '{telefone}' {Fore.GREEN}inserido com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o telefone:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def selecionar_genero(navegador, genero):
    """
        Radio button 'Gender'
        ---------------------
        Selecionar o gênero do usuário.
        O radio button aceita apenas uma opção como gênero:
            
            'Feminino', 'Masculino'.
            
        Parâmetros: Navegador, gênero do usuário.
    """
    try:
        if not genero:
            raise ValueError("O campo de gênero não pode estar vazio.")

        if genero == "Feminino":
            feminino = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='FeMale']")))
            feminino.click()
            print(f"{Fore.GREEN}\nGênero{Style.RESET_ALL} '{genero}' {Fore.GREEN}selecionado com sucesso.{Style.RESET_ALL}")
        elif genero == "Masculino":
            masculino = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='Male']")))
            masculino.click()
            print(f"{Fore.GREEN}\nGênero{Style.RESET_ALL} '{genero}' {Fore.GREEN}selecionado com sucesso.{Style.RESET_ALL}")
        else:
            raise ValueError(f"Gênero '{genero}' inválido. Selecione 'Feminino' ou 'Masculino'.")
        
    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o gênero:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def selecionar_hobbie(navegador, hobbies):
    """
        Checkbox 'Hobbies'
        ------------------
        Selecionar o hobbie do usuário.
        O checkbox aceita uma ou mais opções da lista de hobbies. 
            
        Parâmetros: Navegador, hobbies do usuário.
    """
    lista_hobbies = ["Cricket", "Movies", "Hockey"]
    try:
        if not hobbies:
            raise ValueError("O campo de hobbies não pode estar vazio.")

        for hobbie in hobbies:
            if hobbie not in lista_hobbies:
                raise ValueError(f"O hobbie '{hobbie}' não é válido.")
                
            hobby_checkbox = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f"//input[@type='checkbox' and @value='{hobbie}']")))

            if not hobby_checkbox.is_selected():
                hobby_checkbox.click()
                print(f"{Fore.GREEN}\nHobbie{Style.RESET_ALL} '{hobbie}' {Fore.GREEN}selecionado com sucesso.{Style.RESET_ALL}")
            else:
                raise ValueError(f"O hobbie '{hobbie}' já estava selecionado.")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o hobbie:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def selecionar_idiomas(navegador, idiomas):
    """
        Barra 'Languages'
        -----------------
        Selecionar os idiomas do usuário.
        O botão de seleção aceita uma ou mais opções da lista de idiomas.
        
        Parâmetros: Navegador, idiomas do usuário.
    """
    lista_idiomas = ['Arabic', 'Bulgarian', 'Catalan', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Filipino', 
                     'Finnish', 'French', 'German', 'Greek','Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 
                     'Japanese', 'Korean', 'Latvian', 'Lithuanian', 'Malay', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Romanian', 
                     'Russian', 'Serbian', 'Spanish', 'Swedish', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese']
    try:
        idiomas_invalidos = [idioma for idioma in idiomas if idioma not in lista_idiomas]

        if idiomas_invalidos:
            raise ValueError(f"Idiomas inválidos: {', '.join(idiomas_invalidos)}.")

        navegador.find_element(By.XPATH, '//*[@id="msdd"]').click()
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul')))

        for idioma in idiomas:
            opcao = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, idioma)))
            navegador.execute_script("arguments[0].scrollIntoView()", opcao)
            opcao.click()
            print(f"{Fore.GREEN}\nIdioma{Style.RESET_ALL} '{idioma}' {Fore.GREEN}selecionado com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o idioma:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def selecionar_skill(navegador, skill):
    """
        Botão de opção 'Skills'
        ----------------------
        Selecionar a skill do usuário.
        O botão de seleção aceita apenas uma opção da lista de skills.

        Parâmetros: Navegador, skills do usuário.
    """
    lista_skills = ['Adobe InDesign', 'Adobe Photoshop', 'Analytics', 'Android', 'APIs', 'Art Design', 'AutoCAD', 'Backup Management', 'C', 'C++', 'Certifications', 
                    'Client Server', 'Client Support', 'Configuration', 'Content Management', 'Content Management Systems (CMS)', 'Corel Draw', 'Corel Word Perfect', 
                    'CSS', 'Data Analytics', 'Desktop Publishing', 'Design', 'Diagnostics', 'Documentation', 'End User Support', 'Email', 'Engineering', 'Excel', 
                    'FileMaker Pro', 'Fortran HTML', 'Implementation', 'Installation', 'Internet', 'iOS', 'iPhone', 'Linux', 'Java', 'JavaScript', 'Mac', 'Matlab', 
                    'Maya', 'Micrisoft Excel', 'Microsoft', 'Microsoft Office', 'Microsoft Outlook', 'Microsoft Publisher', 'Microsoft Word', 'Microsoft Visual', 
                    'Mobile', 'MySQL', 'Networks', 'Open Source Software', 'Oracle', 'Perl', 'PHP', 'Presentations', 'Processing', 'Programming', 'PT Modeler', 
                    'Python', 'QuickBooks', 'Ruby', 'Shade', 'Software', 'Spreadsheet', 'SQL', 'Support', 'System Administration', 'Tech Support', 'Troubleshooting', 
                    'Unix', 'UI / UX', 'Page Design', 'Windows', 'Word Processing', 'XML', 'XHTML']

    try:
        if not skill:
            raise ValueError("O campo de skill não pode estar vazio.")
        
        if skill not in lista_skills:
            raise ValueError(f"A skill '{skill}' não é válida.")

        skills = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "Skills")))
        select = Select(skills)
        select.select_by_value(skill)
        print(f"{Fore.GREEN}\nSkill{Style.RESET_ALL} '{skill}' {Fore.GREEN}selecionada com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir a skill:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def selecionar_pais(navegador, pais):
    """
        Botão de opção 'Country'
        ------------------------
        Selecionar o país do usuário.
        O botão de seleção aceita apenas um país como opção.
        Caso o país selecionado pelo usuário não conste na lista de opções, o programa irá inserí-lo à lista através do comando execute_script().

        Parâmetros: Navegador, país do usuário.
    """
    try:
        if not pais:
            raise ValueError("O campo de país não pode estar vazio.")
    
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, "countries")))
        navegador.execute_script(
            "var select = document.getElementById('countries');"
            "var option = document.createElement('option');"
            f"option.text = '{pais}';"
            f"option.value = '{pais}';"
            "select.add(option);"
            f"select.value = '{pais}';"
        )
        print(f"{Fore.GREEN}\nPaís{Style.RESET_ALL} '{pais}' {Fore.GREEN}selecionado com sucesso.{Style.RESET_ALL}")
    
    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir o país:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def preencher_data(navegador, ano, mes, dia):
    """
        Botão de opção 'Date Of Birth'
        ------------------------------
        Inserir data de nascimento do usuário.
        O botão de selecão de data exige os seguintes formatos:
          
            Ano: Número inteiro de 1916 a 2015, inserindo 4 dígitos (XXXX).
            Mês: Número inteiro de 1 a 12.
            Dia: Número inteiro de 1 a 31.

        Parâmetros: Navegador, ano, mês e dia do nascimento do usuário.
    """
    try: 
        if not (ano, mes, dia):
            raise ValueError("Os campos de ano, mês e dia não podem estar vazios.")
        
        if not (1916 <= ano <= 2015):
            raise ValueError("Insira um ano entre 1916 e 2015.")
        if not (1 <= mes <= 12):
            raise ValueError("Insira um mês entre 1 e 12.")
        if not (1 <= dia <= 31):
            raise ValueError("Insira um dia entre 1 e 31.")
        
        navegador.execute_script("document.getElementById('yearbox').click();")
        barra_ano = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'yearbox')))
        barra_ano.send_keys(str(ano), Keys.RETURN)

        barra_mes = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')))
        select = Select(barra_mes)
        meses = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        select.select_by_visible_text(meses[mes])

        barra_dia = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'daybox')))
        select = Select(barra_dia)
        select.select_by_value(str(dia))

        print(f"{Fore.GREEN}\nData{Style.RESET_ALL} '{dia}/{mes}/{ano}' {Fore.GREEN}inserida com sucesso.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir a data:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def inserir_imagem(navegador, imagem):
    """
        Botão 'Escolher arquivo'
        ------------------------
        Inserir uma imagem do usuário (OPCIONAL).
        O input exige o caminho da imagem.

        Parâmetros: Navegador, imagem do usuário.
    """
    try:
        if not imagem:
            return

        botao_imagem = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'imagesrc')))
        caminho_imagem = f"{imagem}"
        botao_imagem.send_keys(caminho_imagem)
        print(Fore.GREEN + "\nImagem inserida com sucesso.")

    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir a imagem:{Style.RESET_ALL} {e}")
    print("_" * 60)


def preencher_senha(navegador, senha):
    """
        Barras 'Password' e 'Confirm Password'
        --------------------------------------
        Inserir e confirmar a senha do usuário.
        O input exige ao menos uma letra minúscula, uma maiúscula e um número para preencher a senha.

        Parâmetros: Navegador, senha do usuário.
    """
    try:
        if not senha:
            raise ValueError("O campo de senha não pode estar vazio.")
        
        senha_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'

        if not re.match(senha_pattern, senha):
            raise ValueError("Formato inválido. A senha deve conter 8 caracteres incluindo ao menos uma letra minúscula, uma maiúscula e um número.")
        
        barra_senha = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'firstpassword')))
        barra_senha.send_keys(senha)

        barra_confirmação = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'secondpassword')))
        barra_confirmação.send_keys(senha)
        print(Fore.GREEN + "\nSenha inserida com sucesso.")

    except ValueError as e:
        print(f"{Fore.RED}\nErro de entrada:{Style.RESET_ALL} {e}")
        sys.exit()
    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao inserir a senha:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


def confirmar_cadastro(navegador):
    """
        Botão de finalização
        --------------------
        Clicar no botão para finalizar o cadastro.

        Parâmetro: Navegador.
    """
    try:
        botao = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, 'submitbtn')))
        botao.click()
        print(Fore.GREEN + "\n\n\nFormulário preenchido com sucesso.")

    except NoSuchElementException as e:
        print(f"{Fore.RED}\nErro ao localizar o elemento:{Style.RESET_ALL} {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}\nErro ao executar o clique:{Style.RESET_ALL} {e}")
        sys.exit()
    print("_" * 60)


"""
    INSTRUÇÕES DE USO
    -----------------
    Inserir um tipo de valor para cada variável criada.
    Para cada função, inserir a variável como argumento.
"""

"""
    Exemplo de uso:
    ---------------
    email_login = "usuario@email.com" -> tipo string (str)
    preencher_login(navegador, email_login)
"""
email_login = "alucard@castlevania.com"
preencher_login(navegador, email_login)
confirmar_login(navegador)


"""
    Exemplo de uso:
    ---------------
    nome = "Nome do usuário" -> tipo string (str)
    preencher_nome(navegador, nome)
"""
nome = "Alucard"
preencher_nome(navegador, nome) 


"""
    Exemplo de uso:
    ---------------
    sobrenome = "Sobrenome do usuário" -> tipo string (str)
    preencher_sobrenome(navegador, sobrenome)
"""
sobrenome = "Tepes"
preencher_sobrenome(navegador, sobrenome) 


"""
    Exemplo de uso:
    ---------------
    endereco = "Endereço do usuário" -> tipo string (str)
    preencher_endereco(navegador, endereco)
"""
endereco = "Valachia, 666"
preencher_endereco(navegador, endereco) 


"""
    Exemplo de uso:
    ---------------
    email = "usuario@email.com" -> tipo string (str)
    preencher_email(navegador, email)
"""
email = "alucard@castlevania.com"
preencher_email(navegador, email) 


"""
    Exemplo de uso:
    ---------------
    telefone = "0123456789" -> tipo string (str)
    preencher_telefone(navegador, telefone)
"""
telefone = "0123456789"
preencher_telefone(navegador, telefone) 


"""
    Exemplo de uso:
    ---------------
    genero = "Gênero do usuário" -> tipo string (str)
    preencher_genero(navegador, genero)
"""
genero = "Masculino"
selecionar_genero(navegador, genero) 


"""
    Exemplo de uso:
    ---------------
    hobbie = ["Hobbie do usuário"] -> tipo lista (list)
    selecionar_hobbie(navegador, hobbie)
"""
hobbies = ["Movies"]
selecionar_hobbie(navegador, hobbies)


"""
    Exemplo de uso:
    ---------------
    idiomas = ["Idiomas do usuário"] -> tipo lista (list)
    selecionar_idiomas(navegador, idiomas)
"""
idiomas = ["Portuguese", "English"]
selecionar_idiomas(navegador, idiomas)


"""
    Exemplo de uso:
    ---------------
    skill = "Skill do usuário" -> tipo string (str)
    selecionar_skill(navegador, skill)
"""
skill = "Python"
selecionar_skill(navegador, skill) 


"""
    Exemplo de uso:
    ---------------
    pais = "País do usuário" -> tipo string (str)
    selecionar_pais(navegador, pais)
"""
pais = "Brasil"
selecionar_pais(navegador, pais)


"""
    Exemplo de uso:
    ---------------
    ano = Ano de nascimento do usuário -> tipo inteiro (int)
    mes = Mês de nascimento do usuário -> tipo inteiro (int)
    dia = Dia de nascimento do usuário -> tipo inteiro (int)
    preencher_data(navegador, ano, mes, dia)
"""
ano = 1950
mes = 12
dia = 2
preencher_data(navegador, ano, mes, dia)

"""
    Exemplo de uso:
    ---------------
    imagem = "C:\\Users\\usuario\\pasta\\imagem.jpg" -> tipo string (str)
    inserir_imagem(navegador, imagem)
"""
imagem = ""
inserir_imagem(navegador, imagem)


"""
    Exemplo de uso:
    ---------------
    senha = "Senha123" -> tipo string (str)
    preencher_senha(navegador, senha)
"""
senha = "Alucard123"
preencher_senha(navegador, senha)
confirmar_cadastro(navegador)


"""
    Para encerrar automaticamente, usar:

        navegador.quit()

    Para encerrar manualmente, clicar no botão 'Enter' no input a seguir.
"""
print(input("\nPara encerrar o programa manualmente, aperte a tecla 'Enter'."))