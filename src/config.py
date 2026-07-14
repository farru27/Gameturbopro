"""
Configuración centralizada de Game Turbo Pro
"""

import json
import os
from pathlib import Path

class Config:
    """Gestiona la configuración de la aplicación"""
    
    def __init__(self):
        self.config_dir = Path(os.path.expanduser('~/.gameturbopro'))
        self.config_file = self.config_dir / 'config.json'
        self.profiles_file = self.config_dir / 'profiles.json'
        
        # Crear directorio si no existe
        self.config_dir.mkdir(exist_ok=True)
        
        # Configuración por defecto
        self.defaults = {
            'cpu_priority': 'high',
            'gpu_enabled': True,
            'temperature_limit': 80,
            'ram_cleanup_interval': 300,  # 5 minutos
            'fps_target': 60,
            'background_processes': True,
            'theme': 'dark'
        }
        
        self.config = self._load_config()
    
    def _load_config(self):
        """Carga la configuración desde archivo"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error cargando configuración: {e}")
        return self.defaults.copy()
    
    def save_config(self):
        """Guarda la configuración en archivo"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error guardando configuración: {e}")
    
    def get(self, key, default=None):
        """Obtiene un valor de configuración"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Establece un valor de configuración"""
        self.config[key] = value
        self.save_config()
    
    def get_profiles(self):
        """Obtiene los perfiles de juegos guardados"""
        if self.profiles_file.exists():
            try:
                with open(self.profiles_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error cargando perfiles: {e}")
        return {}
    
    def save_profiles(self, profiles):
        """Guarda los perfiles de juegos"""
        try:
            with open(self.profiles_file, 'w') as f:
                json.dump(profiles, f, indent=2)
        except Exception as e:
            print(f"Error guardando perfiles: {e}")


# Instancia global
config = Config()
