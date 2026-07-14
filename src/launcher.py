"""
Lanzador Unificado - Combina Game Turbo y Game Booster
"""

import subprocess
import os
from typing import Dict, Optional
from .game_turbo import GameTurbo
from .game_booster import GameBooster
from .monitor import SystemMonitor
from .config import config

class UnifiedLauncher:
    """Lanzador que combina Game Turbo y Game Booster"""
    
    def __init__(self):
        self.turbo = GameTurbo()
        self.booster = GameBooster()
        self.monitor = SystemMonitor()
        self.current_game = None
        self.game_process = None
    
    def get_combined_status(self) -> Dict:
        """Obtiene estado combinado de ambas herramientas"""
        return {
            'turbo': self.turbo.get_status(),
            'booster': self.booster.get_status(),
            'current_game': self.current_game,
            'monitor': self.monitor.get_system_stats()
        }
    
    def launch_game(self, game_path: str, game_name: str = None, profile: str = 'balanced') -> bool:
        """Lanza un juego con optimizaciones"""
        try:
            if not os.path.exists(game_path):
                print(f"Ejecutable no encontrado: {game_path}")
                return False
            
            self.current_game = game_name or os.path.basename(game_path)
            
            # Aplicar optimizaciones según perfil
            self._apply_profile(profile)
            
            # Iniciar monitoreo
            self.monitor.start()
            
            # Lanzar juego
            try:
                self.game_process = subprocess.Popen(game_path)
                print(f"Juego lanzado: {self.current_game} (PID: {self.game_process.pid})")
                return True
            except Exception as e:
                print(f"Error lanzando juego: {e}")
                return False
        
        except Exception as e:
            print(f"Error en launcher: {e}")
            return False
    
    def _apply_profile(self, profile: str):
        """Aplica perfil de optimización"""
        profiles = {
            'performance': {
                'turbo': True,
                'booster': True,
                'boost_level': 100,
                'fps_target': 120
            },
            'balanced': {
                'turbo': True,
                'booster': True,
                'boost_level': 70,
                'fps_target': 60
            },
            'power_saving': {
                'turbo': False,
                'booster': True,
                'boost_level': 30,
                'fps_target': 30
            }
        }
        
        settings = profiles.get(profile, profiles['balanced'])
        
        if settings['turbo']:
            self.turbo.activate_turbo(self.current_game)
        
        if settings['booster']:
            self.booster.activate_boost(settings['boost_level'])
        
        self.booster.boost_fps(settings['fps_target'])
    
    def stop_game(self) -> bool:
        """Detiene la ejecución del juego y desactiva optimizaciones"""
        try:
            if self.game_process:
                self.game_process.terminate()
                self.game_process.wait(timeout=5)
            
            self.turbo.deactivate_turbo()
            self.booster.deactivate_boost()
            self.monitor.stop()
            
            self.current_game = None
            self.game_process = None
            
            return True
        except Exception as e:
            print(f"Error deteniendo juego: {e}")
            return False
    
    def get_available_profiles(self) -> list:
        """Retorna lista de perfiles disponibles"""
        return ['performance', 'balanced', 'power_saving']
    
    def get_running_processes(self):
        """Obtiene procesos en ejecución para seleccionar juegos"""
        return self.monitor.get_running_processes()
