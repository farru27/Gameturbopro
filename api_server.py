#!/usr/bin/env python3
"""
Servidor API REST para Game Turbo Pro
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.launcher import UnifiedLauncher
from src.api import GameTurboAPI

if __name__ == '__main__':
    launcher = UnifiedLauncher()
    api = GameTurboAPI(launcher)
    
    print("""
    ╔════════════════════════════════════════╗
    ║   GAME TURBO PRO - API REST Server    ║
    ║   🌐 Servidor ejecutándose...         ║
    ╚════════════════════════════════════════╝
    """)
    print("API disponible en: http://localhost:5000")
    print("Presiona Ctrl+C para detener...\n")
    
    try:
        api.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n✓ Servidor detenido")
