#!/usr/bin/env python3
"""
Sistema de atajos de teclado para Game Turbo Pro
"""

from typing import Callable, Dict
import keyboard

class HotkeyManager:
    """Gestor de atajos de teclado"""
    
    def __init__(self):
        self.hotkeys = {}
        self.enabled = False
    
    def register_hotkey(self, key_combination: str, callback: Callable, description: str = ''):
        """Registra un atajo de teclado"""
        try:
            keyboard.add_hotkey(key_combination, callback)
            self.hotkeys[key_combination] = {
                'callback': callback,
                'description': description
            }
            return True
        except Exception as e:
            print(f"Error registrando hotkey: {e}")
            return False
    
    def unregister_hotkey(self, key_combination: str):
        """Desregistra un atajo de teclado"""
        try:
            keyboard.remove_hotkey(key_combination)
            if key_combination in self.hotkeys:
                del self.hotkeys[key_combination]
            return True
        except Exception as e:
            print(f"Error desregistrando hotkey: {e}")
            return False
    
    def get_hotkeys(self) -> Dict:
        """Obtiene lista de atajos registrados"""
        return {k: v['description'] for k, v in self.hotkeys.items()}
    
    def enable_all(self):
        """Habilita todos los atajos"""
        self.enabled = True
    
    def disable_all(self):
        """Deshabilita todos los atajos"""
        self.enabled = False
