#!/usr/bin/env python3
"""
Sistema de logging y estadísticas para Game Turbo Pro
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class GameLogger:
    """Logger para sesiones de juegos"""
    
    def __init__(self):
        self.logs_dir = Path('logs')
        self.logs_dir.mkdir(exist_ok=True)
        self.current_session = None
    
    def start_session(self, game_name: str) -> str:
        """Inicia una nueva sesión de logging"""
        timestamp = datetime.now().isoformat()
        session_id = f"{game_name}_{timestamp.replace(':', '-')}"
        
        self.current_session = {
            'id': session_id,
            'game': game_name,
            'start_time': timestamp,
            'end_time': None,
            'duration': 0,
            'stats': [],
            'events': []
        }
        
        return session_id
    
    def log_stat(self, stat_name: str, value: float, unit: str = ''):
        """Registra una estadística"""
        if self.current_session:
            self.current_session['stats'].append({
                'timestamp': datetime.now().isoformat(),
                'name': stat_name,
                'value': value,
                'unit': unit
            })
    
    def log_event(self, event_name: str, description: str = ''):
        """Registra un evento"""
        if self.current_session:
            self.current_session['events'].append({
                'timestamp': datetime.now().isoformat(),
                'name': event_name,
                'description': description
            })
    
    def end_session(self) -> Dict:
        """Finaliza la sesión actual y guarda el log"""
        if self.current_session:
            self.current_session['end_time'] = datetime.now().isoformat()
            
            # Calcular duración
            start = datetime.fromisoformat(self.current_session['start_time'])
            end = datetime.fromisoformat(self.current_session['end_time'])
            self.current_session['duration'] = (end - start).total_seconds()
            
            # Guardar log
            self._save_session()
            
            session = self.current_session
            self.current_session = None
            return session
        return {}
    
    def _save_session(self):
        """Guarda la sesión actual en un archivo"""
        if self.current_session:
            log_file = self.logs_dir / f"{self.current_session['id']}.json"
            try:
                with open(log_file, 'w') as f:
                    json.dump(self.current_session, f, indent=2)
            except Exception as e:
                print(f"Error guardando log: {e}")
    
    def get_session_history(self, game_name: str = None) -> List[Dict]:
        """Obtiene historial de sesiones"""
        history = []
        try:
            for log_file in self.logs_dir.glob('*.json'):
                with open(log_file, 'r') as f:
                    session = json.load(f)
                    if game_name is None or session.get('game') == game_name:
                        history.append(session)
        except Exception as e:
            print(f"Error leyendo historial: {e}")
        
        return sorted(history, key=lambda x: x['start_time'], reverse=True)
    
    def get_statistics(self, game_name: str = None) -> Dict:
        """Calcula estadísticas agregadas"""
        history = self.get_session_history(game_name)
        
        if not history:
            return {}
        
        total_sessions = len(history)
        total_time = sum(s['duration'] for s in history)
        
        # Promedio de estadísticas
        avg_stats = {}
        if history and history[0]['stats']:
            stat_names = set(s['name'] for session in history for s in session['stats'])
            for stat_name in stat_names:
                values = []
                for session in history:
                    for stat in session['stats']:
                        if stat['name'] == stat_name:
                            values.append(stat['value'])
                if values:
                    avg_stats[stat_name] = {
                        'average': sum(values) / len(values),
                        'min': min(values),
                        'max': max(values)
                    }
        
        return {
            'total_sessions': total_sessions,
            'total_time': total_time,
            'average_session_time': total_time / total_sessions if total_sessions > 0 else 0,
            'average_stats': avg_stats
        }
