# Importa a biblioteca Tkinter, utilizada para criar a interface gráfica da calculadora.
import tkinter as tk

# Cria a função responsável por inserir os números no visor.
def digitar(numero):
    # Permite modificar a variável novo_calculo, que foi criada fora da função.
    global novo_calculo

    # Verifica se um cálculo acabou de ser realizado.
    if novo_calculo:
        # Apaga o resultado anterior do visor.
        visor.delete(0, tk.END)
        # Informa que um novo cálculo está começando.
        novo_calculo = False

    # Verifica se o visor está apresentando a mensagem de segundo número.
    elif visor.get() == "Digite o segundo número":
        # Apaga a mensagem do visor.
        visor.delete(0, tk.END)

    # Verifica se ocorreu uma divisão por zero.
    elif visor.get() == "ERRO: divisão por zero":
        # Apaga a mensagem de erro.
        visor.delete(0, tk.END)

    # Insere o número escolhido no final do conteúdo do visor.
    visor.insert(tk.END, numero)

# Cria a função responsável por limpar a calculadora.
def limpar():
    # Permite modificar as variáveis criadas fora da função.
    global numero1, operacao, novo_calculo

    # Reinicia o controle de cálculo.
    novo_calculo = False

    # Apaga todo o conteúdo do visor.
    visor.delete(0 , tk.END)
    # Limpa o valor armazenado do primeiro número.
    numero1=None
    # Limpa a operação matemática selecionada.
    operacao=None

# OPERAÇÕES, VARIÁVEIS E TRATAMENTOS

# Inicializa a variável que armazenará o primeiro número.
numero1 = None
# Inicializa a variável que armazenará a operação matemática.
operacao = None
# Controla se um cálculo acabou de ser realizado.
novo_calculo = False

# Cria a função responsável por selecionar a operação matemática.
def selecionar_operacao(simbolo):
    # Permite modificar as variáveis globais.
    global numero1, operacao, novo_calculo

    # Obtém o conteúdo atual do visor.
    texto = visor.get()

    # Verifica se existe alguma mensagem de erro no visor.
    if texto in ("Digite o segundo número", "ERRO: divisão por zero"):
        # Apaga a mensagem apresentada.
        visor.delete(0, tk.END)
        # Limpa o primeiro número armazenado.
        numero1 = None
        # Limpa a operação selecionada.
        operacao = None
        # Reinicia o controle de cálculo.
        novo_calculo = False
        # Encerra a função.
        return

    # Verifica se o visor está vazio.
    if texto == "":
        # Encerra a função sem selecionar uma operação.
        return

    # Converte o primeiro número em decimal e substitui a vírgula por ponto.
    numero1 = float(texto.replace(",", "."))
    # Armazena o símbolo da operação escolhida.
    operacao = simbolo
    # Informa que o cálculo ainda não foi finalizado.
    novo_calculo = False

    # Limpa o visor para receber o segundo número.
    visor.delete(0, tk.END)

