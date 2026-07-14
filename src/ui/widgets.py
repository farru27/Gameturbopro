"""
Componentes personalizados para la UI
"""

import tkinter as tk
from tkinter import ttk
from .styles import Styles, get_theme

class ModernButton(tk.Button):
    """Botón personalizado"""
    
    def __init__(self, parent, text, command=None, width=15, height=2, theme='dark', **kwargs):
        colors = get_theme(theme)
        super().__init__(
            parent,
            text=text,
            command=command,
            width=width,
            height=height,
            bg=colors['accent'],
            fg=colors['bg'],
            font=Styles.FONTS['normal'],
            relief=tk.FLAT,
            cursor='hand2',
            **kwargs
        )


class ModernLabel(tk.Label):
    """Etiqueta personalizada"""
    
    def __init__(self, parent, text, theme='dark', size='normal', **kwargs):
        colors = get_theme(theme)
        super().__init__(
            parent,
            text=text,
            bg=colors['bg'],
            fg=colors['fg'],
            font=Styles.FONTS[size],
            **kwargs
        )


class StatsFrame(tk.Frame):
    """Marco para mostrar estadísticas"""
    
    def __init__(self, parent, title, theme='dark', **kwargs):
        colors = get_theme(theme)
        super().__init__(parent, bg=colors['bg'], **kwargs)
        
        title_label = ModernLabel(self, title, theme=theme, size='heading')
        title_label.pack(fill=tk.X, pady=5)
        
        self.content_frame = tk.Frame(self, bg=colors['bg'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
    
    def add_stat(self, label_text, value_text, theme='dark'):
        """Añade una estadística al marco"""
        colors = get_theme(theme)
        
        stat_frame = tk.Frame(self.content_frame, bg=colors['bg'])
        stat_frame.pack(fill=tk.X, pady=2)
        
        label = ModernLabel(stat_frame, label_text + ':', theme=theme, size='small')
        label.pack(side=tk.LEFT)
        
        value = ModernLabel(stat_frame, value_text, theme=theme, size='small')
        value.pack(side=tk.RIGHT)
        
        return value
