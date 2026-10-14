import graphviz

dot = graphviz.Digraph(comment='Mapa Conceptual: Circuiteria Alternativa de E/S', format='png')
dot.attr(rankdir='TB')
dot.attr(size='24,18', dpi='150')

dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='18', margin='0.4')
dot.attr('edge', fontname='Arial', fontsize='14', penwidth='2.0', arrowhead='vee')
dot.node('Central', 'CIRCUITERÍA ALTERNATIVA DE E/S\n(Técnicas de expansión para superar limitaciones de pines en Microcontroladores)', fillcolor='#D1E8FF', fontsize='26', fontname='Arial Bold')

# --- RAMAS PRINCIPALES ---
dot.node('Shift', 'REGISTROS DE DESPLAZAMIENTO\n(Shift Registers)', fillcolor='#C1FFC1', fontsize='20', fontname='Arial Bold')
dot.node('Mux', 'MULTIPLEXORES /\nDEMULTIPLEXORES (MUX / DEMUX)', fillcolor='#FFFFC1', fontsize='20', fontname='Arial Bold')
dot.node('Bus', 'EXPANSORES POR\nBUS DE COMUNICACIÓN', fillcolor='#FFC1C1', fontsize='20', fontname='Arial Bold')
dot.node('Matrix', 'TÉCNICAS DE MATRICEO\n(Matrixing)', fillcolor='#FFC1FF', fontsize='20', fontname='Arial Bold')
dot.node('Analog', 'TÉCNICAS ANALÓGICAS\n(Resistor Ladders)', fillcolor='#FFE0C1', fontsize='20', fontname='Arial Bold')

# Conexiones
dot.edge('Central', 'Shift', label='se implementa mediante')
dot.edge('Central', 'Mux', label='se implementa mediante')
dot.edge('Central', 'Bus', label='se implementa mediante')
dot.edge('Central', 'Matrix', label='se implementa mediante')
dot.edge('Central', 'Analog', label='se implementa mediante')

# --- INFORMACIÓN TÉCNICA DETALLADA  ---
dot.attr('node', fillcolor='white', fontname='Arial', fontsize='16', shape='note', margin='0.5', style='filled')

dot.node('ExShift',
         r'• Funcionamiento: Convierten datos serie en paralelo (SIPO, ej: 74HC595 para SALIDAS) o viceversa (PISO, ej: CD4021 para ENTRADAS).\l'
         r'• Pines de control: Requieren típicamente 3 pines (Reloj/Clock, Datos/Data, Cerrojo/Latch).\l'
         r'• Ventaja: Escalabilidad. Se pueden encadenar (daisy-chain) varios chips para controlar decenas de pines usando las mismas 3 líneas.\l'
         r'• Ejemplo: Control de matrices de LEDs 8x8 o múltiples displays de 7 segmentos.\l')
dot.edge('Shift', 'ExShift', label='características\ny funcionamiento')

# Detalles de Mux / Demux
dot.node('ExMux',
         r'• Funcionamiento: Conmutan múltiples canales de señal hacia un solo pin del microcontrolador o viceversa.\l'
         r'• Tipos: Analógicos (conmutan voltaje bidireccionalmente, ej: CD4051) o Digitales (conmutan solo niveles lógicos).\l'
         r'• Control: Usan n pines de selección binaria para controlar 2^n canales.\l'
         r'• Ventaja: Permiten leer muchos sensores analógicos con un solo pin ADC o controlar múltiples dispositivos digitales secuencialmente.\l'
         r'• Ejemplo: Lectura secuencial de 16 potenciómetros usando un solo pin analógico.\l')
dot.edge('Mux', 'ExMux', label='características\ny funcionamiento')

# Detalles de Expansores por Bus
dot.node('ExBus',
         r'• Funcionamiento: Utilizan protocolos de comunicación serie síncrona para enviar comandos de E/S.\l'
         r'• Protocolos comunes:\l'
         r'  - I2C: Solo 2 cables (SDA y SCL), bidireccional, permite direccionamiento (ej: PCF8574).\l'
         r'  - SPI: Requiere 4 cables (MISO, MOSI, SCK, CS), más rápido pero usa más pines (ej: MCP23S17).\l'
         r'• Ventaja: Gran flexibilidad, gran cantidad de pines extra (hasta 16 por chip) y direccionamiento avanzado.\l'
         r'• Ejemplo: Adición rápida de un puerto paralelo de 8 bits a un microcontrolador de pocos pines.\l')
dot.edge('Bus', 'ExBus', label='características\ny funcionamiento')

# Detalles de Matrices
dot.node('ExMatrix',
         r'• Funcionamiento: Organizan interruptores o LEDs en filas (Rows) y columnas (Cols).\l'
         r'• Estrategia: Barrido secuencial. Se activa una fila a la vez y se leen las columnas para detectar pulsaciones.\l'
         r'• Optimización: Usan N + M pines para controlar N × M puntos de conexión.\l'
         r'• Ejemplo clásico: Un teclado matricial de 4x4 (16 botones) usa solo 8 pines del microcontrolador.\l')
dot.edge('Matrix', 'ExMatrix', label='características\ny funcionamiento')

# Detalles Analógicos
dot.node('ExAnalog',
         r'• Funcionamiento: Utilizan un divisor de tensión formado por una red de resistencias (Resistor Ladder) conectadas a pulsadores.\l'
         r'• Estrategia: Cada botón presionado altera el valor del divisor y genera un nivel de voltaje analógico único.\l'
         r'• Optimización extrema: Permite diferenciar múltiples botones (ej: 5-10) usando un solo pin analógico (ADC).\l'
         r'• Ejemplo: Botones de control de volumen y navegación en reproductores de música o mandos de juegos.\l')
dot.edge('Analog', 'ExAnalog', label='características\ny funcionamiento')


dot.render('mapa_conceptual_es', view=False)
print("¡Mapa conceptual de alta legibilidad generado con éxito como 'mapa_conceptual_es.png'!")