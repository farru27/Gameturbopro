import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:game_turbo_pro_mobile/screens/booster_screen.dart';
import 'package:game_turbo_pro_mobile/screens/cooler_screen.dart';
import 'package:game_turbo_pro_mobile/screens/stats_screen.dart';
import 'package:game_turbo_pro_mobile/utils/theme.dart';
import 'package:game_turbo_pro_mobile/widgets/bottom_nav.dart';
import 'package:game_turbo_pro_mobile/widgets/stat_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  final List<Widget> _screens = [
    const _DashboardContent(),
    const BoosterScreen(),
    const CoolerScreen(),
    const StatsScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      bottomNavigationBar: BottomNav(
        selectedIndex: _selectedIndex,
        onItemSelected: (index) {
          setState(() => _selectedIndex = index);
        },
      ),
    );
  }
}

class _DashboardContent extends StatelessWidget {
  const _DashboardContent();

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Column(
        children: [
          // Header
          Container(
            padding: EdgeInsets.symmetric(horizontal: 20.w, vertical: 24.h),
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [AppTheme.secondaryBg, AppTheme.tertiaryBg],
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 16.h),
                Row(
                  children: [
                    const Icon(
                      Icons.games,
                      color: AppTheme.accentColor,
                      size: 32,
                    ),
                    SizedBox(width: 12.w),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          '🎮 GAME TURBO',
                          style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                            color: AppTheme.accentColor,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        Text(
                          'Rendimiento Máximo',
                          style: Theme.of(context).textTheme.bodySmall?.copyWith(
                            color: AppTheme.textSecondary,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ],
            ),
          ),
          // Contenido
          Padding(
            padding: EdgeInsets.symmetric(horizontal: 16.w, vertical: 20.h),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Quick Actions
                Text(
                  'Acciones Rápidas',
                  style: Theme.of(context).textTheme.titleLarge?.copyWith(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 12.h),
                Row(
                  children: [
                    Expanded(
                      child: _QuickActionButton(
                        icon: Icons.flash_on,
                        label: 'Boost',
                        color: AppTheme.warningColor,
                        onTap: () {},
                      ),
                    ),
                    SizedBox(width: 12.w),
                    Expanded(
                      child: _QuickActionButton(
                        icon: Icons.ac_unit,
                        label: 'Enfriar',
                        color: AppTheme.accentColor,
                        onTap: () {},
                      ),
                    ),
                    SizedBox(width: 12.w),
                    Expanded(
                      child: _QuickActionButton(
                        icon: Icons.delete,
                        label: 'Limpiar',
                        color: AppTheme.successColor,
                        onTap: () {},
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 24.h),
                // Sistema Stats
                Text(
                  'Estado del Sistema',
                  style: Theme.of(context).textTheme.titleLarge?.copyWith(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 12.h),
                StatCard(
                  title: '⚡ CPU',
                  value: '45%',
                  unit: 'uso',
                  color: AppTheme.accentColor,
                ),
                SizedBox(height: 10.h),
                StatCard(
                  title: '💾 RAM',
                  value: '62%',
                  unit: 'disponible',
                  color: AppTheme.warningColor,
                ),
                SizedBox(height: 10.h),
                StatCard(
                  title: '🧊 Temp',
                  value: '42°C',
                  unit: 'normal',
                  color: AppTheme.successColor,
                ),
                SizedBox(height: 10.h),
                StatCard(
                  title: '🔋 Batería',
                  value: '85%',
                  unit: 'cargada',
                  color: AppTheme.successColor,
                ),
                SizedBox(height: 24.h),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _QuickActionButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final Color color;
  final VoidCallback onTap;

  const _QuickActionButton({
    required this.icon,
    required this.label,
    required this.color,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: EdgeInsets.symmetric(vertical: 16.h),
        decoration: BoxDecoration(
          color: AppTheme.tertiaryBg,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: AppTheme.borderColor, width: 1),
        ),
        child: Column(
          children: [
            Icon(icon, color: color, size: 28),
            SizedBox(height: 8.h),
            Text(
              label,
              style: TextStyle(
                color: AppTheme.textPrimary,
                fontWeight: FontWeight.bold,
                fontSize: 12.sp,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
