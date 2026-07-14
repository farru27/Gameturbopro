"""
Estilos y temas modernos para Game Turbo Pro
"""

import tkinter as tk
from tkinter import ttk

class ModernTheme:
    """Define temas modernos para la aplicación"""
    
    # Tema Oscuro Premium
    DARK = {
        'primary_bg': '#0a0e27',
        'secondary_bg': '#1a1f3a',
        'tertiary_bg': '#242942',
        'accent': '#00d4ff',
        'accent_hover': '#00e6ff',
        'success': '#00ff85',
        'warning': '#ffb700',
        'error': '#ff3838',
        'text_primary': '#ffffff',
        'text_secondary': '#a0a9c3',
        'border': '#2a3f5f',
        'shadow': '#00000040'
    }
    
    # Fuentes modernas
    FONTS = {
        'title': ('Segoe UI', 28, 'bold'),
        'subtitle': ('Segoe UI', 18, 'bold'),
        'heading': ('Segoe UI', 14, 'bold'),
        'normal': ('Segoe UI', 11),
        'small': ('Segoe UI', 9),
        'mono': ('Courier New', 10)
    }
    
    # Tamaños
    SIZES = {
        'padding': 15,
        'margin': 10,
        'border_radius': 8,
        'button_width': 160,
        'button_height': 45
    }
