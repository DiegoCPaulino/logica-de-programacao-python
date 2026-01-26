valor_avista = float(input("Digite o valor que deseja pagar a vista: "));
valor_parcelado = float(input("Digite o valor que deseja pagar a parcelado: "));

total_parcelado = valor_parcelado * 10;
desconto_percentual = ((total_parcelado - valor_avista) / total_parcelado) * 100;

print(f"O valor total do parcelamento é: R$ {total_parcelado: .2f}");