import unittest

import six

from example_tests import example_test


class TestBlackScholes(unittest.TestCase):

    def test_black_scholes(self):
        output = example_test.run_example(
            'finance/black_scholes.py', '--n-options', '10')
        six.assertRegex(
            self, output.decode('utf-8'),
            r'initializing...\n' +
            r'start computation\n' +
            r' CPU \(NumPy, Naive implementation\):\t[0-9\.]+ sec\n' +
            r' GPU \(CuPy, Naive implementation\):\t[0-9\.]+ sec\n' +
            r' GPU \(CuPy, Elementwise kernel\):\t[0-9\.]+ sec')


class TestMonteCarlo(unittest.TestCase):

    def test_monte_carlo(self):
        output = example_test.run_example(
            'finance/monte_carlo.py', '--n-options', '10',
            '--n-samples-per-thread', '10',
            '--n-threads-per-option', '10')
        six.assertRegex(
            self, output.decode('utf-8'),
            r'initializing...\n' +
            r'start computation\n' +
            r'    # of options: 10\n' +
            r'    # of samples per option: 100\n' +
            r'GPU \(CuPy, Monte Carlo method\):\t[0-9\.]+ sec\n' +
            r'Error: [0-9\.]+')


class TestMonteCarloWithMultiGPU(unittest.TestCase):

    def test_monte_carlo_multigpu(self):
        output = example_test.run_example(
            'finance/monte_carlo_multigpu.py', '--gpus', '0', '1',
            '--n-options', '10',
            '--n-samples-per-thread', '10',
            '--n-threads-per-option', '10')
        six.assertRegex(
            self, output.decode('utf-8'),
            r'initializing...\n' +
            r'start computation\n' +
            r'    # of gpus: 2\n' +
            r'    # of options: 10\n' +
            r'    # of samples per option: 200\n' +
            r'GPU \(CuPy, Monte Carlo method\):\t[0-9\.]+ sec\n' +
            r'Error: [0-9\.]+')
