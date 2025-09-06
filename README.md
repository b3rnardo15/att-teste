# Raspagem de Dados com Beautiful Soup

Este projeto consiste em um script Python para realizar a raspagem de dados da cotação do Euro para o Real Brasileiro no site Wise.com, utilizando a biblioteca Beautiful Soup.

## Objetivo

O principal objetivo desta atividade é demonstrar a capacidade de extrair informações específicas de páginas web de forma programática, uma técnica conhecida como Web Scraping. Para isso, foi utilizado o site Wise (anteriormente TransferWise) como fonte de dados e o tutorial da Hashtag Treinamentos como guia para a implementação com Beautiful Soup.

## Tecnologias Utilizadas

*   **Python 3**: Linguagem de programação principal.
*   **Beautiful Soup**: Biblioteca Python para extrair dados de arquivos HTML e XML.
*   **Requests**: Biblioteca Python para fazer requisições HTTP.

## Como Funciona

O script `scrape_wise.py` realiza os seguintes passos:

1.  Faz uma requisição HTTP GET para a URL `https://wise.com/br/currency-converter/euro-hoje`.
2.  Analisa o conteúdo HTML da página utilizando o Beautiful Soup.
3.  Procura por um elemento específico que contém a taxa de câmbio atual de 1 Euro para Real Brasileiro.
4.  Extrai e exibe a taxa de câmbio encontrada.

## Como Executar o Script

Para executar este script, siga os passos abaixo:

1.  Certifique-se de ter o Python 3 instalado em seu sistema.
2.  Instale as bibliotecas `requests` e `beautifulsoup4` (se ainda não as tiver):
    ```bash
    pip install requests beautifulsoup4
    ```
3.  Salve o código fornecido como `scrape_wise.py`.
4.  Abra o terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o script:
    ```bash
    python3 scrape_wise.py
    ```

## Resultado Esperado

Ao executar o script, você verá a taxa de câmbio atual do Euro para o Real Brasileiro impressa no console, similar a:

```
A taxa de câmbio atual de 1 Euro para Real Brasileiro é: X.XXXX BRL
```

(Onde `X.XXXX` será o valor da cotação no momento da execução.)

## Observações

É importante notar que a estrutura de uma página web pode mudar com o tempo. Se o site Wise.com alterar a forma como exibe a cotação do Euro, o script pode precisar de atualizações para continuar funcionando corretamente. A raspagem de dados deve ser feita de forma ética e respeitando os termos de serviço do site alvo.


