# Networking-Station

## Objetivo

O objetivo desse projeto é criar um cliente que recebe e envia informações de/para um arduino através de um servidor.

## Funções

- O **arduino** será responsável por gerar dados através do sensores e ativar/desativar portas digitais conforme o cliente desejar.
- O **servidor** servirá de ponte por onde os dados chegarão do cliente e serão enviados para o arduino e vice-versa. Além disso ele será capaz de enviar mensagens de alerta para o cliente de acordo com condiçes programadas.
- O **cliente** receberá informaçes dos sensores do arduino e poderá enviar mensagens ao mesmo.
