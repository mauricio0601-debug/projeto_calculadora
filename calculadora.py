import tkinter as tk

def digitar(numero):
    global novo_calculo
    if novo_calculo:
        visor.delete(0, tk.END)
        novo_calculo = False

    if visor.get() == "Por favor, digite o primeiro número":
        visor.delete(0, tk.END)

    elif visor.get() == "Digite o segundo número":
        visor.delete(0, tk.END)
    elif visor.get() == "ERRO: divisão por zero":
        visor.delete(0, tk.END)

    visor.insert(tk.END, numero)
def limpar():
    global numero1, operacao, novo_calculo
    novo_calculo = False

    visor.delete(0 , tk.END)
    numero1=None
    operacao=None

#operações, variaveis e tratamentos
numero1 = None
operacao = None
mensagem_erro = "Por favor, digite o primeiro número"
novo_calculo = False

def selecionar_operacao(simbolo):
    global numero1, operacao, novo_calculo

    texto = visor.get()

    # Se houver uma mensagem de erro, limpa os dados
    if texto in (mensagem_erro, "Digite o segundo número", "ERRO: divisão por zero"):
        visor.delete(0, tk.END)
        numero1 = None
        operacao = None
        novo_calculo = False
        return

    # Se o visor estiver vazio, não seleciona operação
    if texto == "":
        return

    # Armazena o primeiro número e a operação
    numero1 = float(texto.replace(",", "."))
    operacao = simbolo
    novo_calculo = False

    visor.delete(0, tk.END)

def calcular():
    global numero1, operacao, novo_calculo

    if visor.get() == "Digite o segundo número":
        return

    if visor.get() == "" and operacao is None:
        return

    if operacao is None:
        return

    if visor.get() == "" and operacao is not None:
        visor.insert(tk.END, "Digite o segundo número")
        return

    numero2 = float(visor.get().replace(",", "."))

    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "x":
        resultado = numero1 * numero2

    elif operacao == "÷":
        if numero2 == 0:
            visor.delete(0, tk.END)
            visor.insert(tk.END, "ERRO: divisão por zero")

            numero1 = None
            operacao = None
            novo_calculo = True
            return

        resultado = numero1 / numero2

    numero1 = resultado
    operacao = None

    visor.delete(0, tk.END)
    resultado_formatado = f"{resultado:.8f}".rstrip("0").rstrip(".")
    visor.insert(tk.END, resultado_formatado.replace(".", ","))
    
    novo_calculo = True
    
def apagar_ultimo():
    texto = visor.get()

    if texto in (mensagem_erro, "Digite o segundo número", "ERRO: divisão por zero"):
        return

    if texto != "":
        visor.delete(len(texto) - 1, tk.END)

def decimal():
    global novo_calculo

    texto = visor.get()

    if novo_calculo:
        visor.delete(0, tk.END)
        novo_calculo = False
        visor.insert(tk.END, "0,")
        return

    if texto == "":
        visor.insert(tk.END, "0,")
        return

    if texto in (mensagem_erro, "Digite o segundo número", "ERRO: divisão por zero"):
        return

    if "," not in texto:
        visor.insert(tk.END, ",") 

def validar_entrada(texto):
    if texto == "":
        return True

    if texto in (
        mensagem_erro,
        "Digite o segundo número",
        "ERRO: divisão por zero"
    ):
        return True

    if texto.count(",") > 1:
        return False

    return texto.replace(",", "").isdigit()

def adicionar_efeito(botao, cor_original, cor_hover):
    botao.bind(
        "<Enter>",
        lambda evento: botao.config(bg=cor_hover)
    )

    botao.bind(
        "<Leave>",
        lambda evento: botao.config(bg=cor_original)
    )

#interface da calculadora
janela = tk.Tk()

janela.title("Teclado da Calculadora")

janela.configure(bg="#121212")
janela.resizable(False, False)

# Configuração das 4 colunas
for coluna in range(4):
    janela.grid_columnconfigure(coluna, weight=1)

# Configuração das 5 linhas dos botões
for linha in range(1, 6):
    janela.grid_rowconfigure(linha, weight=1)

