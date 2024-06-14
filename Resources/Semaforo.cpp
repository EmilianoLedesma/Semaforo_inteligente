#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Pines para los LEDs
const int redLED = 8;
const int yellowLED = 7;
const int greenLED = 6;

// Configuración del sensor DHT11
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Configuración del display LCD 16x2 con I2C
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Variables para almacenar temperatura y humedad
float temperature;
float humidity;

void setup() {
  // Inicialización de los pines de los LEDs
  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(greenLED, OUTPUT);

  // Inicialización del sensor DHT11
  dht.begin();

  // Inicialización del display LCD
  lcd.begin();
  lcd.backlight();

  // Mensaje de inicio en el LCD
  lcd.setCursor(0, 0);
  lcd.print("Semaforo Intel.");
  lcd.setCursor(0, 1);
  lcd.print("Iniciando...");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Leer los valores del sensor DHT11
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  // Mostrar los valores en el LCD
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print(" C");
  lcd.setCursor(0, 1);
  lcd.print("Hum: ");
  lcd.print(humidity);
  lcd.print(" %");

  // Control del semáforo (ciclo simple)
  digitalWrite(redLED, HIGH);
  delay(5000); // Mantener LED rojo encendido por 5 segundos
  digitalWrite(redLED, LOW);
  
  digitalWrite(yellowLED, HIGH);
  delay(2000); // Mantener LED amarillo encendido por 2 segundos
  digitalWrite(yellowLED, LOW);
  
  digitalWrite(greenLED, HIGH);
  delay(5000); // Mantener LED verde encendido por 5 segundos
  digitalWrite(greenLED, LOW);

  // Esperar antes de repetir el ciclo
  delay(1000);
}
