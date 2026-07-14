#!/usr/bin/env python3
"""
Tests unitarios para Game Turbo Pro
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.game_turbo import GameTurbo
from src.game_booster import GameBooster
from src.monitor import SystemMonitor

class TestGameTurbo(unittest.TestCase):
    """Tests para Game Turbo"""
    
    def setUp(self):
        self.turbo = GameTurbo()
    
    def test_initial_state(self):
        self.assertFalse(self.turbo.active)
        self.assertEqual(len(self.turbo.optimizations), 0)
    
    def test_activate_turbo(self):
        result = self.turbo.activate_turbo('TestGame')
        self.assertTrue(result)
        self.assertTrue(self.turbo.active)

class TestGameBooster(unittest.TestCase):
    """Tests para Game Booster"""
    
    def setUp(self):
        self.booster = GameBooster()
    
    def test_initial_state(self):
        self.assertFalse(self.booster.active)
        self.assertEqual(self.booster.boost_level, 0)
    
    def test_activate_boost(self):
        result = self.booster.activate_boost(80)
        self.assertTrue(result)
        self.assertTrue(self.booster.active)

class TestSystemMonitor(unittest.TestCase):
    """Tests para System Monitor"""
    
    def setUp(self):
        self.monitor = SystemMonitor()
    
    def test_get_system_stats(self):
        stats = self.monitor.get_system_stats()
        self.assertIn('cpu', stats)
        self.assertIn('memory', stats)

if __name__ == '__main__':
    unittest.main()
