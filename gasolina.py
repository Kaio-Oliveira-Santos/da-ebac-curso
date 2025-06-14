import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha usando Seaborn
plt.figure(figsize=(10, 6)) 
sns.lineplot(x='dia', y='venda', data=df, marker='o', linestyle='-', color='blue')

# Adicionar título e rótulos aos eixos
plt.title('Preço da Gasolina por Dia', fontsize=16)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)

# Adicionar grade para melhor visualização
plt.grid(True)

# Salvar o gráfico em um arquivo PNG
plt.savefig('gasolina.png')

plt.show()