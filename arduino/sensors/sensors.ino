#include <DHT.h>

#define DHTPIN A0 // pino que estamos conectado
#define DHTTYPE DHT11 // DHT 11
 
// Conecte pino 1 do sensor (esquerda) ao +5V
// Conecte pino 2 do sensor ao pino de dados definido em seu Arduino
// Conecte pino 4 do sensor ao GND
// Conecte o resistor de 10K entre pin 2 (dados) 
// e ao pino 1 (VCC) do sensor
DHT dht(DHTPIN, DHTTYPE);

//LDR 
int ldrPin = A5; //LDR no pino analígico 8
int ldrValor = 0; //Valor lido do LDR

//Senso de chuva
int rainD = 7; //Pino ligado ao D0 do sensor
int rainA = A1; //Pino ligado ao A0 do sensor
int valD = 0; //Armazena o valor lido do pino digital
int valA = 0; //Armazena o valor lido do pino analogico
 
void setup() 
{
  Serial.begin(9600);
  dht.begin();
  pinMode(rainD, INPUT);
  pinMode(rainA, INPUT);
}
 
void loop() 
{
  // A leitura da temperatura e umidade pode levar 250ms!
  // O atraso do sensor pode chegar a 2 segundos.
  int humid = dht.readHumidity();
  int temp = dht.readTemperature();

  ///ler o valor do LDR
  ldrValor = analogRead(ldrPin); //O valor lido será entre 0 e 1023
  
  //sedor de chuva
  valD = digitalRead(rainD);
  //Le e armazena o valor do pino analogico
  valA = analogRead(rainA);
 
  
  String splitAux = ":";
  String stringStream = humid + splitAux + temp + splitAux + ldrValor + splitAux + valD + splitAux + valA;

  Serial.println(stringStream);
  delay(2000);
  
}
