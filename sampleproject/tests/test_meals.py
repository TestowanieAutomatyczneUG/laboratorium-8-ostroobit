# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from sample.meals import Meals
# class TestSimple(unittest.TestCase):

#     def test_add_one(self):
#         self.assertEqual(add_one(5), 6)

#     def test_add_two(self):
#         self.assertEqual(add_one(4), 5)

class TestMeals(unittest.TestCase):
    def setUp(self):
        self.temp = Meals()
    
    def test_search_by_name_correct(self):
        self.assertEqual(self.temp.search_by_name("arrabiata"), {'name': 'Spicy Arrabiata Penne', 'category': 'Vegetarian', 'instructions': 'Spicy Arrabiata Penne', 'tags': 'Pasta,Curry'})
    
    def test_search_by_name_incorrect(self):
        self.assertEqual(self.temp.search_by_name("ahehehihi"), False)
    
    def test_search_by_name_not_string(self):
        with self.assertRaises(Exception):
            self.temp.search_by_name(1234)

    def test_search_by_id_correct(self):
        self.assertEqual(self.temp.search_by_id(52771), {'name': 'Spicy Arrabiata Penne', 'category': 'Vegetarian', 'instructions': 'Spicy Arrabiata Penne', 'tags': 'Pasta,Curry'})
    
    def test_search_by_id_incorrect(self):
        self.assertEqual(self.temp.search_by_id(1234), False)
    
    def test_search_by_id_not_int(self):
        with self.assertRaises(Exception):
            self.temp.search_by_id("huehuehue")

    def test_filter_by_category_correct(self):
        self.assertEqual(self.temp.filter_by_category("seafood"), ['Baked salmon with fennel & tomatoes', 'Cajun spiced fish tacos', 'Escovitch Fish', 'Fish pie', 'Fish Stew with Rouille', 'Garides Saganaki', 'Honey Teriyaki Salmon', 'Kedgeree', 'Kung Po Prawns', 'Laksa King Prawn Noodles', 'Mediterranean Pasta Salad', 'Recheado Masala Fish', 'Salmon Avocado Salad', 'Salmon Prawn Risotto', 'Saltfish and Ackee', 'Seafood fideuà', 'Shrimp Chow Fun', 'Sledz w Oleju (Polish Herrings)', 'Three Fish Pie', 'Tuna and Egg Briks', 'Tuna Nicoise'])
    
    def test_filter_by_category_incorrect(self):
        self.assertEqual(self.temp.filter_by_category("landfood"), False)
    
    def test_filter_by_category_not_string(self):
        with self.assertRaises(Exception):
            self.temp.filter_by_category([1, 2, 3, 4])

    def test_filter_by_area_correct(self):
        self.assertEqual(self.temp.filter_by_area("canadian"), ['BeaverTails', 'Breakfast Potatoes', 'Canadian Butter Tarts', 'Montreal Smoked Meat', 'Nanaimo Bars', 'Pate Chinois', 'Pouding chomeur', 'Poutine', 'Rappie Pie', 'Split Pea Soup', 'Sugar Pie', 'Timbits', 'Tourtiere'])
    
    def test_filter_by_area_incorrect(self):
        self.assertEqual(self.temp.filter_by_area("polandian"), False)
    
    def test_filter_by_area_not_string(self):
        with self.assertRaises(Exception):
            self.temp.filter_by_area({"hi": "hello"})

if __name__ == '__main__':
    unittest.main()
