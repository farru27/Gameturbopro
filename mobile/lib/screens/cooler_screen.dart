import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:game_turbo_pro_mobile/utils/theme.dart';

class CoolerScreen extends StatefulWidget {
  const CoolerScreen({Key? key}) : super(key: key);

  @override
  State<CoolerScreen> createState() => _CoolerScreenState();
}

class _CoolerScreenState extends State<CoolerScreen> {
  double _currentTemp = 42.0;
  double _maxTemp = 85.0;
  bool _isCooling = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('🧊 Refrigerador'),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(16.w),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Temperatura Actual
              Card(
                child: Padding(
                  padding: EdgeInsets.all(20.w),
                  child: Column(
                    children: [
                      Text(
                        'Temperatura Actual',
                        style: Theme.of(context).textTheme.titleMedium,
                      ),
                      SizedBox(height: 16.h),
                      Stack(
                        alignment: Alignment.center,
                        children: [
                          SizedBox(
                            width: 150.w,
                            height: 150.w,
                            child: CircularProgressIndicator(
                              value: _currentTemp / _maxTemp,
                              strokeWidth: 8,
                              backgroundColor: AppTheme.borderColor,
                              valueColor: AlwaysStoppedAnimation(
                                _currentTemp > 70
                                    ? AppTheme.errorColor
                                    : _currentTemp > 50
                                        ? AppTheme.warningColor
                                        : AppTheme.successColor,
                              ),
                            ),
                          ),
                          Column(
                            children: [
                              Text(
                                '${_currentTemp.toStringAsFixed(1)}°C',
                                style: TextStyle(
                                  fontSize: 36.sp,
                                  fontWeight: FontWeight.bold,
                                  color: AppTheme.accentColor,
                                ),
                              ),
                              Text(
                                _currentTemp > 70
                                    ? 'Muy caliente'
                                    : _currentTemp > 50
                                        ? 'Normal'
                                        : 'Frío',
                                style: TextStyle(
                                  color: AppTheme.textSecondary,
                                  fontSize: 12.sp,
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
              SizedBox(height: 20.h),
              // Botón Enfriar
              SizedBox(
                width: double.infinity,
                child: ElevatedButton.icon(
                  onPressed: () {
                    setState(() => _isCooling = !_isCooling);
                  },
                  icon: Icon(_isCooling ? Icons.stop : Icons.ac_unit),
                  label: Text(_isCooling ? 'Detener' : 'Enfriar Ahora'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: _isCooling
                        ? AppTheme.errorColor
                        : AppTheme.accentColor,
                    padding: EdgeInsets.symmetric(vertical: 12.h),
                  ),
                ),
              ),
              SizedBox(height: 20.h),
              // Información
              Card(
                child: Padding(
                  padding: EdgeInsets.all(16.w),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Información',
                        style: Theme.of(context).textTheme.titleMedium,
                      ),
                      SizedBox(height: 12.h),
                      _InfoRow(
                        label: 'Max Temperatura',
                        value: '${_maxTemp.toStringAsFixed(0)}°C',
                      ),
                      _InfoRow(
                        label: 'Min Temperatura',
                        value: '28°C',
                      ),
                      _InfoRow(
                        label: 'Estado',
                        value: _isCooling ? 'Enfriando' : 'Normal',
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _InfoRow extends StatelessWidget {
  final String label;
  final String value;

  const _InfoRow({
    required this.label,
    required this.value,
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
            style: const TextStyle(
              color: AppTheme.accentColor,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}
