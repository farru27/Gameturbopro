import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:game_turbo_pro_mobile/utils/theme.dart';

class StatsScreen extends StatelessWidget {
  const StatsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('📊 Estadísticas'),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(16.w),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _StatSection(
                title: 'Uso del Sistema',
                stats: [
                  _StatItem('CPU', '45%', AppTheme.accentColor),
                  _StatItem('RAM', '62%', AppTheme.warningColor),
                  _StatItem('Almacenamiento', '78%', AppTheme.warningColor),
                  _StatItem('Batería', '85%', AppTheme.successColor),
                ],
              ),
              SizedBox(height: 20.h),
              _StatSection(
                title: 'Procesos Principales',
                stats: [
                  _StatItem('YouTube', '245 MB', AppTheme.accentColor),
                  _StatItem('Chrome', '189 MB', AppTheme.accentColor),
                  _StatItem('Instagram', '156 MB', AppTheme.accentColor),
                  _StatItem('Otros', '410 MB', AppTheme.warningColor),
                ],
              ),
              SizedBox(height: 20.h),
              _StatSection(
                title: 'Temperatura por Sensor',
                stats: [
                  _StatItem('Procesador', '42°C', AppTheme.successColor),
                  _StatItem('Batería', '38°C', AppTheme.successColor),
                  _StatItem('GPU', '45°C', AppTheme.successColor),
                  _StatItem('Sensor Frontal', '35°C', AppTheme.successColor),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _StatSection extends StatelessWidget {
  final String title;
  final List<_StatItem> stats;

  const _StatSection({
    required this.title,
    required this.stats,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title,
          style: Theme.of(context).textTheme.titleLarge?.copyWith(
            fontWeight: FontWeight.bold,
          ),
        ),
        SizedBox(height: 12.h),
        Card(
          child: Padding(
            padding: EdgeInsets.all(12.w),
            child: Column(
              children: stats
                  .asMap()
                  .entries
                  .map((entry) => Column(
                    children: [
                      _StatRow(
                        label: entry.value.label,
                        value: entry.value.value,
                        color: entry.value.color,
                      ),
                      if (entry.key < stats.length - 1)
                        Divider(
                          color: AppTheme.borderColor,
                          height: 12.h,
                        ),
                    ],
                  ))
                  .toList(),
            ),
          ),
        ),
      ],
    );
  }
}

class _StatItem {
  final String label;
  final String value;
  final Color color;

  _StatItem(this.label, this.value, this.color);
}

class _StatRow extends StatelessWidget {
  final String label;
  final String value;
  final Color color;

  const _StatRow({
    required this.label,
    required this.value,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 8.h),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            label,
            style: TextStyle(color: AppTheme.textSecondary),
          ),
          Text(
            value,
            style: TextStyle(
              color: color,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}
