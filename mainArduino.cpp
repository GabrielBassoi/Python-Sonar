#include <Servo.h>

Servo servo;

int contador;
int posicao = 0;
int PinTrigger = 4;
int PinEcho = 3;
float TempEcho = 0;

const float VelocidadeSom_mpors = 340;
const float VelocidadeSom_mporus = 0.000340;

void setup(){
  servo.attach(2);
  pinMode(PinTrigger, OUTPUT);
  digitalWrite(PinTrigger, LOW);
  pinMode(PinEcho, INPUT);
  pinMode(11, OUTPUT);
  Serial.begin(115200);
}

void DisparaPulsoUltrassonico(){
  digitalWrite(PinTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(PinTrigger, LOW);
}

float CalculaDistancia(float tempo_us){
  return((tempo_us*VelocidadeSom_mporus)/2);
}

int Distancia() {
  DisparaPulsoUltrassonico();
  TempEcho = pulseIn(PinEcho, HIGH);
  return CalculaDistancia(TempEcho)*100;
}

void loop(){
  for (contador = 1; contador <= 180; contador++)
  {
    servo.write(posicao);
    posicao = posicao + 1;

    int d = Distancia();
    if (d < 200) {
      Serial.print(posicao)
      Serial.print(", ")
      Serial.println(d)
    }
    delay(50);
  }

  for (contador = 180; contador >= 1; contador--)
  {
    servo.write(posicao);
    posicao = posicao - 1;

    int d = Distancia();
    if (d < 200) {
      Serial.print(posicao)
      Serial.print(", ")
      Serial.println(d)
    }
    delay(50);
  }
}