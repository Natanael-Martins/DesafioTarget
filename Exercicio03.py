import json

with open('faturamento.json') as file:
    faturamento = json.load(file)

# Calcula o menor e maior valor de faturamento
min_faturamento = min(faturamento)
max_faturamento = max(faturamento)

# Calcula a média de faturamento (ignorando dias sem faturamento)
dias_com_faturamento = [f for f in faturamento if f > 0]
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_faturamento)

print(f"Menor faturamento diário: {min_faturamento}")
print(f"Maior faturamento diário: {max_faturamento}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")