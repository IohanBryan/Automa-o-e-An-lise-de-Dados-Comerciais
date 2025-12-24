import pandas as pd
import os
import matplotlib.pyplot as plt


df = pd.read_excel("vendas.xlsx")
df["Total"] = df["Quantidade"] * df["Preço Unitário"]

total_por_produto = df.groupby("Produto")["Total"].sum().reset_index()
total_por_categoria = df.groupby("Categoria")["Total"].sum().reset_index()

os.makedirs("graficos", exist_ok=True)

plt.figure()
plt.bar(total_por_produto["Produto"], total_por_produto["Total"])
plt.title("Faturamento por Produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento")
plt.tight_layout()
plt.savefig("graficos/faturamento_por_produto.png")
plt.close()

plt.figure()
plt.bar(total_por_categoria["Categoria"], total_por_categoria["Total"])
plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento")
plt.tight_layout()
plt.savefig("graficos/faturamento_por_categoria.png")
plt.close()

plt.figure()
plt.hist(df["Total"], bins=5)
plt.title("Distribuição do Faturamento por Venda")
plt.xlabel("Valor da Venda")
plt.ylabel("Quantidade de Vendas")
plt.tight_layout()
plt.savefig("graficos/distribuicao_faturamento.png")
plt.close()

print("Gráficos salvos com sucesso!")
