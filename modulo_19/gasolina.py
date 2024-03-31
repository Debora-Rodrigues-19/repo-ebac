import pandas as pd
dado = pd.read_csv ('gasolina.csv')

grafico = dado.plot.line(color='green', x='dia', y='venda', xlabel='Dia', ylabel='Vendas', title='Preço médio da gasolina na cidade de SP, 10 primeiros dias, Jul/21')

figura = grafico.get_figure()
figura.savefig('grafico_gasolina.png')
