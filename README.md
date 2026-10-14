# Mapa Conceptual: Circuitería Alternativa de E/S

Repositorio que contiene un script en Python para generar un mapa conceptual detallado sobre las técnicas de expansión y manejo de entradas/salidas (E/S) en microcontroladores.

# Contenido del Mapa Conceptual
El mapa generado aborda las siguientes estrategias para superar limitaciones de pines:
1. **Registros de Desplazamiento (Shift Registers):** Conversión serie-paralelo (ej. 74HC595, CD4021).
2. **Multiplexores y Demultiplexores (MUX / DEMUX):** Conmutación de canales analógicos y digitales.
3. **Expansores por Bus de Comunicación:** Protocolos síncronos como I2C (ej. PCF8574) y SPI.
4. **Técnicas de Matricéo (Matrixing):** Organización de interruptores en filas y columnas ($N \times M$).
5. **Técnicas Analógicas (Resistor Ladders):** Lectura múltiple de pulsadores mediante divisores de tensión y un solo pin ADC.

## Requisitos e Instalación
Para ejecutar el script y generar el mapa conceptual, necesitas tener instalado:
* **Python** (versión 3.x recomendada).
* La librería **Graphviz** para Python.
* El motor del sistema de Graphviz.

### 1. Instalar la librería en Python
Abre tu terminal o la consola de PyCharm y ejecuta:
```bash
pip install graphviz
