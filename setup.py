#!/usr/bin/env python3
"""
Script de configuración inicial de Game Turbo Pro
"""

import os
import sys
from pathlib import Path

def setup():
    """Ejecuta la configuración inicial"""
    print("""
    ╔════════════════════════════════════════╗
    ║   GAME TURBO PRO - Setup Inicial       ║
    ║   🎮 Lanzador de Juegos Optimizado    ║
    ╚════════════════════════════════════════╝
    """)
    
    # Crear directorios necesarios
    dirs = ['logs', 'profiles', 'plugins', '.gameturbopro']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✓ Directorio creado: {dir_name}")
    
    # Crear archivo de configuración
    config_file = Path('.gameturbopro/config.json')
    if not config_file.exists():
        import json
        config = {
            'cpu_priority': 'high',
            'gpu_enabled': True,
            'temperature_limit': 80,
            'ram_cleanup_interval': 300,
            'fps_target': 60,
            'background_processes': True,
            'theme': 'dark'
        }
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✓ Archivo de configuración creado")
    
    print("""
    ✓ Setup completado exitosamente
    
    Próximos pasos:
    1. Instala dependencias: pip install -r requirements.txt
    2. Ejecuta la aplicación: python main.py
    3. ¡Disfruta optimizando tus juegos!
    """)

if __name__ == '__main__':
    setup()
