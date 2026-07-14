# Game Turbo Pro 🎮

Lanzador de juegos profesional que combina Game Turbo y Game Booster para optimizar el rendimiento de tus juegos.

## Características

### 🚀 Game Turbo
- Optimización de CPU y GPU
- Monitoreo de temperatura
- Gestión de procesos en segundo plano
- Asignación de recursos prioritarios

### ⚡ Game Booster
- Aumento de FPS
- Limpieza de RAM
- Optimización de memoria
- Gestión de procesos del sistema

### 🎯 Lanzador Unificado
- Interfaz gráfica intuitiva
- Control centralizado de ambas herramientas
- Perfiles predefinidos por juego
- Monitoreo en tiempo real

## Requisitos

- Python 3.8+
- tkinter (incluido en Python)
- psutil
- GPUtil (opcional para monitoreo GPU)

## Instalación

```bash
pip install -r requirements.txt
python main.py
```

## Uso

1. Abre Game Turbo Pro
2. Selecciona tu juego
3. Elige el perfil de optimización
4. Presiona "Iniciar Juego"

## Estructura del Proyecto

```
Gameturbopro/
├── main.py                 # Punto de entrada
├── requirements.txt        # Dependencias
├── README.md              # Este archivo
├── src/
│   ├── __init__.py
│   ├── game_turbo.py      # Módulo Game Turbo
│   ├── game_booster.py    # Módulo Game Booster
│   ├── launcher.py        # Lanzador unificado
│   ├── config.py          # Configuración
│   ├── monitor.py         # Monitor del sistema
│   └── ui/
│       ├── __init__.py
│       ├── main_window.py # Ventana principal
│       ├── styles.py      # Estilos GUI
│       └── widgets.py     # Componentes personalizados
├── games/                 # Perfiles de juegos
│   └── profiles.json
└── logs/                  # Registros de ejecución
```

## Licencia

MIT
