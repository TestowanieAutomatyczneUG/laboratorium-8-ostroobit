import requests
import json

class Meals:
    def __init__(self):
        pass
    
    def search_by_name(self, name):
        if type(name) != str:
            raise Exception("Invalid name type")
        result = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}").json()
        if result["meals"]:
            result = result["meals"][0]
            meal = {
                "name": result["strMeal"] if result["strMeal"] else "",
                "category": result["strCategory"] if result["strMeal"] else "",
                "instructions": result["strMeal"] if result["strMeal"] else "",
                "tags": result["strTags"] if result["strTags"] else ""
            }
            return meal
        return False
    def search_by_id(self, id):
        if type(id) != int:
            raise Exception("Invalid id type")
        result = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={str(id)}").json()
        if result["meals"]:
            result = result["meals"][0]
            meal = {
                "name": result["strMeal"] if result["strMeal"] else "",
                "category": result["strCategory"] if result["strMeal"] else "",
                "instructions": result["strMeal"] if result["strMeal"] else "",
                "tags": result["strTags"] if result["strTags"] else ""
            }
            return meal
        return False

    def filter_by_category(self, category):
        if type(category) != str:
            raise Exception("Invalid category type")
        result = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}").json()
        meals = []
        if result["meals"]:
            for meal in result["meals"]:
                meals.append(meal["strMeal"] if meal["strMeal"] else "")
            return meals
        return False

    def filter_by_area(self, area):
        if type(area) != str:
            raise Exception("Invalid category type")
        result = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area}").json()
        meals = []
        if result["meals"]:
            for meal in result["meals"]:
                meals.append(meal["strMeal"] if meal["strMeal"] else "")
            return meals
        return False   
