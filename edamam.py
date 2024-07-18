import requests

class Edamam():
    def __init__(self, app_key, app_id) -> None:
        self.app_key = app_key
        self.app_id = app_id

    def get_nutritional_facts(self, ingredients):  
        print(ingredients)
        result = requests.get(
            f"https://api.edamam.com/api/nutrition-data?app_id={self.app_id}&app_key={self.app_key}&nutrition-type=cooking&ingr={ingredients}"
        )
    
        data = result.json()
        return data
        