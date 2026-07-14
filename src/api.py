#!/usr/bin/env python3
"""
API REST para Game Turbo Pro (opcional)
"""

from flask import Flask, jsonify, request
from typing import Dict

class GameTurboAPI:
    """API REST para Game Turbo Pro"""
    
    def __init__(self, launcher):
        self.app = Flask(__name__)
        self.launcher = launcher
        self._setup_routes()
    
    def _setup_routes(self):
        """Configura las rutas de la API"""
        
        @self.app.route('/api/status', methods=['GET'])
        def get_status():
            return jsonify(self.launcher.get_combined_status())
        
        @self.app.route('/api/launch', methods=['POST'])
        def launch_game():
            data = request.json
            success = self.launcher.launch_game(
                data.get('game_path'),
                data.get('game_name'),
                data.get('profile', 'balanced')
            )
            return jsonify({'success': success})
        
        @self.app.route('/api/stop', methods=['POST'])
        def stop_game():
            success = self.launcher.stop_game()
            return jsonify({'success': success})
        
        @self.app.route('/api/profiles', methods=['GET'])
        def get_profiles():
            profiles = self.launcher.get_available_profiles()
            return jsonify({'profiles': profiles})
        
        @self.app.route('/api/processes', methods=['GET'])
        def get_processes():
            processes = self.launcher.get_running_processes()
            return jsonify({'processes': processes})
    
    def run(self, host='localhost', port=5000, debug=False):
        """Inicia el servidor API"""
        self.app.run(host=host, port=port, debug=debug)