# Cria a função responsável por realizar os cálculos.
def calcular():
    # Permite modificar as variáveis globais.
    global numero1, operacao, novo_calculo

    # Verifica se o visor está apresentando a mensagem de segundo número.
    if visor.get() == "Digite o segundo número":
        # Impede a realização do cálculo.
        return

    # Verifica se o visor está vazio e nenhuma operação foi selecionada.
    elif visor.get() == "" and operacao is None:
        # Encerra a função.
        return

    # Verifica se nenhuma operação matemática foi selecionada.
    elif operacao is None:
        # Impede a realização do cálculo.
        return

    # Verifica se uma operação foi selecionada, mas o segundo número não foi digitado.
    elif visor.get() == "" and operacao is not None:
        # Exibe uma mensagem solicitando o segundo número.
        visor.insert(tk.END, "Digite o segundo número")
        # Encerra a função.
        return

    # Obtém o segundo número e transforma o texto em um valor decimal.
    numero2 = float(visor.get().replace(",", "."))

    # Verifica se a operação escolhida foi adição.
    if operacao == "+":
        # Soma o primeiro número com o segundo.
        resultado = numero1 + numero2

    # Verifica se a operação escolhida foi subtração.
    elif operacao == "-":
        # Subtrai o segundo número do primeiro.
        resultado = numero1 - numero2

    # Verifica se a operação escolhida foi multiplicação.
    elif operacao == "x":
        # Multiplica os dois números.
        resultado = numero1 * numero2

    # Verifica se a operação escolhida foi divisão.
    elif operacao == "÷":
        # Verifica se o segundo número é igual a zero.
        if numero2 == 0:
            # Limpa o visor.
            visor.delete(0, tk.END)
            # Exibe a mensagem de erro.
            visor.insert(tk.END, "ERRO: divisão por zero")

            # Limpa o primeiro número armazenado.
            numero1 = None
            # Limpa a operação selecionada.
            operacao = None
            # Permite iniciar um novo cálculo.
            novo_calculo = True
            # Encerra a função para impedir a divisão por zero.
            return

        # Divide o primeiro número pelo segundo.
        resultado = numero1 / numero2

    # Armazena o resultado na variável do primeiro número.
    numero1 = resultado
    # Limpa a operação selecionada.
    operacao = None

    # Apaga o conteúdo atual do visor.
    visor.delete(0, tk.END)
    # Formata o resultado com até oito casas decimais e remove zeros desnecessários.
    resultado_formatado = f"{resultado:.8f}".rstrip("0").rstrip(".")
    # Exibe o resultado utilizando vírgula como separador decimal.
    visor.insert(tk.END, resultado_formatado.replace(".", ","))

    # Informa que um cálculo foi finalizado.
    novo_calculo = True

# Cria a função responsável por apagar o último caractere digitado.
def apagar_ultimo():
    # Obtém o conteúdo atual do visor.
    texto = visor.get()

    # Verifica se o visor apresenta alguma mensagem de erro.
    if texto in ("Digite o segundo número", "ERRO: divisão por zero"):
        # Impede que a mensagem seja apagada parcialmente.
        return

    # Verifica se o visor não está vazio.
    if texto != "":
        # Apaga somente o último caractere digitado.
        visor.delete(len(texto) - 1, tk.END)

# Cria a função responsável por inserir a vírgula decimal.
def decimal():
    # Permite modificar a variável global novo_calculo.
    global novo_calculo

    # Obtém o conteúdo atual do visor.
    texto = visor.get()

    # Verifica se um cálculo acabou de ser realizado.
    if novo_calculo:
        # Apaga o resultado anterior.
        visor.delete(0, tk.END)
        # Reinicia o controle de cálculo.
        novo_calculo = False
        # Insere zero e vírgula para começar um número decimal.
        visor.insert(tk.END, "0,")
        # Encerra a função.
        return

    # Verifica se o visor está vazio.
    elif texto == "":
        # Insere zero e vírgula.
        visor.insert(tk.END, "0,")
        # Encerra a função.
        return

    # Verifica se o visor apresenta alguma mensagem de erro.
    elif texto in ("Digite o segundo número", "ERRO: divisão por zero"):
        # Impede a inserção da vírgula.
        return

    # Verifica se o número ainda não possui uma vírgula.
    elif "," not in texto:
        # Insere a vírgula no final do número.
        visor.insert(tk.END, ",")

# Cria a função responsável por validar os caracteres digitados.
def validar_entrada(texto):
    # Verifica se o conteúdo está vazio.
    if texto == "":
        # Permite deixar o visor vazio.
        return True

    # Verifica se o texto corresponde a alguma mensagem utilizada pela calculadora.
    if texto in ("Digite o segundo número","ERRO: divisão por zero"):
        # Permite que essas mensagens apareçam no visor.
        return True

    # Verifica se existe mais de uma vírgula no texto.
    if texto.count(",") > 1:
        # Impede a entrada de mais de uma vírgula.
        return False

    # Remove temporariamente a vírgula e verifica se o restante contém apenas números.
    return texto.replace(",", "").isdigit()

