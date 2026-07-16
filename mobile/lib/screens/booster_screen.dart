import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:game_turbo_pro_mobile/utils/theme.dart';

class BoosterScreen extends StatefulWidget {
  const BoosterScreen({Key? key}) : super(key: key);

  @override
  State<BoosterScreen> createState() => _BoosterScreenState();
}

class _BoosterScreenState extends State<BoosterScreen> {
  bool _isBoostActive = false;
  int _boostLevel = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('⚡ Game Booster'),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(16.w),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Boost Toggle
              Card(
                child: Padding(
                  padding: EdgeInsets.all(20.w),
                  child: Column(
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'Estado Boost',
                            style: Theme.of(context).textTheme.titleLarge,
                          ),
                          Switch(
                            value: _isBoostActive,
                            onChanged: (value) {
                              setState(() => _isBoostActive = value);
                            },
                            activeColor: AppTheme.accentColor,
                          ),
                        ],
                      ),
                      SizedBox(height: 16.h),
                      if (_isBoostActive)
                        Container(
                          padding: EdgeInsets.symmetric(vertical: 12.h),
                          decoration: BoxDecoration(
                            color: AppTheme.successColor.withOpacity(0.2),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: const [
                              Icon(
                                Icons.check_circle,
                                color: AppTheme.successColor,
                              ),
                              SizedBox(width: 8),
                              Text(
                                'Boost Activo',
                                style: TextStyle(
                                  color: AppTheme.successColor,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ],
                          ),
                        )
                      else
                        Container(
                          padding: EdgeInsets.symmetric(vertical: 12.h),
                          decoration: BoxDecoration(
                            color: AppTheme.textSecondary.withOpacity(0.2),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: const [
                              Icon(
                                Icons.info,
                                color: AppTheme.textSecondary,
                              ),
                              SizedBox(width: 8),
                              Text(
                                'Boost Inactivo',
                                style: TextStyle(
                                  color: AppTheme.textSecondary,
                                ),
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),
                ),
              ),
              SizedBox(height: 20.h),
              // Boost Level
              Card(
                child: Padding(
                  padding: EdgeInsets.all(20.w),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Nivel de Boost',
                        style: Theme.of(context).textTheme.titleMedium,
                      ),
                      SizedBox(height: 16.h),
                      Slider(
                        value: _boostLevel.toDouble(),
                        min: 0,
                        max: 100,
                        activeColor: AppTheme.accentColor,
                        inactiveColor: AppTheme.borderColor,
                        onChanged: (value) {
                          setState(() => _boostLevel = value.toInt());
                        },
                      ),
                      Center(
                        child: Text(
                          '$_boostLevel%',
                          style: TextStyle(
                            color: AppTheme.accentColor,
                            fontSize: 28.sp,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              SizedBox(height: 20.h),
              // Características
              Text(
                'Características',
                style: Theme.of(context).textTheme.titleLarge,
              ),
              SizedBox(height: 12.h),
              _FeatureItem(
                icon: Icons.memory,
                title: 'Limpieza de RAM',
                description: 'Libera memoria no utilizada',
              ),
              _FeatureItem(
                icon: Icons.speed,
                title: 'Optimizar Velocidad',
                description: 'Acelera procesos críticos',
              ),
              _FeatureItem(
                icon: Icons.videogame_asset,
                title: 'Modo Gaming',
                description: 'Dedica recursos a juegos',
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _FeatureItem extends StatelessWidget {
  final IconData icon;
  final String title;
  final String description;

  const _FeatureItem({
    required this.icon,
    required this.title,
    required this.description,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(bottom: 12.h),
      padding: EdgeInsets.all(12.w),
      decoration: BoxDecoration(
        color: AppTheme.tertiaryBg,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        children: [
          Icon(icon, color: AppTheme.accentColor),
          SizedBox(width: 12.w),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: TextStyle(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  description,
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 12.sp,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
