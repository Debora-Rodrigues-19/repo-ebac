# código de geração do gráfico
import pandas as pd
dado = pd.read_csv ('gasolina.csv')

grafico = dado.plot.line(x='dia', y='venda', xlabel='Dia', ylabel='Venda', title='Preço médio da gasolina na cidade de São Paulo, 10 primeiros dias, Jul/21')

figura = grafico.get_figure()
figura.savefig('grafico_gasolina.png')
