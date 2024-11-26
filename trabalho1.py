def calcularMensalidade():
    print("\nBem vindo ao Sistema de Pedro Gabriel Pasqualim Abenza");

    valor_base = float(input("Informe o valor base do plano: R$ "))
    idade_base = int(input("Informe a idade do cliente: "))
        
    # Evitar valores negativos
    if valor_base <= 0 or idade_base < 0:
        print("Por favor, insira valores positivos para o valor e a idade.")
        return

    # Percentual com base na faixa etária
    if(0 <= idade_base < 19):
        percentual = 100
    elif(19 <= idade_base < 29):
        percentual = 150
    elif(29 <= idade_base < 39):
        percentual = 225
    elif(39 <= idade_base < 49):
        percentual = 240
    elif(49 <= idade_base < 59):
        percentual = 350
    elif(59 <= idade_base):
        percentual = 600
    else:
        percentual = 0

    # Calculo do valor mensal
    valor_mensal =  valor_base * (percentual / 100)

    print(f"O valor mensal para idade {idade_base} é: R${valor_mensal:.2f}");


calcularMensalidade();