import 'package:flutter/material.dart';

class AppTheme {
  // Colores
  static const Color primaryBg = Color(0xFF0a0e27);
  static const Color secondaryBg = Color(0xFF1a1f3a);
  static const Color tertiaryBg = Color(0xFF242942);
  static const Color accentColor = Color(0xFF00d4ff);
  static const Color accentHover = Color(0xFF00e6ff);
  static const Color successColor = Color(0xFF00ff85);
  static const Color warningColor = Color(0xFFffb700);
  static const Color errorColor = Color(0xFFff3838);
  static const Color textPrimary = Color(0xFFffffff);
  static const Color textSecondary = Color(0xFFa0a9c3);
  static const Color borderColor = Color(0xFF2a3f5f);

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      primaryColor: accentColor,
      scaffoldBackgroundColor: primaryBg,
      appBarTheme: const AppBarTheme(
        backgroundColor: secondaryBg,
        elevation: 0,
        centerTitle: true,
      ),
      cardTheme: CardTheme(
        color: secondaryBg,
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: accentColor,
          foregroundColor: primaryBg,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
        ),
      ),
    );
  }
}
