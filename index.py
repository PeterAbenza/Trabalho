produtos = {
    1: {"nome": "Maçã", "preco": 2.3},
    2: {"nome": "Laranja", "preco": 3.6},
    3: {"nome": "Banana", "preco": 1.85},
}

def processar_compra(produto, qnt):
    nome = produtos[produto]["nome"];
    preco = produtos[produto]["preco"];
    total = qnt * preco;
    print(f"Você comprou {qnt} {nome}(s), e o valor total é: R$ {total:.2f}");

cancelar = False;

while not cancelar:
    print("Menu de compras, selecione qual item deseja.");
    for codigo, info in produtos.items(): 
        print(f"{codigo} - {info['nome']} (R$ {info['preco']:.2f})")
    
    try:
        produto = int(input("\nDigite o número do produto que deseja: "));

        if produto not in produtos:
            print("Você selecionou um item fora de estoque!\n")
            continue

        qnt = int(input("Quantas unidades? "))
        processar_compra(produto, qnt)

        cancelarCompra = input("\nDeseja continuar? (S/N): ").strip().lower()
        if cancelarCompra not in ["s", "sim"]:
            print("Obrigado pela compra!")
            cancelar = True
    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")