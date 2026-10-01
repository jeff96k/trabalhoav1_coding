def calcular_subtotal(item):
    return item["preco"] * item["quantidade"]


def calcular_total(itens):
    total = sum(calcular_subtotal(item) for item in itens)
    return aplicar_desconto(total)


def aplicar_desconto(total):
    return total * 0.9 if total > 500 else total


def imprimir_cabecalho(pedido):
    print("=== PEDIDO ===")
    print(f"Cliente: {pedido['cliente']}")


def imprimir_itens(itens):
    for item in itens:
        print(f"{item['nome']} x{item['quantidade']}: R$ {calcular_subtotal(item):.2f}")


def imprimir_pedido(pedido):
    imprimir_cabecalho(pedido)
    imprimir_itens(pedido["itens"])
    print(f"Total: R$ {calcular_total(pedido['itens']):.2f}")


if __name__ == "__main__":
    pedido = {
        "cliente": "Ana",
        "itens": [
            {"nome": "Teclado", "preco": 250.0, "quantidade": 2},
            {"nome": "Mouse", "preco": 80.0, "quantidade": 1},
        ],
    }
    imprimir_pedido(pedido)
