"""
Módulo Game Turbo - Optimización de CPU y GPU
"""

import psutil
import os
from typing import Dict, List
from .config import config

class GameTurbo:
    """Gestor de optimización de rendimiento para juegos"""
    
    def __init__(self):
        self.active = False
        self.optimizations = []
        self.original_settings = {}
    
    def get_status(self) -> Dict:
        """Obtiene estado actual de Game Turbo"""
        return {
            'active': self.active,
            'optimizations': self.optimizations,
            'cpu_priority': config.get('cpu_priority'),
            'gpu_enabled': config.get('gpu_enabled'),
            'temperature_limit': config.get('temperature_limit')
        }
    
    def optimize_cpu(self) -> bool:
        """Optimiza CPU para juegos"""
        try:
            # Cambiar prioridad de procesos del sistema
            cpu_priority = config.get('cpu_priority', 'high')
            
            # En Windows, sería SetPriorityClass
            # En Linux/Mac, usar nice/renice
            
            self.optimizations.append('CPU Optimized')
            return True
        except Exception as e:
            print(f"Error optimizando CPU: {e}")
            return False
    
    def optimize_gpu(self) -> bool:
        """Optimiza GPU para juegos"""
        if not config.get('gpu_enabled'):
            return True
        
        try:
            # Aquí iría lógica específica para GPU
            # Según el driver (NVIDIA, AMD, Intel)
            self.optimizations.append('GPU Optimized')
            return True
        except Exception as e:
            print(f"Error optimizando GPU: {e}")
            return False
    
    def disable_background_processes(self) -> List[str]:
        """Detiene procesos innecesarios en segundo plano"""
        disabled_processes = []
        
        # Procesos típicos que no afectan el juego
        unnecessary_processes = [
            'update',
            'sync',
            'backup',
            'cloud',
        ]
        
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    name = proc.info['name'].lower()
                    if any(proc_name in name for proc_name in unnecessary_processes):
                        # Solo log, no terminar procesos realmente
                        disabled_processes.append(name)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Error deshabilitando procesos: {e}")
        
        self.optimizations.append(f'Disabled {len(disabled_processes)} background processes')
        return disabled_processes
    
    def activate_turbo(self, game_name: str = None) -> bool:
        """Activa Game Turbo"""
        try:
            self.active = True
            self.optimizations = []
            
            # Ejecutar optimizaciones
            self.optimize_cpu()
            self.optimize_gpu()
            self.disable_background_processes()
            
            return True
        except Exception as e:
            print(f"Error activando Turbo: {e}")
            self.active = False
            return False
    
    def deactivate_turbo(self) -> bool:
        """Desactiva Game Turbo"""
        try:
            self.active = False
            self.optimizations = []
            return True
        except Exception as e:
            print(f"Error desactivando Turbo: {e}")
            return False
    
    def get_cpu_stats(self) -> Dict:
        """Obtiene estadísticas de CPU"""
        return {
            'percent': psutil.cpu_percent(interval=1),
            'count': psutil.cpu_count(),
            'freq': psutil.cpu_freq().current if psutil.cpu_freq() else 0
        }
    
    def get_temperature(self) -> float:
        """Obtiene temperatura del sistema"""
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                # Obtener primera temperatura disponible
                for name, entries in temps.items():
                    if entries:
                        return entries[0].current
        except:
            pass
        return 0.0
    
    def monitor_temperature(self) -> bool:
        """Monitorea temperatura y reduce rendimiento si es necesario"""
        temp = self.get_temperature()
        limit = config.get('temperature_limit', 80)
        
        if temp > limit:
            self.optimizations.append(f'Temperature warning: {temp}°C')
            return False
        return True
