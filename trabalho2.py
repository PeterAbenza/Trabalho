valor_total = 0;
menu = {
        'P': {'PS': 30.00, 'PD': 34.00},
        'M': {'PS': 45.00, 'PD': 48.00},
        'G': {'PS': 60.00, 'PD': 66.00}
    };

def mostrar_menu():
    print("-" * 56)
    print("{:^56}".format("Bem-Vindo à Pizzaria de Pedro Abenza"))
    print("-" * 56);
    print("{:^55}".format("Cardápio"))
    print("-" * 56);
    print("---|" + "  Tamanho   |    Pizza Salgada   |  Pizza Doce  " + "|---");
    print("-" * 56);

    for tamanho, tipos in menu.items():
        print("---|" + "{:^12}".format(tamanho) + "|" + "{:^20}".format(tipos['PS']) + "|" 
              + "{:^14}".format(tipos['PD']) + "|---");


while True:
    mostrar_menu()

    tipo = input("\nEscolha o tipo de pizza (PS para Salgada, PD para Doce): ").upper();
    tamanho = input("Escolha o tamanho da pizza (P/M/G): ").upper();
    
    if tamanho in menu and tipo in menu[tamanho]:
        valor_total += menu[tamanho][tipo];
        print(f"Você escolheu uma pizza {tipo} de tamanho {tamanho}. O preço atual é R$ {valor_total:.2f}");

        continuar = input("\nDeseja mais alguma coisa? (S/N)").upper(); 

        if continuar == "S":
           continue  # Continua o loop
        elif continuar == "N":
           print(f"Obrigado! O valor total da sua compra foi: R$ {valor_total:.2f}")
           break  # Sai do loop
        else:
           print("Opção inválida. Encerrando.")
        break  # Encerra caso de resposta inválida
    else:
        print("Opção inválida. Tente novamente.\n");
        continue