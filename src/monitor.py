"""
Monitor del sistema en tiempo real
"""

import psutil
import threading
from datetime import datetime
from typing import Dict, Callable

class SystemMonitor:
    """Monitorea recursos del sistema"""
    
    def __init__(self):
        self.running = False
        self.callbacks = []
        self.monitor_thread = None
        self.update_interval = 1  # segundos
    
    def register_callback(self, callback: Callable):
        """Registra una función de callback para actualizaciones"""
        self.callbacks.append(callback)
    
    def get_system_stats(self) -> Dict:
        """Obtiene estadísticas actuales del sistema"""
        try:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Temperatura (si está disponible)
            temp = None
            try:
                temp = psutil.sensors_temperatures()
            except:
                pass
            
            return {
                'timestamp': datetime.now().isoformat(),
                'cpu': {
                    'percent': cpu_percent,
                    'count': psutil.cpu_count(),
                    'freq': psutil.cpu_freq().current if psutil.cpu_freq() else 0
                },
                'memory': {
                    'used': memory.used,
                    'total': memory.total,
                    'percent': memory.percent,
                    'available': memory.available
                },
                'disk': {
                    'used': disk.used,
                    'total': disk.total,
                    'percent': disk.percent
                },
                'processes': len(psutil.pids()),
                'temperature': temp
            }
        except Exception as e:
            print(f"Error monitoreando sistema: {e}")
            return {}
    
    def start(self):
        """Inicia el monitoreo"""
        if not self.running:
            self.running = True
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()
    
    def stop(self):
        """Detiene el monitoreo"""
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
    
    def _monitor_loop(self):
        """Loop de monitoreo"""
        while self.running:
            try:
                stats = self.get_system_stats()
                for callback in self.callbacks:
                    try:
                        callback(stats)
                    except Exception as e:
                        print(f"Error en callback: {e}")
                
                import time
                time.sleep(self.update_interval)
            except Exception as e:
                print(f"Error en monitor loop: {e}")
    
    def get_running_processes(self):
        """Obtiene lista de procesos en ejecución"""
        processes = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
                try:
                    processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'memory': proc.info['memory_percent'],
                        'cpu': proc.info['cpu_percent']
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Error obteniendo procesos: {e}")
        
        return sorted(processes, key=lambda x: x['memory'], reverse=True)
