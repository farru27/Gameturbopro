#!/usr/bin/env python3
"""
Integración con plataformas de juegos populares
"""

import os
import json
from pathlib import Path
from typing import List, Dict

class GameDetector:
    """Detecta juegos instalados en el sistema"""
    
    def __init__(self):
        self.detected_games = []
    
    def detect_steam_games(self) -> List[Dict]:
        """Detecta juegos instalados en Steam"""
        steam_paths = self._get_steam_paths()
        games = []
        
        for steam_path in steam_paths:
            games_dir = Path(steam_path) / 'steamapps' / 'common'
            if games_dir.exists():
                for game_folder in games_dir.iterdir():
                    if game_folder.is_dir():
                        # Buscar ejecutable
                        exe_file = self._find_executable(game_folder)
                        if exe_file:
                            games.append({
                                'name': game_folder.name,
                                'path': str(exe_file),
                                'platform': 'Steam',
                                'icon': '🎮'
                            })
        
        return games
    
    def detect_epic_games(self) -> List[Dict]:
        """Detecta juegos instalados en Epic Games"""
        games = []
        epic_path = Path(os.path.expanduser('~')) / '.config' / 'Epic'
        
        if epic_path.exists():
            # Lógica para detectar juegos de Epic
            pass
        
        return games
    
    def detect_installed_games(self) -> List[Dict]:
        """Detecta todos los juegos instalados en el sistema"""
        all_games = []
        
        # Steam
        all_games.extend(self.detect_steam_games())
        
        # Epic Games
        all_games.extend(self.detect_epic_games())
        
        self.detected_games = all_games
        return all_games
    
    def _get_steam_paths(self) -> List[str]:
        """Obtiene rutas de instalación de Steam"""
        paths = []
        
        # Windows
        if os.name == 'nt':
            common_paths = [
                'C:\\Program Files (x86)\\Steam',
                'C:\\Program Files\\Steam',
                'D:\\SteamLibrary'
            ]
            for path in common_paths:
                if Path(path).exists():
                    paths.append(path)
        
        # Linux
        else:
            linux_path = Path(os.path.expanduser('~')) / '.steam' / 'steam'
            if linux_path.exists():
                paths.append(str(linux_path))
        
        return paths
    
    def _find_executable(self, directory: Path):
        """Busca un ejecutable en un directorio"""
        for file in directory.iterdir():
            if file.is_file():
                if file.suffix.lower() in ['.exe', '.sh', '.app']:
                    return file
        return None
    
    def get_game_list(self) -> List[Dict]:
        """Obtiene lista de juegos detectados"""
        if not self.detected_games:
            self.detect_installed_games()
        return self.detected_games
