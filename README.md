# Proyecto de Semáforo Inteligente con Sensores de Temperatura y Humedad

Este repositorio contiene el código y las instrucciones necesarias para construir un semáforo inteligente basado en Arduino que, además de gestionar el tráfico, mide la temperatura y la humedad del ambiente utilizando sensores DHT11.
![Header Image](https://www.cactustraffic.com.mx/wp-content/uploads/2016/07/Destacada.jpg)

## Tabla de Contenidos
- [Descripción](#descripción)
- [Componentes](#componentes)
- [Esquema de Conexión](#esquema-de-conexión)
- [Instalación](#instalación)
- [Licencia](#licencia)

## Descripción

El proyecto consiste en un semáforo inteligente que no solo controla el flujo del tráfico sino que también mide y muestra la temperatura y la humedad del ambiente. Utiliza LEDs para simular el semáforo y un sensor DHT11 para las mediciones ambientales, mostrando los datos en un display LCD de 16x2.

## Componentes

- Arduino Uno o similar
- Sensor de temperatura y humedad DHT11
- Display LCD 16x2 con interfaz I2C
- LEDs (rojo, amarillo y verde)
- Resistencias (220 ohmios para LEDs y 10k ohmios para DHT11)
- Protoboard y cables de conexión

## Esquema de Conexión

### Conexión del Semáforo (LEDs)
- **LED Rojo**
  - Ánodo -> Pin digital 8 en el Arduino
  - Cátodo -> GND (a través de una resistencia de 220 ohmios)
- **LED Amarillo**
  - Ánodo -> Pin digital 7 en el Arduino
  - Cátodo -> GND (a través de una resistencia de 220 ohmios)
- **LED Verde**
  - Ánodo -> Pin digital 6 en el Arduino
  - Cátodo -> GND (a través de una resistencia de 220 ohmios)

### Conexión del Sensor DHT11
- VCC -> 5V en el Arduino
- GND -> GND en el Arduino
- DATA -> Pin digital 2 en el Arduino (con una resistencia de 10k ohmios a VCC)

### Conexión del Display LCD 16x2 con I2C
- VCC -> 5V en el Arduino
- GND -> GND en el Arduino
- SDA -> Pin A4 en el Arduino
- SCL -> Pin A5 en el Arduino

## Instalación

1. **Clona este repositorio en tu máquina local:**
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Instala las bibliotecas necesarias en el IDE de Arduino:**
    - [DHT sensor library](https://github.com/adafruit/DHT-sensor-library) de Adafruit.
    - [LiquidCrystal I2C](https://github.com/johnrickman/LiquidCrystal_I2C).

    Puedes instalar estas bibliotecas directamente desde el Administrador de Bibliotecas en el IDE de Arduino.

3. **Carga el código en tu Arduino:**
    - Abre el archivo `smart_traffic_light.ino` en el IDE de Arduino.
    - Conecta tu Arduino a la computadora.
    - Selecciona el puerto y el tipo de placa correspondiente.
    - Sube el código al Arduino.


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

