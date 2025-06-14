# código de geração do gráfico 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha usando Seaborn
plt.figure(figsize=(12, 7)) 
sns.lineplot(x='dia', y='venda', data=df, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Preço por Dia')

# Adicionar título e subtítulo
plt.title('Variação Diária do Preço de Venda da Gasolina', fontsize=18, fontweight='bold', color='#333333')
plt.suptitle('Período de 10 Dias (Dados Fictícios)', fontsize=12, color='#666666', y=0.92)

# Adicionar rótulos aos eixos com maior clareza
plt.xlabel('Dia do Mês', fontsize=14, color='#333333')
plt.ylabel('Preço de Venda (R$)', fontsize=14, color='#333333')

# Adicionar marcadores de ticks nos eixos
plt.xticks(df['dia'], fontsize=10)
plt.yticks(fontsize=10)

# Adicionar grade para melhor legibilidade
plt.grid(True, linestyle='--', alpha=0.7)

# Adicionar legenda (útil se houvesse múltiplas linhas)
plt.legend(title='Tipo de Dado', loc='best', fontsize=10)

# Remover a moldura superior e direita para um visual mais limpo
sns.despine()

# Salvar o gráfico em um arquivo PNG com alta resolução
plt.savefig('gasolina.png', dpi=300, bbox_inches='tight')

plt.show()