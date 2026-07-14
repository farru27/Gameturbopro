# Game Turbo Pro 🎮

## 📊 Descripción

**Game Turbo Pro** es un lanzador de juegos avanzado que combina **Game Turbo** y **Game Booster** para optimizar el rendimiento de tus juegos al máximo. Con una interfaz moderna, herramientas potentes y un sistema de perfiles inteligente, garantiza una experiencia de juego fluida y sin interrupciones.

## ✨ Características Principales

### 🚀 **Game Turbo - Optimización de Rendimiento**
- ⚙️ Optimización de CPU y GPU
- 🌡️ Monitoreo de temperatura en tiempo real
- 🔧 Deshabilitación automática de procesos innecesarios
- 📊 Control de prioridad de procesos
- 🎯 Asignación inteligente de recursos

### ⚡ **Game Booster - Aumento de Rendimiento**
- 🎮 Boost inteligente de FPS
- 💾 Limpieza automática de RAM
- ⏱️ Reducción de latencia
- 🧹 Optimización de memoria en tiempo real
- 📈 Mejora de velocidad del sistema

### 🎨 **Interfaz Moderna Premium**
- 🌙 Tema oscuro elegante con colores ciano
- 📱 Diseño responsivo y amigable
- 🎯 Controles intuitivos
- 📊 Paneles de estadísticas en tiempo real
- 🔔 Indicadores de estado visuales

### 🎯 **Perfiles Inteligentes**
- ⚡ **Performance**: Máximo rendimiento (240 FPS)
- ⚖️ **Balanced**: Equilibrio rendimiento/consumo (60 FPS)
- 💡 **Power Saving**: Ahorro de energía (30 FPS)
- 🏆 **Esports**: Optimizado para competencia (240 FPS)
- 🛠️ **Perfiles Personalizados**: Crea tus propios perfiles

### 🔌 **Características Avanzadas**
- 🔌 Sistema de plugins extensible
- 📝 Logging detallado de sesiones
- 📊 Estadísticas y análisis de desempeño
- 🎮 Detección automática de juegos (Steam, Epic)
- 🌐 API REST para control remoto
- ⌨️ Atajos de teclado personalizables
- 📈 Historial de sesiones

## 📋 Requisitos

- Python 3.8+
- Windows, Linux o macOS
- 100 MB de espacio en disco
- 512 MB de RAM mínimo

### Dependencias
```bash
psutil              # Monitoreo del sistema
GPUtil              # Información de GPU
pillow              # Procesamiento de imágenes
flask               # API REST
keyboard            # Captura de atajos
requests            # HTTP requests
python-dotenv       # Variables de entorno
```

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/farru27/Gameturbopro.git
cd Gameturbopro
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python main.py
```

## 📖 Guía de Uso

### Inicio Rápido

1. **Abre Game Turbo Pro**
   ```bash
   python main.py
   ```

2. **Selecciona tu juego**
   - Haz clic en "📁 EXAMINAR ARCHIVOS"
   - Busca el ejecutable de tu juego
   - Se mostrará el nombre del archivo

3. **Elige un perfil**
   - **⚡ Performance**: Para máximo FPS
   - **⚖️ Balanced**: Para juego normal
   - **💡 Power Saving**: Para portátiles
   - **🏆 Esports**: Para juegos competitivos

4. **Lanza tu juego**
   - Haz clic en "▶️ LANZAR JUEGO"
   - Observa las estadísticas en tiempo real

5. **Detén cuando termines**
   - Haz clic en "⏹️ DETENER"
   - Automáticamente se desactivan las optimizaciones

### Monitoreo en Tiempo Real

La interfaz muestra en vivo:

#### 🚀 **Game Turbo**
- Estado (Activo/Inactivo)
- Uso de CPU
- Temperatura del sistema
- Procesos activos

#### ⚡ **Game Booster**
- Estado (Activo/Inactivo)
- Uso de RAM
- Nivel de Boost
- FPS objetivo

#### 📊 **Monitoreo General**
- Barra de progreso de CPU
- Barra de progreso de RAM

## 🛠️ Configuración Avanzada

### Editar Perfiles

Los perfiles se encuentran en `profiles/`:

```bash
profiles/
├── performance.json
├── balanced.json
├── power_saving.json
└── esports.json
```

**Ejemplo de perfil personalizado:**
```json
{
  "name": "Mi Perfil Custom",
  "description": "Optimizado para Valorant",
  "icon": "🎯",
  "settings": {
    "cpu_priority": "realtime",
    "gpu_enabled": true,
    "boost_level": 95,
    "fps_target": 240,
    "temperature_limit": 85,
    "ram_cleanup_interval": 30,
    "background_processes": false,
    "power_saving": false
  }
}
```

### Variables de Configuración

```python
cpu_priority        # Priority del CPU: 'realtime', 'high', 'normal'
gpu_enabled         # Habilitar optimización de GPU: true/false
boost_level        # Nivel de boost: 0-100
fps_target          # FPS objetivo: 30, 60, 120, 144, 240
temperature_limit   # Límite de temperatura: 70-90°C
ram_cleanup_interval # Intervalo de limpieza: 30-600 segundos
background_processes # Permitir procesos de fondo: true/false
power_saving        # Modo ahorro: true/false
```

## 📊 Estadísticas y Historial

Todas las sesiones de juegos se guardan en `logs/`:

```bash
logs/
├── Valorant_2024-07-14T21-30-45.json
├── CS2_2024-07-14T20-15-30.json
└── ...
```

**Cada log contiene:**
- Duración de la sesión
- Estadísticas de CPU/GPU/RAM
- Eventos importantes
- Temperatura máxima alcanzada
- FPS promedio

## 🔌 Sistema de Plugins

### Crear tu Propio Plugin

```python
from src.plugins import BasePlugin

class MiPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.name = "Mi Plugin"
        self.version = "1.0.0"
    
    def on_game_launch(self, game_info):
        print(f"Juego lanzado: {game_info['name']}")
    
    def on_game_stop(self, game_info):
        print(f"Juego detenido: {game_info['name']}")
```

### Registrar Plugin

```python
from src.plugins import PluginManager

plugin_manager = PluginManager()
plugin_manager.register_plugin('mi_plugin', MiPlugin)
```

## 🌐 API REST

Game Turbo Pro incluye una API REST opcional:

```bash
python api_server.py
```

### Endpoints Disponibles

#### GET `/api/status`
Obtiene estado actual del sistema
```json
{
  "turbo": {"active": true, "cpu_percent": 45.2},
  "booster": {"active": true, "boost_level": 80},
  "current_game": "Valorant"
}
```

#### POST `/api/launch`
Lanza un juego
```json
{
  "game_path": "/path/to/game.exe",
  "game_name": "Valorant",
  "profile": "performance"
}
```

#### POST `/api/stop`
Detiene el juego actual

#### GET `/api/profiles`
Lista perfiles disponibles

#### GET `/api/processes`
Obtiene procesos en ejecución

## ⌨️ Atajos de Teclado

| Atajo | Función |
|-------|----------|
| `Ctrl+Alt+L` | Lanzar juego |
| `Ctrl+Alt+S` | Detener juego |
| `Ctrl+Alt+B` | Cambiar perfil |
| `Ctrl+Alt+M` | Mostrar/ocultar monitor |

## 📊 Estructura del Proyecto

```
Gameturbopro/
├── main.py                      # Punto de entrada principal
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
├── LICENSE                      # Licencia MIT
├── src/
│   ├── __init__.py
│   ├── config.py               # Gestión de configuración
│   ├── monitor.py              # Monitor del sistema
│   ├── game_turbo.py           # Módulo Game Turbo
│   ├── game_booster.py         # Módulo Game Booster
│   ├── launcher.py             # Lanzador unificado
│   ├── plugins.py              # Sistema de plugins
│   ├── logger.py               # Sistema de logging
│   ├── profiles.py             # Gestor de perfiles
│   ├── game_detector.py        # Detector de juegos
│   ├── hotkeys.py              # Gestor de atajos
│   ├── api.py                  # API REST
│   └── ui/
│       ├── __init__.py
│       ├── main_window.py      # Ventana principal
│       ├── styles.py           # Estilos y temas
│       └── widgets.py          # Componentes personalizados
├── profiles/                   # Perfiles de optimización
│   ├── performance.json
│   ├── balanced.json
│   ├── power_saving.json
│   └── esports.json
├── logs/                       # Historial de sesiones
└── plugins/                    # Plugins del usuario
```

## 🎓 Ejemplos de Uso

### Ejemplo 1: Lanzar juego con perfil Performance
```python
from src.launcher import UnifiedLauncher

launcher = UnifiedLauncher()
launcher.launch_game('/path/to/valorant.exe', 'Valorant', 'performance')
```

### Ejemplo 2: Crear perfil personalizado
```python
from src.profiles import ProfileManager

pm = ProfileManager()
pm.create_custom_profile(
    'my_profile',
    'balanced',
    {'boost_level': 85, 'fps_target': 120}
)
```

### Ejemplo 3: Ver estadísticas
```python
from src.logger import GameLogger

logger = GameLogger()
stats = logger.get_statistics('Valorant')
print(f"Total sessions: {stats['total_sessions']}")
print(f"Total time: {stats['total_time']} seconds")
```

## 🐛 Solución de Problemas

### No detecta el juego
- Verifica que la ruta sea correcta
- Asegúrate de seleccionar un ejecutable válido
- Intenta usar la detección automática (Steam/Epic)

### Baja de rendimiento
- Cambia a perfil "Performance"
- Cierra programas en segundo plano
- Verifica la temperatura del sistema

### Errores de permisos
- En Linux/Mac, ejecuta con `sudo` si es necesario
- Verifica permisos de carpetas

### Crash de la aplicación
- Comprueba que Python 3.8+ está instalado
- Reinstala dependencias: `pip install -r requirements.txt --force-reinstall`
- Consulta los logs en `logs/`

## 📈 Roadmap

- [ ] Soporte para directX 12
- [ ] Monitoreo de GPU mejorado
- [ ] Interfaz web
- [ ] Sincronización en la nube
- [ ] Soporte para más plataformas (GOG, Xbox)
- [ ] Machine Learning para perfiles automáticos
- [ ] Sistema de competiciones

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👨‍💻 Autor

**Game Turbo Pro** fue creado por [@farru27](https://github.com/farru27)

## 📞 Soporte

Para reportar bugs o solicitar features:
- [GitHub Issues](https://github.com/farru27/Gameturbopro/issues)
- Email: federicotourino318@gmail.com

## ⭐ Agradecimientos

Gracias a todos los que usan y contribuyen a mejorar Game Turbo Pro.

---

**¡Optimiza tu experiencia de juego ahora! 🎮✨**
