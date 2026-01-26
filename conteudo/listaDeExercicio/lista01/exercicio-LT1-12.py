nac = float(input("Digite a nota da NAC: "));
am = float(input("Digite a nota da AM: "));
ps = float(input("Digite a nota da PS: "));

nota_final = (nac * 2 + am * 3 + ps * 5) / 10;

print(f"A nota final é: {nota_final: .1f}");