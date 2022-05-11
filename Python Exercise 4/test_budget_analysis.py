import unittest
import numpy as np
from matplotlib import pyplot as plt
from budget_analysis import (education_budget,
                             security_budget_ratio,
                             largest_budget_year,
                             budget_difference)

class Tests(unittest.TestCase):
    def test_education_budget(self):
        self.assertEqual(education_budget(1997), 19320620000)
        self.assertEqual(education_budget(2000), 22488965000)
        self.assertEqual(education_budget(2005), 26162468000)
        self.assertEqual(education_budget(2010), 36265235000)
        with self.assertRaises(Exception):
            education_budget(1930)

        year_range = np.arange(1997, 2022)
        education_budgets = np.array([education_budget(x) for x in year_range])
        plt.bar(year_range, education_budgets)
        plt.title("Education budget per year")
        plt.xlabel('year')
        plt.ylabel('Budget (tens of billions)')
        plt.show()

    def test_security_budget_ratio(self):
        self.assertAlmostEqual(security_budget_ratio(1997), 0.2, delta=0.001)
        self.assertAlmostEqual(security_budget_ratio(2005), 0.206, delta=0.001)
        self.assertAlmostEqual(security_budget_ratio(2010), 0.192, delta=0.001)
        self.assertAlmostEqual(security_budget_ratio(2015), 0.171, delta=0.001)
        self.assertAlmostEqual(security_budget_ratio(2021), 0.106, delta=0.001)
        with self.assertRaises(Exception):
            security_budget_ratio(3000)

        year_range = np.arange(1997, 2022)
        security_ratios = np.array([round(security_budget_ratio(x), 4) for x in year_range])
        plt.plot(year_range, security_ratios)
        plt.title("Security budgets ratio per year")
        plt.xlabel('year')
        plt.show()

    def test_largest_budget_year(self):
        self.assertEqual(largest_budget_year('חינוך'), 2021)
        self.assertEqual(largest_budget_year('בטחון'), 2016)
        self.assertEqual(largest_budget_year('בריאות'), 2021)
        with self.assertRaises(Exception):
            largest_budget_year('אין משרד כזה')

    def test_budget_difference(self):
        self.assertAlmostEqual(budget_difference(1998), 0.134, delta=0.001)
        self.assertAlmostEqual(budget_difference(2005), 0.088, delta=0.001)
        self.assertAlmostEqual(budget_difference(2010, 'חינוך'), 0.104, delta=0.001)
        self.assertAlmostEqual(budget_difference(2021, 'בריאות'), 0.099, delta=0.001)
        with self.assertRaises(Exception):
            budget_difference(2100)
        with self.assertRaises(Exception):
            budget_difference(2000, 'אין משרד כזה')
        with self.assertRaises(Exception):
            budget_difference(1900, 'חינוך')


if __name__ == '__main__':
    unittest.main()
