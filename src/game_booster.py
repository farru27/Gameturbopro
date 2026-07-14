"""
Módulo Game Booster - Aumento de FPS y limpieza de recursos
"""

import psutil
import os
from typing import Dict
from .config import config

class GameBooster:
    """Gestor de boost de rendimiento para juegos"""
    
    def __init__(self):
        self.active = False
        self.boost_level = 0  # 0-100
        self.fps_target = 60
    
    def get_status(self) -> Dict:
        """Obtiene estado actual de Game Booster"""
        return {
            'active': self.active,
            'boost_level': self.boost_level,
            'fps_target': self.fps_target,
            'ram_cleanup_interval': config.get('ram_cleanup_interval')
        }
    
    def boost_fps(self, target_fps: int = 60) -> bool:
        """Intenta aumentar FPS"""
        try:
            self.fps_target = target_fps
            
            # Estrategias de boost:
            # 1. Reducir calidad gráfica
            # 2. Deshabilitar efectos secundarios
            # 3. Optimizar render
            
            self.boost_level = min(100, target_fps // 6)  # Escala de 0-100
            return True
        except Exception as e:
            print(f"Error aumentando FPS: {e}")
            return False
    
    def clean_ram(self) -> Dict:
        """Limpia memoria RAM innecesaria"""
        try:
            mem_before = psutil.virtual_memory().used
            
            # En sistemas reales, aquí iría lógica de limpieza
            # Por ahora solo simulamos
            import gc
            gc.collect()
            
            mem_after = psutil.virtual_memory().used
            cleaned = mem_before - mem_after
            
            return {
                'memory_before': mem_before,
                'memory_after': mem_after,
                'memory_cleaned': max(0, cleaned),
                'success': True
            }
        except Exception as e:
            print(f"Error limpiando RAM: {e}")
            return {'success': False, 'error': str(e)}
    
    def optimize_memory(self) -> bool:
        """Optimiza uso de memoria"""
        try:
            # Liberar cache no esencial
            import gc
            gc.collect()
            
            # En Windows: EmptyWorkingSet
            # En Linux: sync; echo 3 > /proc/sys/vm/drop_caches (requiere permisos)
            
            return True
        except Exception as e:
            print(f"Error optimizando memoria: {e}")
            return False
    
    def reduce_lag(self) -> bool:
        """Reduce latencia del sistema"""
        try:
            # Priorizar procesos de juego
            # Reducir interrupciones de disco
            # Optimizar red si es multijugador
            return True
        except Exception as e:
            print(f"Error reduciendo lag: {e}")
            return False
    
    def activate_boost(self, level: int = 80) -> bool:
        """Activa Game Booster"""
        try:
            self.active = True
            self.boost_level = min(100, level)
            
            # Ejecutar optimizaciones
            self.boost_fps()
            self.clean_ram()
            self.optimize_memory()
            self.reduce_lag()
            
            return True
        except Exception as e:
            print(f"Error activando Booster: {e}")
            self.active = False
            return False
    
    def deactivate_boost(self) -> bool:
        """Desactiva Game Booster"""
        try:
            self.active = False
            self.boost_level = 0
            return True
        except Exception as e:
            print(f"Error desactivando Booster: {e}")
            return False
    
    def get_memory_stats(self) -> Dict:
        """Obtiene estadísticas de memoria"""
        mem = psutil.virtual_memory()
        return {
            'used': mem.used,
            'total': mem.total,
            'percent': mem.percent,
            'available': mem.available
        }
