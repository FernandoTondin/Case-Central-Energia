import pandas as pd
import matplotlib.pyplot as plt


#--------------------------------------------------------
#plotar o custo das usinas à oleo pelo cotação do dolar
#--------------------------------------------------------
df = pd.read_csv('custo-usina-4-OleoXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Oleo-4-custoXdolar.png')

df = pd.read_csv('custo-usina-170-OleoXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Oleo-170-custoXdolar.png')

df = pd.read_csv('custo-usina-194-OleoXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Oleo-194-custoXdolar.png')

#plotar o custo das usinas à oleo pelo preço do petróleo

df = pd.read_csv('custo-usina-4-OleoXpetroleo.csv',sep=',')
print(df)
df.plot(x="petroleo", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Oleo-4-custoXpetroleo.png')

df = pd.read_csv('custo-usina-170-OleoXpetroleo.csv',sep=',')
print(df)
df.plot(x="petroleo", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Oleo-170-custoXpetroleo.png')

df = pd.read_csv('custo-usina-194-OleoXpetroleo.csv',sep=',')
print(df)
df.plot(x="petroleo", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Oleo-194-custoXpetroleo.png')

#--------------------------------------------------------
#plotar o custo das usinas à gas pelo cotação do dolar
#--------------------------------------------------------

df = pd.read_csv('custo-usina-47-GasXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Gas-47-custoXdolar.png')

df = pd.read_csv('custo-usina-90-GasXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Gas-90-custoXdolar.png')

df = pd.read_csv('custo-usina-137-GasXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Gas-137-custoXdolar.png')

#plotar o custo das usinas à gas pelo preço do gas natural

df = pd.read_csv('custo-usina-47-GasXgas-natural.csv',sep=',')
print(df)
df.plot(x="gas", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Gas-47-custoXgas-natural.png')

df = pd.read_csv('custo-usina-90-GasXgas-natural.csv',sep=',')
print(df)
df.plot(x="gas", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Gas-90-custoXgas-natural.png')

df = pd.read_csv('custo-usina-137-GasXgas-natural.csv',sep=',')
print(df)
df.plot(x="gas", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Gas-137-custoXgas-natural.png')

#--------------------------------------------------------
#plotar o custo das usinas à carvão pelo cotação do dolar
#--------------------------------------------------------

df = pd.read_csv('custo-usina-24-CarvaoXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Carvao-24-custoXdolar.png')

df = pd.read_csv('custo-usina-163-CarvaoXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Carvao-163-custoXdolar.png')

df = pd.read_csv('custo-usina-167-CarvaoXdolar.csv',sep=',')
print(df)
df.plot(x="dolar", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Carvao-167-custoXdolar.png')

#plotar o custo das usinas à carvão pelo preço do carvão mineral

df = pd.read_csv('custo-usina-24-CarvaoXcarvao-mineral.csv',sep=',')
print(df)
df.plot(x="carvao", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Carvao-24-custoXdolar.png')

df = pd.read_csv('custo-usina-163-CarvaoXcarvao-mineral.csv',sep=',')
print(df)
df.plot(x="carvao", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Carvao-163-custoXdolar.png')

df = pd.read_csv('custo-usina-167-CarvaoXcarvao-mineral.csv',sep=',')
print(df)
df.plot(x="carvao", y="custo1",kind="scatter")
plt.savefig('plot-custo-usina-Carvao-167-custoXdolar.png')