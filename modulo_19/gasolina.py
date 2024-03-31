# código de geração do gráfico
import pandas as pd
dado = pd.read_csv ('gasolina.csv')

grafico = dado.plot.line(x='dia', y='venda', xlabel='Dia', ylabel='Venda', title='Gráfico de Vendas de Gasolina, por dia')

figura = grafico.get_figure()
figura.savefig('grafico_gasolina.png')