validacao = janela.register(validar_entrada)

visor = tk.Entry( janela, width=18, justify="right", font=("Arial", 22), bg="#1E1E1E", fg="white", insertbackground="white", bd=0, highlightthickness=0, validate="key", validatecommand=(validacao, "%P"))
visor.grid(row=0, column=0, columnspan=4, padx=8, pady=12, ipady=15, sticky="nsew")

#primeira linha da calculadora

botao_7 = tk.Button(janela, text="7" , width=6, command= lambda: digitar("7"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_7.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)

botao_8 = tk.Button(janela, text="8" , width=6, command= lambda: digitar("8"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_8.grid(row=1, column=1, sticky="nsew", padx=4, pady=4)

botao_9 = tk.Button(janela, text="9" , width=6, command= lambda: digitar("9"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_9.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)

botao_subtrair = tk.Button(janela, text="-", width=6, command=lambda: selecionar_operacao("-"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_subtrair.grid(row= 1,column=3, sticky="nsew", padx=4, pady=4)

#segunda linha da calculadora

botao_4 = tk.Button(janela, text="4" , width=6, command= lambda: digitar("4"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_4.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)

botao_5 = tk.Button(janela, text="5" , width=6, command= lambda: digitar("5"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_5.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)

botao_6 = tk.Button(janela, text="6" , width=6, command= lambda: digitar("6"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_6.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)

botao_multiplicar = tk.Button(janela, text="x", width=6, command=lambda: selecionar_operacao("x"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_multiplicar.grid(row= 2,column=3, sticky="nsew", padx=4, pady=4)

#terceira linha da calculadora

botao_1 = tk.Button(janela, text="1" , width=6, command= lambda: digitar("1"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_1.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)

botao_2 = tk.Button(janela, text="2" , width=6, command= lambda: digitar("2"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_2.grid(row=3, column=1, sticky="nsew", padx=4, pady=4)

botao_3 = tk.Button(janela, text="3" , width=6, command= lambda: digitar("3"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_3.grid(row=3, column=2, sticky="nsew", padx=4, pady=4)

botao_dividir = tk.Button(janela, text="÷", width=6, command=lambda: selecionar_operacao("÷"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_dividir.grid(row= 3,column=3, sticky="nsew", padx=4, pady=4)

#quarta linha da calculadora

botao_0 = tk.Button(janela, text="0" , width=6, command= lambda: digitar("0"), bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_0.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)

botao_decimal = tk.Button(janela, text=",", width= 6, command= decimal, bg="#303030", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_decimal.grid(row=4, column=2, sticky="nsew", padx=4, pady=4)

botao_igual = tk.Button(janela, text="=", width=6, command=calcular, bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_igual.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=4, pady=4)

#quinta linha da calculadora

botao_somar = tk.Button(janela, text="+", width=6, command=lambda: selecionar_operacao("+"), bg="#FF9500", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_somar.grid(row= 5,column=2, sticky="nsew", padx=4, pady=4)

botao_c = tk.Button(janela, text="C" , width=6, command = limpar, bg="#505050", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_c.grid(row=5, column=0, sticky="nsew", padx=4, pady=4)

botao_apagar = tk.Button(janela, text= "⌫", width= 6, command= apagar_ultimo, bg="#505050", fg="white", font=("Arial", 16, "bold"), bd=0)
botao_apagar.grid(row=5, column=1, sticky="nsew", padx=4, pady=4)

# Botões numéricos
for botao in [
    botao_0, botao_1, botao_2, botao_3,
    botao_4, botao_5, botao_6, botao_7,
    botao_8, botao_9
]:
    adicionar_efeito(botao, "#303030", "#454545")

# Operações
for botao in [
    botao_somar, botao_subtrair,
    botao_multiplicar, botao_dividir
]:
    adicionar_efeito(botao, "#FF9500", "#E08300")

# Botão C
adicionar_efeito(botao_c, "#505050", "#686868")

# Botão de apagar
adicionar_efeito(botao_apagar, "#505050", "#686868")

# Botão de igual
adicionar_efeito(botao_igual, "#FF9500", "#E08300")

janela.mainloop()