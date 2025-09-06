# Análise de Partidas de Futebol

Este relatório apresenta a análise de partidas de futebol com base nos dados fornecidos no arquivo `BRA.csv` e utilizando o script de análise. O objetivo é fornecer insights sobre o desempenho de times em confrontos diretos.

## Metodologia

Foi utilizado o arquivo `BRA.csv` contendo dados de partidas do futebol brasileiro. O script `Script_Analise_Futebol.txt` foi adaptado para um script Python (`analyze_brazil_data.py`) que realiza as seguintes etapas:

1.  Carregamento dos dados do CSV.
2.  Limpeza dos dados, removendo linhas com valores ausentes nas colunas de gols (`HG`, `AG`) e resultado (`Res`).
3.  Definição de uma função `comparar_times` que calcula estatísticas de confrontos diretos entre dois times específicos, incluindo:
    *   Número total de jogos.
    *   Vitórias de cada time.
    *   Empates.
    *   Probabilidade de vitória do mandante, visitante e empate.
    *   Média de gols do mandante, visitante e total por jogo.

Para esta análise, foram comparados os times **Palmeiras** e **Flamengo RJ** como exemplo.

## Resultados da Análise (Palmeiras vs. Flamengo RJ)

A seguir, são apresentados os resultados do confronto entre Palmeiras e Flamengo RJ:

```
Confrontos entre os times:
            Date         Home         Away   HG   AG Res
165   16/08/2012    Palmeiras  Flamengo RJ  1.0  0.0   H
354   18/11/2012  Flamengo RJ    Palmeiras  1.0  1.0   D
786   04/05/2014  Flamengo RJ    Palmeiras  4.0  2.0   H
976   18/09/2014    Palmeiras  Flamengo RJ  2.0  2.0   D
1323  16/08/2015    Palmeiras  Flamengo RJ  4.0  2.0   H
1514  06/12/2015  Flamengo RJ    Palmeiras  1.0  2.0   A
1575  05/06/2016  Flamengo RJ    Palmeiras  1.0  2.0   A
1765  15/09/2016    Palmeiras  Flamengo RJ  1.0  1.0   D
2045  20/07/2017  Flamengo RJ    Palmeiras  2.0  2.0   D
2234  12/11/2017    Palmeiras  Flamengo RJ  2.0  0.0   H
2395  14/06/2018    Palmeiras  Flamengo RJ  1.0  1.0   D
2586  27/10/2018  Flamengo RJ    Palmeiras  1.0  1.0   D
2824  01/09/2019  Flamengo RJ    Palmeiras  3.0  0.0   H
3014  01/12/2019    Palmeiras  Flamengo RJ  1.0  3.0   A
3148  27/09/2020    Palmeiras  Flamengo RJ  1.0  1.0   D
3342  21/01/2021  Flamengo RJ    Palmeiras  2.0  0.0   H
3425  30/05/2021  Flamengo RJ    Palmeiras  1.0  0.0   H
3609  12/09/2021    Palmeiras  Flamengo RJ  1.0  3.0   A
3820  20/04/2022  Flamengo RJ    Palmeiras  0.0  0.0   D
4023  21/08/2022    Palmeiras  Flamengo RJ  1.0  1.0   D
4314  09/07/2023    Palmeiras  Flamengo RJ  1.0  1.0   D
4500  09/11/2023  Flamengo RJ    Palmeiras  3.0  0.0   H
4584  21/04/2024    Palmeiras  Flamengo RJ  0.0  0.0   D
4765  11/08/2024  Flamengo RJ    Palmeiras  1.0  1.0   D
                                     Métrica      Valor
0   Possibilidade de vitória do mandante (%)  33.333333
1  Possibilidade de vitória do visitante (%)  16.666667
2                Possibilidade de empate (%)  50.000000
3         Média de gols do mandante por jogo   1.500000
4        Média de gols do visitante por jogo   1.083333
5               Média total de gols por jogo   2.583333
6                      Vitórias de Palmeiras   5.000000
7                    Vitórias de Flamengo RJ   7.000000
8                        Total de confrontos  24.000000
```

### Interpretação dos Resultados

Com base nos 24 confrontos diretos entre Palmeiras e Flamengo RJ no dataset, observamos o seguinte:

*   **Probabilidades de Resultado:**
    *   A probabilidade de vitória do time mandante (considerando o time que joga em casa no confronto específico) é de aproximadamente **33.33%**.
    *   A probabilidade de vitória do time visitante é de aproximadamente **16.67%**.
    *   A probabilidade de empate é a mais alta, com **50%**.
    Isso sugere que, historicamente, confrontos entre Palmeiras e Flamengo RJ tendem a terminar em empate.

*   **Média de Gols:**
    *   A média de gols marcados pelo time mandante por jogo é de **1.50**.
    *   A média de gols marcados pelo time visitante por jogo é de **1.08**.
    *   A média total de gols por jogo é de **2.58**.
    Esses números indicam que os jogos entre esses dois times são, em média, de placares moderados, com o time mandante tendo uma ligeira vantagem na média de gols marcados.

*   **Vitórias por Time:**
    *   O Palmeiras obteve **5** vitórias nos confrontos diretos.
    *   O Flamengo RJ obteve **7** vitórias nos confrontos diretos.
    *   Houve **12** empates (24 total de jogos - 5 vitórias do Palmeiras - 7 vitórias do Flamengo RJ = 12 empates).
    Apesar da alta taxa de empates, o Flamengo RJ tem um histórico ligeiramente superior de vitórias diretas contra o Palmeiras neste conjunto de dados.

## Conclusão

A análise dos confrontos entre Palmeiras e Flamengo RJ revela uma tendência significativa de empates, indicando jogos equilibrados. Embora o Flamengo RJ tenha um número maior de vitórias diretas, a alta probabilidade de empate sugere que o resultado de um jogo entre esses dois times é frequentemente imprevisível. A média de gols indica partidas com placares razoáveis, sem uma dominância esmagadora de gols por parte de nenhum dos times.

Esta análise pode ser estendida para comparar quaisquer outros dois times presentes no arquivo `BRA.csv`.

