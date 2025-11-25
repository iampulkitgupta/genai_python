class ChaiUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water, milk, sugar, tea leaves"
obj = ChaiUtils()
print(ChaiUtils.clean_ingredients(raw)) 
print(obj.clean_ingredients(raw))