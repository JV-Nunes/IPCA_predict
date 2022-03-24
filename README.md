# IPCA_predict
Data scraping and IPCA forecast model


## Instalação
Para executar os códigos, deve-se executar o comando em um terminal em seu ambiente de desenvolvimento:

    pip install requirements.txt

## Execução

O projeto está dividido em dois diretórios principais: *getters* e *model*

> *getters*: 
 
-Responsável por executar todo o funcionamento do web scraping (aquisição dos dados via web)  

> *model*:

-Responsável pelo tratamento dos dados e construção do modelo preditivo. 


Para a captação inicial dos dados, deve-se executar o arquivo getters/get_data.py a partir de um terminal com o comando:

    python get_data.py

IMPORTANTE: é imprescindível alterar o modo de importação do arquivo url_dict.py a partir do arquivo get_data.py, quando se executa o get_data.py como main a partir do terminal. A forma de importação correta está definida no início do arquivo, comentada.

## Embasamento

Esta modelagem utiliza de uma análise de série temporal, com variáveis independentes de importante peso macroeconômico sendo elas:
-Variação mensal do IPCA
-Taxa Meta Selic
-Taxa Selic a.a
-Variação Mensal Selic
-Expectativa Média da Inflação

Todas as variáveis foram coletadas a partir das instituições públicas que divulgam estes dados, e as fontes estão disponibilizadas no arquivo url_dict.py

### Modelagem
Foi utilizado um modelo de regressão, tendo como variável dependente a ser prevista o IPCA com base em 1991. O modelo utilizado foi o XGBoost,  modelo de Machine Learning que utiliza uma combinação de técnicas computacionais como Gradient Descend e Random Forests, incluindo em sua execução uma forte otimização de hardware.