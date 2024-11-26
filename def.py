def borda(text):
    formado = len(text);

    if formado:
        print("+", "-" * formado, "+");
        print("|", text, "|");
        print("+", "-" * formado, "+");


borda("viado");