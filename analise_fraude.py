# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o arquivo CSV com os dados de transações fraudulentas
df = pd.read_csv('Fraudulent_E-Commerce_Transaction_Data_2.csv')

# Verificar as primeiras linhas para ter uma ideia do conteúdo
print(df.head())

# 2. Análises focadas no tema de fraudes em idosos

# Fraudes por faixa etária - foco em idosos (acima de 50 anos)
age_above_50 = df[df['Customer Age'] > 50]
age_above_50_fraud = age_above_50.groupby('Customer Age')['Is Fraudulent'].mean().reset_index()

# Gráfico: Percentual de fraudes por idade acima de 50 anos
plt.figure(figsize=(10,6))
plt.plot(age_above_50_fraud['Customer Age'], age_above_50_fraud['Is Fraudulent']*100, color='green', marker='o')
plt.title('Percentual de Fraudes por Idade Acima de 50 Anos')
plt.xlabel('Idade do Cliente')
plt.ylabel('Percentual de Fraude (%)')
plt.grid(True)
plt.show()

# 3. Média de valor das transações fraudulentas por faixa etária
age_transaction_value = df[df['Is Fraudulent'] == 1].groupby('Customer Age')['Transaction Amount'].mean().reset_index()

# Gráfico: Valor médio das transações fraudulentas por idade
plt.figure(figsize=(10,6))
plt.plot(age_transaction_value['Customer Age'], age_transaction_value['Transaction Amount'], color='purple', marker='o')
plt.title('Valor Médio das Transações Fraudulentas por Idade')
plt.xlabel('Idade do Cliente')
plt.ylabel('Valor Médio da Transação (USD)')
plt.grid(True)
plt.show()

# 4. Fraudes por dispositivo utilizado por idosos (clientes acima de 50 anos)
device_fraud = age_above_50.groupby('Device Used')['Is Fraudulent'].mean().reset_index()

# Gráfico: Percentual de fraudes por dispositivo para idosos
plt.figure(figsize=(10,6))
plt.bar(device_fraud['Device Used'], device_fraud['Is Fraudulent']*100, color='red')
plt.title('Percentual de Fraudes por Dispositivo (Clientes Acima de 50 Anos)')
plt.xlabel('Dispositivo Utilizado')
plt.ylabel('Percentual de Fraude (%)')
plt.show()

# 5. Fraudes por localização para clientes idosos (50+ anos)
location_fraud = age_above_50.groupby('Customer Location')['Is Fraudulent'].mean().reset_index()

# Exibir as localizações com maiores taxas de fraude (Top 10)
location_fraud_sorted = location_fraud.sort_values(by='Is Fraudulent', ascending=False).head(10)
print("Top 10 Localizações com maiores fraudes para clientes idosos:")
print(location_fraud_sorted)

# 6. Distribuição dos valores das transações fraudulentas para clientes acima de 50 anos
plt.figure(figsize=(10,6))
plt.hist(age_above_50[age_above_50['Is Fraudulent'] == 1]['Transaction Amount'], bins=30, color='blue', edgecolor='black')
plt.title('Distribuição de Valores das Transações Fraudulentas (Clientes Acima de 50 Anos)')
plt.xlabel('Valor da Transação (USD)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# 7. Comparação de fraudes entre clientes acima e abaixo de 50 anos
below_50 = df[df['Customer Age'] <= 50].groupby('Customer Age')['Is Fraudulent'].mean().reset_index()
above_50 = df[df['Customer Age'] > 50].groupby('Customer Age')['Is Fraudulent'].mean().reset_index()

# Gráfico: Comparação de fraudes entre faixas etárias
plt.figure(figsize=(10,6))
plt.plot(below_50['Customer Age'], below_50['Is Fraudulent']*100, color='blue', label='Clientes ≤ 50 anos', marker='o')
plt.plot(above_50['Customer Age'], above_50['Is Fraudulent']*100, color='green', label='Clientes > 50 anos', marker='o')
plt.title('Comparação de Fraudes por Idade (Clientes ≤ 50 e > 50)')
plt.xlabel('Idade do Cliente')
plt.ylabel('Percentual de Fraude (%)')
plt.legend()
plt.grid(True)
plt.show()

# 8. Percentual de fraudes por hora do dia
hour_fraud = df.groupby('Transaction Hour')['Is Fraudulent'].mean().reset_index()

# Gráfico: Percentual de fraudes por hora do dia
plt.figure(figsize=(10,6))
plt.plot(hour_fraud['Transaction Hour'], hour_fraud['Is Fraudulent']*100, color='orange', marker='o')
plt.title('Percentual de Fraudes por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Percentual de Fraude (%)')
plt.grid(True)
plt.show()

# 9. Exportar tabelas consolidadas para Excel
age_above_50_fraud.to_excel('tabela_fraude_idade_acima_50.xlsx', index=False)
age_transaction_value.to_excel('tabela_valor_fraude_idade.xlsx', index=False)
device_fraud.to_excel('tabela_fraude_dispositivo_idosos.xlsx', index=False)
location_fraud_sorted.to_excel('tabela_fraude_localizacao_idosos.xlsx', index=False)
hour_fraud.to_excel('tabela_fraude_hora_do_dia.xlsx', index=False)