# Cria a função responsável pelos efeitos visuais dos botões.
def adicionar_efeito(botao, cor_original, cor_hover):
    # Associa um evento ao botão quando o mouse entra na sua área.
    botao.bind(
        # Identifica quando o cursor entra na área do botão.
        "<Enter>",
        # Altera a cor de fundo para a cor de destaque.
        lambda evento: botao.config(bg=cor_hover))

    # Associa outro evento ao botão quando o mouse sai da sua área.
    botao.bind(
        # Identifica quando o cursor sai da área do botão.
        "<Leave>",
        # Restaura a cor de fundo original. 
        lambda evento: botao.config(bg=cor_original))


# INTERFACE DA CALCULADORA

# Cria a janela principal da calculadora.
janela = tk.Tk()

# Define o título que aparece na parte superior da janela.
janela.title("Calculadora")

# Define a cor de fundo da janela.
janela.configure(bg="#121212")
# Impede que a janela seja redimensionada.
janela.resizable(False, False)

# CONFIGURAÇÃO DAS 4 COLUNAS

# Inicia uma repetição para configurar as quatro colunas.
for coluna in range(4):
    # Configura cada coluna para distribuir o espaço igualmente.
    janela.grid_columnconfigure(coluna, weight=1)

# CONFIGURAÇÃO DAS 5 LINHAS DOS BOTÕES

# Inicia uma repetição que percorre as cinco linhas dos botões.
for linha in range(1, 6):
    # Configura cada linha para distribuir o espaço igualmente.
    janela.grid_rowconfigure(linha, weight=1)

# Registra a função de validação para utilizá-la no visor.
validacao = janela.register(validar_entrada)

# Cria o campo de texto onde os números e resultados serão exibidos.
visor = tk.Entry( janela, width=18, justify="right", font=("Arial", 22), bg="#1E1E1E", fg="white", insertbackground="white", bd=0, highlightthickness=0, validate="key", validatecommand=(validacao, "%P"))

# Posiciona o visor na primeira linha, ocupando as quatro colunas.
visor.grid(row=0, column=0, columnspan=4, padx=8, pady=12, ipady=15, sticky="nsew")

# PRIMEIRA LINHA DA CALCULADORA

