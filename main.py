#!/usr/bin/env python3
"""
Game Turbo Pro - Lanzador de Juegos Unificado
Combina Game Turbo y Game Booster para optimización de rendimiento
"""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ui.main_window import GameLauncherApp

if __name__ == '__main__':
    app = GameLauncherApp()
    app.run()
