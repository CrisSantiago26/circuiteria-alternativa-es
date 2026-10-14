
import graphviz

dot = graphviz.Digraph(
    'MapaConceptual',
    comment='Circuitería alternativa de E/S',
    format='png'
)

dot.attr(
    rankdir='TB',
    size='11,8.5!',
    ratio='compress',
    dpi='180',
    margin='0.12',
    nodesep='0.18',
    ranksep='0.35',
    splines='polyline',
    bgcolor='white',
    pad='0.10'
)


dot.attr(
    'node',
    shape='box',
    style='rounded,filled',
    fontname='Arial',
    fontsize='9',
    margin='0.10,0.07',
    color='#526579',
    penwidth='1.1'
)

dot.attr(
    'edge',
    fontname='Arial',
    fontsize='7',
    color='#526579',
    fontcolor='#34495E',
    penwidth='1.0',
    arrowsize='0.65',
    arrowhead='vee'
)


dot.node(
    'Central',
    'CIRCUITERÍA ALTERNATIVA DE E/S\n'
    'Expansión de entradas y salidas en microcontroladores',
    fillcolor='#CFE5FF',
    fontsize='13',
    fontname='Arial Bold',
    penwidth='1.8'
)

categorias = [
    ('Shift', 'REGISTROS DE\nDESPLAZAMIENTO', '#D7F3D0'),
    ('Mux', 'MULTIPLEXORES Y\nDEMULTIPLEXORES', '#FFF0B8'),
    ('Bus', 'EXPANSORES POR\nBUS DE COMUNICACIÓN', '#FFD9D9'),
    ('Matrix', 'TÉCNICAS DE\nMATRICEO', '#EAD9FF'),
    ('Analog', 'TÉCNICAS\nANALÓGICAS', '#FFE2C5')
]

for nodo, texto, color in categorias:
    dot.node(
        nodo,
        texto,
        fillcolor=color,
        fontsize='9',
        fontname='Arial Bold'
    )

detalles = {
    'ExShift': (
        'Funcionamiento:\n'
        'Convierten datos serie-paralelo (SIPO)\n'
        'o paralelo-serie (PISO).\n\n'
        'Utilizan:\n'
        'Reloj, datos y cerrojo (latch).\n\n'
        'Ventaja:\n'
        'Permiten encadenar circuitos.\n\n'
        'Ejemplo: 74HC595 y CD4021.'
    ),

    'ExMux': (
        'Funcionamiento:\n'
        'Seleccionan una señal entre varios\n'
        'canales, o distribuyen una señal.\n\n'
        'Utilizan:\n'
        'Líneas de selección binarias.\n\n'
        'Ventaja:\n'
        'Reducen los pines necesarios.\n\n'
        'Ejemplo: CD4051.'
    ),

    'ExBus': (
        'Funcionamiento:\n'
        'Amplían las E/S mediante buses\n'
        'de comunicación serie.\n\n'
        'Utilizan:\n'
        'I2C (SDA y SCL) o SPI.\n\n'
        'Ventaja:\n'
        'Añaden puertos de E/S.\n\n'
        'Ejemplo: PCF8574 y MCP23S17.'
    ),

    'ExMatrix': (
        'Funcionamiento:\n'
        'Organizan botones o LED en filas\n'
        'y columnas mediante barrido.\n\n'
        'Utilizan:\n'
        'Filas y columnas compartidas.\n\n'
        'Ventaja:\n'
        'Reducen las conexiones necesarias.\n\n'
        'Ejemplo: teclado 4 × 4 con 8 pines.'
    ),

    'ExAnalog': (
        'Funcionamiento:\n'
        'Una red de resistencias genera\n'
        'voltajes distintos por pulsador.\n\n'
        'Utilizan:\n'
        'Divisores de tensión y una entrada ADC.\n\n'
        'Ventaja:\n'
        'Leen varios botones con un pin.\n\n'
        'Ejemplo: controles de navegación.'
    )
}

for nodo, texto in detalles.items():
    dot.node(
        nodo,
        texto,
        shape='box',
        style='filled',
        fillcolor='#F7F9FC',
        fontsize='8',
        fontname='Arial',
        margin='0.12',
        width='1.75'
    )

with dot.subgraph() as nivel2:
    nivel2.attr(rank='same')
    for nodo, _, _ in categorias:
        nivel2.node(nodo)

with dot.subgraph() as nivel3:
    nivel3.attr(rank='same')
    for nodo in detalles:
        nivel3.node(nodo)

for nodo, _, _ in categorias:
    dot.edge(
        'Central',
        nodo,
        label='se implementa mediante'
    )

relaciones = [
    ('Shift', 'ExShift', 'se caracteriza por'),
    ('Mux', 'ExMux', 'permite'),
    ('Bus', 'ExBus', 'utiliza'),
    ('Matrix', 'ExMatrix', 'organiza'),
    ('Analog', 'ExAnalog', 'se basa en')
]

for origen, destino, enlace in relaciones:
    dot.edge(origen, destino, label=enlace)

dot.render('mapa_conceptual_carta', view=False, cleanup=True)

print('Mapa conceptual generado: mapa_conceptual_carta.png')
