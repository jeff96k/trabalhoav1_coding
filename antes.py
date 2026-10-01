def imprimir_pedido(pedido):
    total = 0
    for item in pedido["itens"]:
        total += item["preco"] * item["quantidade"]
    if total > 500:
        total = total * 0.9

    print("=== PEDIDO ===")
    print(f"Cliente: {pedido['cliente']}")
    for item in pedido["itens"]:
        subtotal = item["preco"] * item["quantidade"]
        print(f"{item['nome']} x{item['quantidade']}: R$ {subtotal:.2f}")
    print(f"Total: R$ {total:.2f}")


if __name__ == "__main__":
    pedido = {
        "cliente": "Ana",
        "itens": [
            {"nome": "Teclado", "preco": 250.0, "quantidade": 2},
            {"nome": "Mouse", "preco": 80.0, "quantidade": 1},
        ],
    }
    imprimir_pedido(pedido)
