def mostrar_menu():
    print("Entre com o Tipo de Madeira desejado")
    print("PIN - Tora de Pinho")
    print("PER - Tora de Peroba")
    print("MOG - Tora de Mogno")
    print("IPE - Tora de Ipê")
    print("IMB - Tora de Imbuia")

def escolha_tipo():
    mostrar_menu()
    precos = {
        "PIN": 150.40,  # Tora de Pinho
        "PER": 170.20,  # Tora de Peroba
        "MOG": 190.90,  # Tora de Mogno
        "IPE": 210.10,  # Tora de Ipê
        "IMB": 220.70   # Tora de Imbuia
    }

    while True:
        tipo = input(">>>").upper()

        if tipo in precos:
            return tipo, precos[tipo]  # Retorna tipo e preço corretamente
        else:
            print("Opção inválida. Tente novamente.")
            continue

def qtd_toras():
    while True:
        try:
            quantidade_toras = float(input("Entre com a quantidade de toras (m³): "))
            
            if quantidade_toras < 100:
                desconto = 0
            elif 100 <= quantidade_toras < 500:
                desconto = 0.04
            elif 500 <= quantidade_toras < 1000:
                desconto = 0.09
            elif 1000 <= quantidade_toras <= 2000:
                desconto = 0.16
            else:
                print("Não aceitamos pedidos com mais de 2000 m³ de toras.")
                continue  # Volta para pedir a quantidade novamente

            return quantidade_toras, desconto  # Retorna a quantidade e o desconto
        except ValueError:
            print("Valor inválido. Por favor, entre com um número válido.")

def transporte():
    while True:
        print("\nEscolha o tipo de transporte:")
        print("1 - Rodoviário (R$ 1000,00)")
        print("2 - Ferroviário (R$ 2000,00)")
        print("3 - Hidroviário (R$ 2500,00)")

        tipo_transporte = input("Escolha o tipo de transporte (1, 2, 3): ")

        if tipo_transporte == "1":
            return 1000
        elif tipo_transporte == "2":
            return 2000
        elif tipo_transporte == "3":
            return 2500
        else:
            print("Opção inválida. Tente novamente.")

def main():
    print("\nBem-vindo à Madeireira do Lenhador Pedro Abenza")

    # Escolhe o tipo de madeira e retorna o tipo e o preço
    tipo, preco_m3 = escolha_tipo()

    # Obtém a quantidade de toras e o desconto
    quantidade_toras, desconto = qtd_toras()

    # Escolhe o tipo de transporte e o valor extra
    custo_transporte = transporte()

    # Calcula o valor total
    total = ((preco_m3 * quantidade_toras) * (1 - desconto)) + custo_transporte

    print(f"Total a pagar: R${total:.2f}")

main()
