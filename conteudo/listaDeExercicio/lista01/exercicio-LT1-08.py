preco = float(input('Digite o valor do produto: '));
percentual = float(input('Digite o percentual de desconto ou aumento (sem o %): '));

print(f'Valor original: R$ {preco: .2f}');
print(f'Percentual: {percentual: .2f}%');
print(f'Produto com desconto: R$ {preco - (preco * percentual / 100): .2f}');
print(f'Produto com aumento: R$ {preco + (preco * percentual / 100): .2f}');