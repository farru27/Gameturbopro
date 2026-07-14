"""
Ventana principal de Game Turbo Pro - Interfaz moderna
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
from .styles import ModernTheme
from .widgets import RoundedButton, StatsCard, ProgressBar, StatusIndicator, GlassPanel
from ..launcher import UnifiedLauncher
from ..config import config

class GameLauncherApp:
    """Aplicación principal del lanzador de juegos con diseño moderno"""
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Game Turbo Pro 🎮')
        self.window.geometry('1000x700')
        self.window.minsize(900, 600)
        
        self.theme = ModernTheme.DARK
        self.window.config(bg=self.theme['primary_bg'])
        
        self.launcher = UnifiedLauncher()
        self.game_running = False
        self.update_running = True
        
        # Configurar icono si existe
        try:
            self.window.iconphoto(False, tk.PhotoImage(file='icon.png'))
        except:
            pass
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Configura la interfaz de usuario moderna"""
        # Panel superior
        self._create_header()
        
        # Panel principal con dos columnas
        main_frame = tk.Frame(self.window, bg=self.theme['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Columna izquierda - Controles
        left_frame = tk.Frame(main_frame, bg=self.theme['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        self._create_control_panel(left_frame)
        
        # Columna derecha - Estadísticas
        right_frame = tk.Frame(main_frame, bg=self.theme['primary_bg'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        self._create_stats_panels(right_frame)
        
        # Panel inferior - Estado
        self._create_footer()
    
    def _create_header(self):
        """Crea el encabezado de la aplicación"""
        header = GlassPanel(self.window, theme=self.theme)
        header.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        content = tk.Frame(header, bg=self.theme['secondary_bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        title = tk.Label(
            content,
            text='🎮 GAME TURBO PRO',
            font=ModernTheme.FONTS['title'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['accent']
        )
        title.pack(anchor='w')
        
        subtitle = tk.Label(
            content,
            text='Lanzador de juegos con optimización de rendimiento avanzada',
            font=ModernTheme.FONTS['small'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_secondary']
        )
        subtitle.pack(anchor='w')
    
    def _create_control_panel(self, parent):
        """Crea el panel de controles"""
        control_card = StatsCard(parent, 'CONTROLES', '⚙️', theme=self.theme)
        control_card.pack(fill=tk.X, pady=(0, 15))
        
        # Seleccionar juego
        game_label = tk.Label(
            control_card.content_frame,
            text='Selecciona tu juego:',
            font=ModernTheme.FONTS['normal'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_primary']
        )
        game_label.pack(anchor='w', pady=(0, 8))
        
        self.game_path_var = tk.StringVar(value='Ningún juego seleccionado')
        game_display = tk.Label(
            control_card.content_frame,
            text='Ningún juego seleccionado',
            font=ModernTheme.FONTS['small'],
            bg=self.theme['tertiary_bg'],
            fg=self.theme['accent'],
            relief=tk.FLAT,
            padx=10,
            pady=8
        )
        game_display.pack(fill=tk.X, pady=(0, 10))
        
        def update_display(*args):
            path = self.game_path_var.get()
            display_text = path.split('/')[-1] if path != 'Ningún juego seleccionado' else path
            game_display.config(text=display_text)
        
        self.game_path_var.trace('w', update_display)
        
        # Botón examinar
        browse_btn = RoundedButton(
            control_card.content_frame,
            text='📁 EXAMINAR ARCHIVOS',
            command=self._select_game,
            width=140,
            height=40,
            theme=self.theme
        )
        browse_btn.pack(pady=10)
        
        # Perfil
        profile_label = tk.Label(
            control_card.content_frame,
            text='Perfil de optimización:',
            font=ModernTheme.FONTS['normal'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_primary']
        )
        profile_label.pack(anchor='w', pady=(20, 8))
        
        self.profile_var = tk.StringVar(value='balanced')
        
        profiles_frame = tk.Frame(control_card.content_frame, bg=self.theme['secondary_bg'])
        profiles_frame.pack(fill=tk.X, pady=10)
        
        profiles = [
            ('⚡ RENDIMIENTO', 'performance'),
            ('⚖️ EQUILIBRADO', 'balanced'),
            ('🔋 AHORRO', 'power_saving')
        ]
        
        for label, value in profiles:
            btn = tk.Radiobutton(
                profiles_frame,
                text=label,
                variable=self.profile_var,
                value=value,
                font=ModernTheme.FONTS['small'],
                bg=self.theme['secondary_bg'],
                fg=self.theme['text_primary'],
                selectcolor=self.theme['accent'],
                activebackground=self.theme['secondary_bg'],
                activeforeground=self.theme['accent'],
                relief=tk.FLAT,
                highlightthickness=0
            )
            btn.pack(anchor='w', pady=4)
        
        # Botones de acción
        button_frame = tk.Frame(control_card.content_frame, bg=self.theme['secondary_bg'])
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.launch_btn = RoundedButton(
            button_frame,
            text='▶️ LANZAR JUEGO',
            command=self._launch_game,
            width=150,
            height=45,
            theme=self.theme
        )
        self.launch_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.stop_btn = RoundedButton(
            button_frame,
            text='⏹️ DETENER',
            command=self._stop_game,
            width=150,
            height=45,
            theme=self.theme
        )
        self.stop_btn.pack(side=tk.LEFT)
        
        # Inicialmente deshabilitado
        self.stop_btn.config(state=tk.DISABLED)
    
    def _create_stats_panels(self, parent):
        """Crea los paneles de estadísticas"""
        # Game Turbo
        turbo_card = StatsCard(parent, 'GAME TURBO', '🚀', theme=self.theme)
        turbo_card.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.turbo_status = turbo_card.add_stat('Estado', 'Inactivo')
        self.cpu_stat = turbo_card.add_stat('CPU', '0', '%')
        self.temp_stat = turbo_card.add_stat('Temperatura', '0', '°C')
        self.processes_stat = turbo_card.add_stat('Procesos Activos', '0')
        
        # Game Booster
        booster_card = StatsCard(parent, 'GAME BOOSTER', '⚡', theme=self.theme)
        booster_card.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.booster_status = booster_card.add_stat('Estado', 'Inactivo')
        self.memory_stat = booster_card.add_stat('RAM', '0', '%')
        self.boost_level = booster_card.add_stat('Nivel Boost', '0', '%')
        self.fps_stat = booster_card.add_stat('FPS Objetivo', '60')
        
        # Monitor del Sistema
        monitor_card = StatsCard(parent, 'MONITOREO', '📊', theme=self.theme)
        monitor_card.pack(fill=tk.BOTH, expand=True)
        
        # CPU Progress
        tk.Label(
            monitor_card.content_frame,
            text='Uso de CPU:',
            font=ModernTheme.FONTS['small'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_secondary']
        ).pack(anchor='w', pady=(5, 2))
        
        self.cpu_progress = ProgressBar(monitor_card.content_frame, theme=self.theme, height=6)
        self.cpu_progress.pack(fill=tk.X, pady=(0, 10))
        
        # Memory Progress
        tk.Label(
            monitor_card.content_frame,
            text='Uso de RAM:',
            font=ModernTheme.FONTS['small'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_secondary']
        ).pack(anchor='w', pady=(5, 2))
        
        self.memory_progress = ProgressBar(monitor_card.content_frame, theme=self.theme, height=6)
        self.memory_progress.pack(fill=tk.X)
    
    def _create_footer(self):
        """Crea el pie de página"""
        footer = tk.Frame(self.window, bg=self.theme['secondary_bg'])
        footer.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Status indicator
        status_frame = tk.Frame(footer, bg=self.theme['secondary_bg'])
        status_frame.pack(anchor='w', padx=10, pady=10)
        
        self.status_indicator = StatusIndicator(status_frame, 'off', theme=self.theme)
        self.status_indicator.pack(side=tk.LEFT, padx=(0, 8))
        
        self.status_label = tk.Label(
            status_frame,
            text='Sistema listo',
            font=ModernTheme.FONTS['small'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_secondary']
        )
        self.status_label.pack(side=tk.LEFT)
    
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
        if game_path == 'Ningún juego seleccionado':
            messagebox.showwarning('Advertencia', '⚠️ Por favor selecciona un juego')
            return
        
        profile = self.profile_var.get()
        
        def launch_thread():
            success = self.launcher.launch_game(game_path, profile=profile)
            if success:
                self.game_running = True
                self.launch_btn.config(state=tk.DISABLED)
                self.stop_btn.config(state=tk.NORMAL)
                self.status_indicator.set_status('on')
                self.status_label.config(text='🎮 Juego en ejecución...')
            else:
                messagebox.showerror('Error', '❌ No se pudo lanzar el juego')
        
        threading.Thread(target=launch_thread, daemon=True).start()
    
    def _stop_game(self):
        """Detiene el juego en ejecución"""
        def stop_thread():
            self.launcher.stop_game()
            self.game_running = False
            self.launch_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.status_indicator.set_status('off')
            self.status_label.config(text='Sistema listo')
        
        threading.Thread(target=stop_thread, daemon=True).start()
    
    def _update_stats(self):
        """Actualiza las estadísticas mostradas"""
        if self.game_running:
            try:
                turbo_status = self.launcher.turbo.get_status()
                booster_status = self.launcher.booster.get_status()
                
                # Game Turbo
                self.turbo_status.config(text='🟢 Activo' if turbo_status['active'] else '🔴 Inactivo')
                
                cpu_stats = self.launcher.turbo.get_cpu_stats()
                self.cpu_stat.config(text=f"{cpu_stats['percent']:.1f}")
                self.cpu_progress.set_value(cpu_stats['percent'])
                
                temp = self.launcher.turbo.get_temperature()
                self.temp_stat.config(text=f"{temp:.1f}")
                
                # Game Booster
                self.booster_status.config(text='🟢 Activo' if booster_status['active'] else '🔴 Inactivo')
                
                mem_stats = self.launcher.booster.get_memory_stats()
                self.memory_stat.config(text=f"{mem_stats['percent']:.1f}")
                self.memory_progress.set_value(mem_stats['percent'])
                
                self.boost_level.config(text=f"{booster_status['boost_level']}")
                self.fps_stat.config(text=str(booster_status['fps_target']))
                
                # Procesos
                processes = self.launcher.monitor.get_running_processes()
                self.processes_stat.config(text=str(len(processes)))
            
            except Exception as e:
                print(f"Error actualizando stats: {e}")
        
        if self.update_running:
            self.window.after(1000, self._update_stats)
    
    def run(self):
        """Inicia la aplicación"""
        self._update_stats()
        self.window.mainloop()
        self.update_running = False
