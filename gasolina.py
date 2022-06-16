import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço por dia', xlabel='Dia', ylabel='Preço médio de venda(reais)');
  fig = grafico.get_figure()
  fig.savefig('gasolina.png')