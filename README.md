# Networking-Station
# Versão de teste sem arduino

## Objetivo

O objetivo desse projeto é criar um cliente que recebe informações de um arduino através de um servidor.


## Instalação

[Instalação PyQt5](http://pyqt.sourceforge.net/Docs/PyQt5/installation.html)

[Instalação pySerial](http://pyserial.readthedocs.io/en/latest/pyserial.html)

[Instalação Arduino Library DHT-sensor](https://github.com/adafruit/DHT-sensor-library)

## Execução

[Versão sem Arduino](https://github.com/lfelipev/Networking-Station/tree/no-arduino)

O servidor deve ser executado antes de rodar a aplicação por inteiro: ```python server.py```

Em seguida a aplicação pode ser executada: ```python3 main.py```

## Estrutura

- O **arduino** será responsável por gerar dados através do sensores.
- O **servidor** servirá de ponte por onde os dados chegarão do arduino e serão enviados para o cliente.
- O **cliente** receberá as informaçes do servidor e exibirá na tela.

![estruct](https://github.com/lfelipev/Networking-Station/blob/master/pics/estrutura.png "Estrutura do projeto")

## Interface

Na interface do cliente apresentamos em ordem:

1. Temperatura (indicado pelo ícone do termômetro)

   ![thermometer](https://github.com/lfelipev/Networking-Station/blob/master/pics/thermometer.png "Thermometer")
2. Umidade relativa do ar (indicada pelo ícone da gota)

   ![drop](https://github.com/lfelipev/Networking-Station/blob/master/pics/drop.png "Drop")
3. Luminosidade do ambiente (indicada pelo ícone da lua)

   Sem luz: ![dark](https://github.com/lfelipev/Networking-Station/blob/master/pics/dark.png "Dark")
   Luz fraca: ![dim-light](https://github.com/lfelipev/Networking-Station/blob/master/pics/dim-light.png "Dim-light")
   Luz média: ![medium-light](https://github.com/lfelipev/Networking-Station/blob/master/pics/medium-light.png "Medium-light")
   Iluminado: ![light](https://github.com/lfelipev/Networking-Station/blob/master/pics/light.png "Light")
   Luz forte: ![very-light](https://github.com/lfelipev/Networking-Station/blob/master/pics/very-light.png "Very-light")
4. Intensidade da chuva (indicade pelo ícone da núvem)

   Sem chuva: ![no-rain](https://github.com/lfelipev/Networking-Station/blob/master/pics/no-rain.png "No rain")
   Chuva moderada: ![rain](https://github.com/lfelipev/Networking-Station/blob/master/pics/rain.png "Rain")
   Chuva forte: ![storm](https://github.com/lfelipev/Networking-Station/blob/master/pics/storm.png "Storm")

## Sensores

- Sensor de chuva YL-83 [example](https://www.filipeflop.com/blog/sensor-de-chuva-yl-83/)
- Sensor de temperatura e umidade [example](https://www.filipeflop.com/produto/sensor-de-umidade-e-temperatura-dht11/)
- Sensor de luminosidade LDR (Light-Dependent Resistor)
