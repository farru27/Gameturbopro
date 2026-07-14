"""
Estilos y temas para la interfaz gráfica
"""

class Styles:
    """Define estilos para la aplicación"""
    
    COLORS = {
        'dark': {
            'bg': '#1e1e1e',
            'fg': '#ffffff',
            'accent': '#00a8ff',
            'success': '#00d966',
            'warning': '#ffb800',
            'error': '#ff3838'
        },
        'light': {
            'bg': '#f5f5f5',
            'fg': '#000000',
            'accent': '#0078d4',
            'success': '#107c10',
            'warning': '#ffb900',
            'error': '#d13438'
        }
    }
    
    FONTS = {
        'title': ('Segoe UI', 24, 'bold'),
        'heading': ('Segoe UI', 14, 'bold'),
        'normal': ('Segoe UI', 10),
        'small': ('Segoe UI', 9)
    }
    
    SIZES = {
        'padding': 10,
        'margin': 5,
        'button_width': 150,
        'button_height': 40
    }


def get_theme(theme_name='dark'):
    """Obtiene la paleta de colores del tema"""
    return Styles.COLORS.get(theme_name, Styles.COLORS['dark'])
