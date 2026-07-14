"""
Componentes personalizados modernos para Game Turbo Pro
"""

import tkinter as tk
from tkinter import ttk
from .styles import ModernTheme
import math

class RoundedButton(tk.Canvas):
    """Botón con esquinas redondeadas"""
    
    def __init__(self, parent, text='', command=None, width=160, height=45, theme=None, **kwargs):
        self.theme = theme or ModernTheme.DARK
        self.text = text
        self.command = command
        self.hover = False
        
        super().__init__(
            parent,
            width=width,
            height=height,
            bg=self.theme['primary_bg'],
            highlightthickness=0,
            **kwargs
        )
        
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        self.bind('<Button-1>', self._on_click)
        
        self.pack_propagate(False)
        self._draw()
    
    def _draw(self):
        """Dibuja el botón"""
        self.delete('all')
        
        color = self.theme['accent_hover'] if self.hover else self.theme['accent']
        radius = 10
        
        x1, y1 = 0, 0
        x2, y2 = self.winfo_width(), self.winfo_height()
        
        self.create_arc((x1, y1, x1+2*radius, y1+2*radius), start=90, extent=90, fill=color, outline=color)
        self.create_arc((x2-2*radius, y1, x2, y1+2*radius), start=0, extent=90, fill=color, outline=color)
        self.create_arc((x2-2*radius, y2-2*radius, x2, y2), start=270, extent=90, fill=color, outline=color)
        self.create_arc((x1, y2-2*radius, x1+2*radius, y2), start=180, extent=90, fill=color, outline=color)
        
        self.create_rectangle((x1+radius, y1, x2-radius, y2), fill=color, outline=color)
        self.create_rectangle((x1, y1+radius, x2, y2-radius), fill=color, outline=color)
        
        self.create_text(self.winfo_width()//2, self.winfo_height()//2, 
                        text=self.text, 
                        font=ModernTheme.FONTS['normal'],
                        fill=self.theme['primary_bg'])
    
    def _on_enter(self, event):
        self.hover = True
        self._draw()
    
    def _on_leave(self, event):
        self.hover = False
        self._draw()
    
    def _on_click(self, event):
        if self.command:
            self.command()


class StatsCard(tk.Frame):
    """Tarjeta de estadísticas moderna"""
    
    def __init__(self, parent, title='', icon='📊', theme=None, **kwargs):
        self.theme = theme or ModernTheme.DARK
        super().__init__(parent, bg=self.theme['secondary_bg'], **kwargs)
        
        # Configurar bordes
        self.config(relief=tk.FLAT, borderwidth=1, highlightthickness=1, highlightbackground=self.theme['border'])
        
        # Título con icono
        title_frame = tk.Frame(self, bg=self.theme['secondary_bg'])
        title_frame.pack(fill=tk.X, padx=15, pady=12)
        
        title_label = tk.Label(
            title_frame,
            text=f'{icon} {title}',
            font=ModernTheme.FONTS['heading'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['accent']
        )
        title_label.pack(anchor='w')
        
        # Contenedor de contenido
        self.content_frame = tk.Frame(self, bg=self.theme['secondary_bg'])
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=0, ipady=10)
        
        self.stats = {}
    
    def add_stat(self, name, value='0', unit=''):
        """Añade una estadística"""
        stat_frame = tk.Frame(self.content_frame, bg=self.theme['secondary_bg'])
        stat_frame.pack(fill=tk.X, pady=8)
        
        name_label = tk.Label(
            stat_frame,
            text=name,
            font=ModernTheme.FONTS['small'],
            bg=self.theme['secondary_bg'],
            fg=self.theme['text_secondary']
        )
        name_label.pack(anchor='w')
        
        value_frame = tk.Frame(stat_frame, bg=self.theme['secondary_bg'])
        value_frame.pack(fill=tk.X)
        
        value_label = tk.Label(
            value_frame,
            text=value,
            font=('Segoe UI', 16, 'bold'),
            bg=self.theme['secondary_bg'],
            fg=self.theme['accent']
        )
        value_label.pack(side=tk.LEFT)
        
        if unit:
            unit_label = tk.Label(
                value_frame,
                text=f' {unit}',
                font=ModernTheme.FONTS['normal'],
                bg=self.theme['secondary_bg'],
                fg=self.theme['text_secondary']
            )
            unit_label.pack(side=tk.LEFT)
        
        self.stats[name] = value_label
        return value_label
    
    def update_stat(self, name, value):
        """Actualiza el valor de una estadística"""
        if name in self.stats:
            self.stats[name].config(text=str(value))


class ProgressBar(tk.Frame):
    """Barra de progreso moderna"""
    
    def __init__(self, parent, value=0, max_value=100, height=8, theme=None, **kwargs):
        self.theme = theme or ModernTheme.DARK
        self.value = value
        self.max_value = max_value
        self.height = height
        
        super().__init__(parent, bg=self.theme['tertiary_bg'], height=height, **kwargs)
        self.pack_propagate(False)
        
        self.canvas = tk.Canvas(
            self,
            bg=self.theme['secondary_bg'],
            highlightthickness=0,
            height=height
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self._draw_progress)
    
    def set_value(self, value):
        """Establece el valor del progreso"""
        self.value = min(max(value, 0), self.max_value)
        self._draw_progress()
    
    def _draw_progress(self, event=None):
        """Dibuja la barra de progreso"""
        self.canvas.delete('all')
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Fondo
        self.canvas.create_rectangle(0, 0, width, height, fill=self.theme['tertiary_bg'], outline='none')
        
        # Progreso
        progress_width = (self.value / self.max_value) * width
        
        # Determinar color según valor
        if self.value < 40:
            color = self.theme['success']
        elif self.value < 70:
            color = self.theme['warning']
        else:
            color = self.theme['error']
        
        self.canvas.create_rectangle(0, 0, progress_width, height, fill=color, outline='none')


class StatusIndicator(tk.Canvas):
    """Indicador de estado (online/offline)"""
    
    def __init__(self, parent, status='off', theme=None, size=12, **kwargs):
        self.theme = theme or ModernTheme.DARK
        self.status = status
        self.size = size
        
        super().__init__(
            parent,
            width=size,
            height=size,
            bg='transparent',
            highlightthickness=0,
            **kwargs
        )
        self._draw()
    
    def set_status(self, status):
        """Cambia el estado"""
        self.status = status
        self._draw()
    
    def _draw(self):
        """Dibuja el indicador"""
        self.delete('all')
        
        color = self.theme['success'] if self.status == 'on' else self.theme['text_secondary']
        self.create_oval(2, 2, self.size-2, self.size-2, fill=color, outline=color)


class GlassPanel(tk.Frame):
    """Panel con efecto de cristal"""
    
    def __init__(self, parent, theme=None, **kwargs):
        self.theme = theme or ModernTheme.DARK
        super().__init__(parent, bg=self.theme['secondary_bg'], **kwargs)
        
        self.config(
            relief=tk.FLAT,
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.theme['border'],
            highlightcolor=self.theme['accent']
        )
