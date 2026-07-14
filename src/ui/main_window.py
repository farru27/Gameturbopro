"""
Ventana principal de Game Turbo Pro
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from .styles import Styles, get_theme
from .widgets import ModernButton, ModernLabel, StatsFrame
from ..launcher import UnifiedLauncher
from ..config import config

class GameLauncherApp:
    """Aplicación principal del lanzador de juegos"""
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Game Turbo Pro')
        self.window.geometry('800x600')
        
        self.theme = config.get('theme', 'dark')
        colors = get_theme(self.theme)
        self.window.config(bg=colors['bg'])
        
        self.launcher = UnifiedLauncher()
        self.game_running = False
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Configura la interfaz de usuario"""
        colors = get_theme(self.theme)
        
        # Título
        title = ModernLabel(self.window, 'Game Turbo Pro 🎮', theme=self.theme, size='title')
        title.pack(pady=20)
        
        # Panel de control
        control_frame = tk.Frame(self.window, bg=colors['bg'])
        control_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Seleccionar juego
        game_frame = tk.Frame(control_frame, bg=colors['bg'])
        game_frame.pack(fill=tk.X, pady=10)
        
        ModernLabel(game_frame, 'Juego:', theme=self.theme).pack(side=tk.LEFT)
        self.game_path_var = tk.StringVar(value='Selecciona un juego...')
        game_label = ModernLabel(game_frame, '', theme=self.theme)
        self.game_path_var.trace('w', lambda *args: game_label.config(text=self.game_path_var.get().split('/')[-1]))
        game_label.pack(side=tk.LEFT, padx=10)
        
        browse_btn = ModernButton(game_frame, 'Examinar', command=self._select_game, theme=self.theme, width=10)
        browse_btn.pack(side=tk.RIGHT)
        
        # Perfil
        profile_frame = tk.Frame(control_frame, bg=colors['bg'])
        profile_frame.pack(fill=tk.X, pady=10)
        
        ModernLabel(profile_frame, 'Perfil:', theme=self.theme).pack(side=tk.LEFT)
        self.profile_var = tk.StringVar(value='balanced')
        profile_menu = tk.OptionMenu(profile_frame, self.profile_var, 'performance', 'balanced', 'power_saving')
        profile_menu.config(bg=colors['accent'], fg=colors['bg'])
        profile_menu.pack(side=tk.LEFT, padx=10)
        
        # Botones de control
        button_frame = tk.Frame(self.window, bg=colors['bg'])
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.launch_btn = ModernButton(button_frame, 'Lanzar Juego', command=self._launch_game, theme=self.theme, width=15)
        self.launch_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = ModernButton(button_frame, 'Detener', command=self._stop_game, theme=self.theme, width=15, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Panel de estadísticas
        stats_frame = tk.Frame(self.window, bg=colors['bg'])
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Frame izquierdo - Game Turbo
        turbo_frame = StatsFrame(stats_frame, 'Game Turbo', theme=self.theme)
        turbo_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.turbo_status_label = turbo_frame.add_stat('Estado', 'Inactivo', theme=self.theme)
        self.cpu_label = turbo_frame.add_stat('CPU', '0%', theme=self.theme)
        self.temp_label = turbo_frame.add_stat('Temperatura', '0°C', theme=self.theme)
        
        # Frame derecho - Game Booster
        booster_frame = StatsFrame(stats_frame, 'Game Booster', theme=self.theme)
        booster_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        self.booster_status_label = booster_frame.add_stat('Estado', 'Inactivo', theme=self.theme)
        self.memory_label = booster_frame.add_stat('Memoria', '0%', theme=self.theme)
        self.boost_label = booster_frame.add_stat('Nivel Boost', '0%', theme=self.theme)
        
        # Iniciar actualización de estadísticas
        self._update_stats()
    
    def _select_game(self):
        """Abre diálogo para seleccionar juego"""
        file_path = filedialog.askopenfilename(
            title='Selecciona ejecutable del juego',
            filetypes=[('Ejecutables', '*.exe *.sh *.app'), ('Todos', '*.*')]
        )
        if file_path:
            self.game_path_var.set(file_path)
    
    def _launch_game(self):
        """Lanza el juego seleccionado"""
        game_path = self.game_path_var.get()
        if game_path == 'Selecciona un juego...':
            messagebox.showwarning('Advertencia', 'Por favor selecciona un juego')
            return
        
        profile = self.profile_var.get()
        
        def launch_thread():
            success = self.launcher.launch_game(game_path, profile=profile)
            if success:
                self.game_running = True
                self.launch_btn.config(state=tk.DISABLED)
                self.stop_btn.config(state=tk.NORMAL)
            else:
                messagebox.showerror('Error', 'No se pudo lanzar el juego')
        
        threading.Thread(target=launch_thread, daemon=True).start()
    
    def _stop_game(self):
        """Detiene el juego en ejecución"""
        def stop_thread():
            self.launcher.stop_game()
            self.game_running = False
            self.launch_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
        
        threading.Thread(target=stop_thread, daemon=True).start()
    
    def _update_stats(self):
        """Actualiza las estadísticas mostradas"""
        if self.game_running:
            turbo_status = self.launcher.turbo.get_status()
            booster_status = self.launcher.booster.get_status()
            
            self.turbo_status_label.config(text='Activo' if turbo_status['active'] else 'Inactivo')
            self.booster_status_label.config(text='Activo' if booster_status['active'] else 'Inactivo')
            
            cpu_stats = self.launcher.turbo.get_cpu_stats()
            self.cpu_label.config(text=f"{cpu_stats['percent']:.1f}%")
            
            temp = self.launcher.turbo.get_temperature()
            self.temp_label.config(text=f"{temp:.1f}°C")
            
            mem_stats = self.launcher.booster.get_memory_stats()
            self.memory_label.config(text=f"{mem_stats['percent']:.1f}%")
            
            self.boost_label.config(text=f"{booster_status['boost_level']}%")
        
        self.window.after(1000, self._update_stats)
    
    def run(self):
        """Inicia la aplicación"""
        self.window.mainloop()
