import pandas as pd

df = pd.read_csv('/home/ubuntu/upload/BRA.csv')

df_clean = df.dropna(subset=['HG', 'AG', 'Res'])

def comparar_times(time1, time2, df):
    confrontos = df[((df['Home'] == time1) & (df['Away'] == time2)) | \
                    ((df['Home'] == time2) & (df['Away'] == time1))]

    confrontos_unicos = confrontos.drop_duplicates(subset=['Date', 'Home', 'Away'])
    
    if confrontos_unicos.empty:
        print("Não há confrontos registrados entre esses times.")
        return
    
    print("Confrontos entre os times:")
    print(confrontos_unicos[['Date', 'Home', 'Away', 'HG', 'AG', 'Res']])
    
    total_jogos = len(confrontos_unicos)
    
    vitorias_mandante = len(confrontos_unicos[confrontos_unicos['Res'] == 'H'])
    vitorias_visitante = len(confrontos_unicos[confrontos_unicos['Res'] == 'A'])
    empates = len(confrontos_unicos[confrontos_unicos['Res'] == 'D'])
    
    prob_vitoria_mandante = (vitorias_mandante / total_jogos) * 100
    prob_vitoria_visitante = (vitorias_visitante / total_jogos) * 100
    prob_empate = (empates / total_jogos) * 100
    
    media_gols_mandante = confrontos_unicos['HG'].mean()
    media_gols_visitante = confrontos_unicos['AG'].mean()
    media_gols_total = confrontos_unicos[['HG', 'AG']].sum(axis=1).mean()
    
    vitorias_time1 = len(confrontos_unicos[(confrontos_unicos['Home'] == time1) & (confrontos_unicos['Res'] == 'H')]) + len(confrontos_unicos[(confrontos_unicos['Away'] == time1) & (confrontos_unicos['Res'] == 'A')])
    vitorias_time2 = len(confrontos_unicos[(confrontos_unicos['Home'] == time2) & (confrontos_unicos['Res'] == 'H')]) + len(confrontos_unicos[(confrontos_unicos['Away'] == time2) & (confrontos_unicos['Res'] == 'A')])
    
    resultados = {
        'Métrica': [
            'Possibilidade de vitória do mandante (%)',
            'Possibilidade de vitória do visitante (%)',
            'Possibilidade de empate (%)',
            'Média de gols do mandante por jogo',
            'Média de gols do visitante por jogo',
            'Média total de gols por jogo',
            f'Vitórias de {time1}',
            f'Vitórias de {time2}',
            'Total de confrontos'
        ],
        'Valor': [
            prob_vitoria_mandante,
            prob_vitoria_visitante,
            prob_empate,
            media_gols_mandante,
            media_gols_visitante,
            media_gols_total,
            vitorias_time1,
            vitorias_time2,
            total_jogos
        ]
    }

    df_resultados = pd.DataFrame(resultados)
    print(df_resultados)

# Exemplo de uso: (Você pode alterar os times aqui para testar)
# comparar_times('Palmeiras', 'Flamengo RJ', df_clean)

# Para interação com o usuário, descomente as linhas abaixo e comente as de exemplo
# time1 = input("Digite o nome do primeiro time: ")
# time2 = input("Digite o nome do segundo time: ")
# comparar_times(time1, time2, df_clean)

# Exemplo de uso com times específicos para demonstração
comparar_times('Palmeiras', 'Flamengo RJ', df_clean)


