<h1 align = center>
    Câmbio Dólar e Euro em Reais
</h1>

<h1 align = center>
    <img src = "public/câmbio.jpg">
</h1>

## Índice

- [Sobre](#-Sobre)
- [Tecnologias](#-Tecnologias)



## Sobre

O projeto tem como intuito enviar uma mensagem contendo o câmbio atual
do Dólar e do Euro em Reais. Tal mensagem é enviada diariamente para um grupo específico
setado no código, a fim de ter uma percepção de flutuação no valor das moedas.

## Tecnologias

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- [Python](https://www.python.org/downloads/)
- [Awesome API](https://docs.awesomeapi.com.br/api-de-moedas)
- [Requests](https://pypi.org/project/requests/)
- [Telegram Bot](https://core.telegram.org/bots)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Schedule](https://schedule.readthedocs.io/en/stable/)

## Preparando o Ambiente

Para que o arquivo "main.py" consiga executar de forma correta, faz necessário importar as bibliotecas, como no exemplo a seguir:
```bash
$ import os
$import dotenv
$import time
$import schedule
$import src.Exchange.Client as exchange
$import src.Telegram.Client as TEC
```
Obs: Note que nas duas últimas linhas, as bibliotecas importadas correspondem aos arquivos do próprio projeto.

## Uso 

Este programa destina-se para pessoas que desejam monitorar o valor diário das moedas em questão, para uma compra acertiva.

## Contato
e-mail: daniel_itame@hotmail.com 

