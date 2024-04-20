# Previsao-de-Vendas
# Problema: Previsão de Vendas Futuras
|
|
|
|
|
# Descrição: Utilizando os dados históricos de vendas de varejo, desenvolva um modelo de previsão de vendas para prever as vendas futuras da empresa. Isso pode ajudar a empresa a planejar seus estoques, otimizar sua produção e gerenciar melhor suas operações.

## Através de uma planilha retirada da internet, sobre as vendas de um mercado de varejo nos anos de 2010 e 2011, gostaria de prever as vendas de janeiro de 2012.
![image](https://github.com/brunogboy/Previsao-de-Vendas/assets/165103663/c65cc6f2-2049-478a-80ca-fd4bec01661e)

 Antes de tudo, precisei transformar a coluna aonde está a data, em datetime, para assim começar os trabalhos.
## Dados transformados, puxei o metódo .describe() para podermos analisar a média das vendas em 2011, a maior venda dentre os 12 meses.
![image](https://github.com/brunogboy/Previsao-de-Vendas/assets/165103663/9be825b5-c26e-4800-96b8-848a8dfce52b)

# A partir disso, transformei o índice em uma matriz de recursos (reshape) para a regressão linear e ajustei um modelo de regressão linear aos dados
# Logo em seguida, fiz a previsão para janeiro de 2012. Como mostra o gráfico abaixo:
![image](https://github.com/brunogboy/Previsao-de-Vendas/assets/165103663/e6052e8a-32d6-46d0-9eac-3ea7c27baf51)

# Resposta Final:
![image](https://github.com/brunogboy/Previsao-de-Vendas/assets/165103663/d8a3f705-9190-4c5b-aab0-5a90806eb4f7)
