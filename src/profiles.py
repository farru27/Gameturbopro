#!/usr/bin/env python3
"""
Sistema de perfiles avanzados y presets para Game Turbo Pro
"""

import json
from pathlib import Path
from typing import Dict, List

class ProfileManager:
    """Gestor de perfiles de optimización"""
    
    def __init__(self):
        self.profiles_dir = Path('profiles')
        self.profiles_dir.mkdir(exist_ok=True)
        self.current_profile = None
        self._create_default_profiles()
    
    def _create_default_profiles(self):
        """Crea perfiles por defecto"""
        default_profiles = {
            'performance': {
                'name': 'Máximo Rendimiento',
                'description': 'Prioriza FPS y velocidad',
                'icon': '⚡',
                'settings': {
                    'cpu_priority': 'realtime',
                    'gpu_enabled': True,
                    'boost_level': 100,
                    'fps_target': 144,
                    'temperature_limit': 85,
                    'ram_cleanup_interval': 60,
                    'background_processes': False,
                    'power_saving': False
                }
            },
            'balanced': {
                'name': 'Equilibrado',
                'description': 'Balance entre rendimiento y consumo',
                'icon': '⚖️',
                'settings': {
                    'cpu_priority': 'high',
                    'gpu_enabled': True,
                    'boost_level': 70,
                    'fps_target': 60,
                    'temperature_limit': 80,
                    'ram_cleanup_interval': 300,
                    'background_processes': True,
                    'power_saving': False
                }
            },
            'power_saving': {
                'name': 'Ahorro de Energía',
                'description': 'Minimiza consumo de recursos',
                'icon': '🔋',
                'settings': {
                    'cpu_priority': 'normal',
                    'gpu_enabled': False,
                    'boost_level': 30,
                    'fps_target': 30,
                    'temperature_limit': 75,
                    'ram_cleanup_interval': 600,
                    'background_processes': True,
                    'power_saving': True
                }
            },
            'esports': {
                'name': 'Esports',
                'description': 'Optimizado para competencia',
                'icon': '🏆',
                'settings': {
                    'cpu_priority': 'realtime',
                    'gpu_enabled': True,
                    'boost_level': 100,
                    'fps_target': 240,
                    'temperature_limit': 85,
                    'ram_cleanup_interval': 30,
                    'background_processes': False,
                    'power_saving': False
                }
            }
        }
        
        # Guardar perfiles si no existen
        for profile_name, profile_data in default_profiles.items():
            profile_file = self.profiles_dir / f"{profile_name}.json"
            if not profile_file.exists():
                self.save_profile(profile_name, profile_data)
    
    def save_profile(self, profile_name: str, profile_data: Dict) -> bool:
        """Guarda un perfil"""
        try:
            profile_file = self.profiles_dir / f"{profile_name}.json"
            with open(profile_file, 'w') as f:
                json.dump(profile_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error guardando perfil: {e}")
            return False
    
    def load_profile(self, profile_name: str) -> Dict:
        """Carga un perfil"""
        try:
            profile_file = self.profiles_dir / f"{profile_name}.json"
            with open(profile_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error cargando perfil: {e}")
            return {}
    
    def list_profiles(self) -> List[str]:
        """Lista todos los perfiles disponibles"""
        profiles = []
        for file in self.profiles_dir.glob('*.json'):
            profiles.append(file.stem)
        return profiles
    
    def create_custom_profile(self, profile_name: str, base_profile: str, overrides: Dict) -> bool:
        """Crea un perfil personalizado basado en uno existente"""
        base = self.load_profile(base_profile)
        if not base:
            return False
        
        custom = base.copy()
        custom['name'] = profile_name
        custom['settings'].update(overrides)
        
        return self.save_profile(profile_name, custom)
    
    def apply_profile(self, profile_name: str) -> Dict:
        """Aplica un perfil"""
        profile = self.load_profile(profile_name)
        if profile:
            self.current_profile = profile_name
            return profile.get('settings', {})
        return {}
    
    def get_profile_info(self, profile_name: str) -> Dict:
        """Obtiene información de un perfil"""
        profile = self.load_profile(profile_name)
        return {
            'name': profile.get('name', ''),
            'description': profile.get('description', ''),
            'icon': profile.get('icon', ''),
            'settings': profile.get('settings', {})
        }
