import pandas as pd
import matplotlib.pyplot as plt

# Carregamento dos dados
# Certifique-se de que o nome do arquivo Excel esteja correto
df = pd.read_excel("importacoes_ficticias_2 (2).xlsx", engine="openpyxl")

# KPIs
total = df["Valor_USD"].sum()

# Agrupamento por país
por_pais = df.groupby("Pais")["Valor_USD"].sum().sort_values(ascending=False)

# Configuração de estilo
plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))

# Definição de cores (destacando a maior barra)
cores = ["#4CAF50"] + ["#A5D6A7"] * (len(por_pais) - 1)

# Criação do gráfico de barras
bars = ax.bar(por_pais.index, por_pais.values, color=cores)

# Título e subtítulo
ax.set_title("Importação por País", fontsize=16, fontweight="bold")
plt.suptitle(f"Total importado: ${total:,.0f}".replace(",", "."), fontsize=10, y=0.93)

# Limpeza do layout (remover bordas desnecessárias)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Rotação dos nomes dos países
plt.xticks(rotation=30, ha='right')

# Adição de labels nas barras (valores e percentuais)
for i, v in enumerate(por_pais):
    perc = v / total * 100
    ax.text(
        i, v,
        f"${v:,.0f}\n({perc:.1f}%)".replace(",", "."),
        ha='center',
        va='bottom',
        fontsize=9
    )

# Ajustes finais de eixos
ax.set_ylabel("Valor (USD)")
ax.set_xlabel("")

plt.tight_layout()
plt.show()
