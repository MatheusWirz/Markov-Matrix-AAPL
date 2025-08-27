# Análise de Cadeias de Markov para Retornos de Ações

## Descrição do Projeto

Este projeto em Python analisa o comportamento histórico dos retornos diários de uma ação para modelar as suas transições de estado (dia de alta vs. dia de baixa) usando uma Cadeia de Markov de primeira ordem. O objetivo é calcular a matriz de transição, que nos dá a probabilidade condicional de um dia ser positivo ou negativo, dado o resultado do dia anterior.

Esta é uma análise fundamental em finanças quantitativas para estudar a "memória" de curto prazo de um ativo financeiro.

## Tecnologias Utilizadas

* **Python**
* **Pandas:** Para manipulação e análise de dados.
* **NumPy:** Para cálculos numéricos eficientes.
* **yfinance:** Para baixar os dados históricos de preços das ações do Yahoo Finance.

## Exemplo de Saída

Ao analisar o ticker `AAPL`, o programa gera as seguintes matrizes:

**Matriz de Contagem de Transições**
(Linhas = Estado de Ontem, Colunas = Estado de Hoje)

| Estado | Negativo | Positivo |
| :--- | :---: | :---: |
| **Estado_Anterior** | | |
| **Negativo** | 55 | 66 |
| **Positivo** | 59 | 69 |


**Matriz de Transição de Markov (Probabilidades)**
(Probabilidade de ir do estado da Linha para o estado da Coluna)

| Estado | Negativo | Positivo |
| :--- | :---: | :---: |
| **Estado_Anterior** | | |
| **Negativo** | 45.45% | 54.55% |
| **Positivo** | 46.46% | 53.54% |