# Cria o botão 7 e define sua aparência e função.
botao_7 = tk.Button(janela, text="7" , width=6, command= lambda: digitar("7"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 7 na primeira linha e primeira coluna.
botao_7.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)

# Cria o botão 8.
botao_8 = tk.Button(janela, text="8" , width=6, command= lambda: digitar("8"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 8 na primeira linha e segunda coluna.
botao_8.grid(row=1, column=1, sticky="nsew", padx=4, pady=4)

# Cria o botão 9.
botao_9 = tk.Button(janela, text="9" , width=6, command= lambda: digitar("9"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 9 na primeira linha e terceira coluna.
botao_9.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)

# Cria o botão de subtração e associa a operação matemática -.
botao_subtrair = tk.Button(janela, text="-", width=6, command=lambda: selecionar_operacao("-"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão de subtração na primeira linha e quarta coluna.
botao_subtrair.grid(row= 1,column=3, sticky="nsew", padx=4, pady=4)

# SEGUNDA LINHA DA CALCULADORA

# Cria o botão 4.
botao_4 = tk.Button(janela, text="4" , width=6, command= lambda: digitar("4"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 4 na segunda linha e primeira coluna.
botao_4.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)

# Cria o botão 5.
botao_5 = tk.Button(janela, text="5" , width=6, command= lambda: digitar("5"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 5 na segunda linha e segunda coluna.
botao_5.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)

# Cria o botão 6.
botao_6 = tk.Button(janela, text="6" , width=6, command= lambda: digitar("6"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 6 na segunda linha e terceira coluna.
botao_6.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)

# Cria o botão de multiplicação e associa a operação matemática x.
botao_multiplicar = tk.Button(janela, text="x", width=6, command=lambda: selecionar_operacao("x"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão de multiplicação na segunda linha e quarta coluna.
botao_multiplicar.grid(row= 2,column=3, sticky="nsew", padx=4, pady=4)

# TERCEIRA LINHA DA CALCULADORA

# Cria o botão 1.
botao_1 = tk.Button(janela, text="1" , width=6, command= lambda: digitar("1"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 1 na terceira linha e primeira coluna.
botao_1.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)

# Cria o botão 2.
botao_2 = tk.Button(janela, text="2" , width=6, command= lambda: digitar("2"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 2 na terceira linha e segunda coluna.
botao_2.grid(row=3, column=1, sticky="nsew", padx=4, pady=4)

# Cria o botão 3.
botao_3 = tk.Button(janela, text="3" , width=6, command= lambda: digitar("3"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 3 na terceira linha e terceira coluna.
botao_3.grid(row=3, column=2, sticky="nsew", padx=4, pady=4)

# Cria o botão de divisão e associa a operação matemática ÷.
botao_dividir = tk.Button(janela, text="÷", width=6, command=lambda: selecionar_operacao("÷"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão de divisão na terceira linha e quarta coluna.
botao_dividir.grid(row= 3,column=3, sticky="nsew", padx=4, pady=4)


# QUARTA LINHA DA CALCULADORA

# Cria o botão 0.
botao_0 = tk.Button(janela, text="0" , width=6, command= lambda: digitar("0"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão 0 na quarta linha, ocupando duas colunas.
botao_0.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)

# Cria o botão da vírgula decimal.
botao_decimal = tk.Button(janela, text=",", width= 6, command= decimal, bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão decimal na quarta linha e terceira coluna.
botao_decimal.grid(row=4, column=2, sticky="nsew", padx=4, pady=4)

# Cria o botão de igual e associa a função responsável pelos cálculos.
botao_igual = tk.Button(janela, text="=", width=6, command=calcular, bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão de igual na quarta coluna, ocupando duas linhas.
botao_igual.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=4, pady=4)

# QUINTA LINHA DA CALCULADORA

# Cria o botão de adição e associa a operação matemática +.
botao_somar = tk.Button(janela, text="+", width=6, command=lambda: selecionar_operacao("+"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão de adição na quinta linha e terceira coluna.
botao_somar.grid(row= 5,column=2, sticky="nsew", padx=4, pady=4)

# Cria o botão C, responsável por limpar a calculadora.
botao_c = tk.Button(janela, text="C" , width=6, command = limpar, bg="#505050", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão C na quinta linha e primeira coluna.
botao_c.grid(row=5, column=0, sticky="nsew", padx=4, pady=4)

# Cria o botão de apagar o último caractere digitado.
botao_apagar = tk.Button(janela, text= "⌫", width= 6, command= apagar_ultimo, bg="#505050", fg="white", font=("Arial", 16, "bold"), bd=0)
# Posiciona o botão de apagar na quinta linha e segunda coluna.
botao_apagar.grid(row=5, column=1, sticky="nsew", padx=4, pady=4)

# BOTÕES NUMÉRICOS

# Inicia uma repetição para percorrer todos os botões numéricos.
for botao in [
    # Adiciona os botões de 0 a 3 à lista.
    botao_0, botao_1, botao_2, botao_3,
    # Adiciona os botões de 4 a 7 à lista.
    botao_4, botao_5, botao_6, botao_7,
    # Adiciona os botões 8 e 9 à lista.
    botao_8, botao_9
]:
    # Aplica o efeito de mudança de cor aos botões numéricos.
    adicionar_efeito(botao, "#303030", "#454545")

# OPERAÇÕES

# Inicia uma repetição para percorrer os botões de operações matemáticas.
for botao in [
    # Adiciona os botões de adição e subtração à lista.
    botao_somar, botao_subtrair,
    # Adiciona os botões de multiplicação e divisão à lista.
    botao_multiplicar, botao_dividir
]:
    # Aplica o efeito de mudança de cor aos botões de operações.
    adicionar_efeito(botao, "#FF9500", "#E08300")

# BOTÃO C

# Aplica o efeito de mudança de cor ao botão C.
adicionar_efeito(botao_c, "#505050", "#686868")

# BOTÃO DE APAGAR

# Aplica o efeito de mudança de cor ao botão de apagar.
adicionar_efeito(botao_apagar, "#505050", "#686868")

# BOTÃO DE IGUAL

# Aplica o efeito de mudança de cor ao botão de igual.
adicionar_efeito(botao_igual, "#FF9500", "#E08300")

# Mantém a janela aberta e permite que a calculadora receba interações.
janela.mainloop()