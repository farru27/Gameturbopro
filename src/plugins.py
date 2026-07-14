#!/usr/bin/env python3
"""
Game Turbo Pro - Sistema de plugins y extensiones
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Callable

class PluginManager:
    """Gestor de plugins para Game Turbo Pro"""
    
    def __init__(self):
        self.plugins = {}
        self.hooks = {}
        self.plugin_dir = Path('plugins')
        self.plugin_dir.mkdir(exist_ok=True)
    
    def register_plugin(self, name: str, plugin_class):
        """Registra un plugin"""
        try:
            instance = plugin_class()
            self.plugins[name] = instance
            print(f"✓ Plugin registrado: {name}")
            return True
        except Exception as e:
            print(f"✗ Error registrando plugin {name}: {e}")
            return False
    
    def register_hook(self, hook_name: str, callback: Callable):
        """Registra un hook/callback"""
        if hook_name not in self.hooks:
            self.hooks[hook_name] = []
        self.hooks[hook_name].append(callback)
    
    def execute_hook(self, hook_name: str, *args, **kwargs):
        """Ejecuta todos los callbacks registrados para un hook"""
        if hook_name in self.hooks:
            for callback in self.hooks[hook_name]:
                try:
                    callback(*args, **kwargs)
                except Exception as e:
                    print(f"Error ejecutando hook {hook_name}: {e}")
    
    def get_plugin(self, name: str):
        """Obtiene un plugin por nombre"""
        return self.plugins.get(name)
    
    def list_plugins(self) -> List[str]:
        """Lista todos los plugins cargados"""
        return list(self.plugins.keys())


class BasePlugin:
    """Clase base para todos los plugins"""
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.version = "1.0.0"
        self.enabled = True
    
    def on_enable(self):
        """Se ejecuta cuando el plugin se habilita"""
        pass
    
    def on_disable(self):
        """Se ejecuta cuando el plugin se deshabilita"""
        pass
    
    def on_game_launch(self, game_info):
        """Se ejecuta cuando se lanza un juego"""
        pass
    
    def on_game_stop(self, game_info):
        """Se ejecuta cuando se detiene un juego"""
        pass
