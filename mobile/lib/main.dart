import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:game_turbo_pro_mobile/screens/home_screen.dart';
import 'package:game_turbo_pro_mobile/utils/theme.dart';

void main() {
  runApp(const GameTurboPro());
}

class GameTurboPro extends StatelessWidget {
  const GameTurboPro({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
      designSize: const Size(390, 844),
      minTextAdapt: true,
      splitScreenMode: true,
      builder: (context, child) {
        return MaterialApp(
          debugShowCheckedModeBanner: false,
          title: 'Game Turbo Pro',
          theme: AppTheme.darkTheme,
          home: child,
        );
      },
      child: const HomeScreen(),
    );
  }
}
