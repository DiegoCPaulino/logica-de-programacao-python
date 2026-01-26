preco_produto = float(input("Digite o preço do produto: R$ "))

opcao1 = preco_produto * 0.90
opcao2 = preco_produto * 0.95
opcao3 = (preco_produto * 1.04) / 2
opcao4 = (preco_produto * 1.08) / 3

print(f"• Opção 1 - À vista em dinheiro ou pix, recebe 10% de desconto: R$ {opcao1:.2f}"
      f"\n• Opção 2 - À vista no débito, recebe 5% de desconto: R$ {opcao2:.2f}"
      f"\n• Opção 3 - Em duas vezes, juros de 4%: 2x de R$ {opcao3:.2f} (Total: R$ {opcao3*2:.2f})"
      f"\n• Opção 4 - Em três vezes, juros de 8%: 3x de R$ {opcao4:.2f} (Total: R$ {opcao4*3:.2f})")