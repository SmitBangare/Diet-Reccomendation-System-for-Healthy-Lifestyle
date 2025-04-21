import json
from integrated_model import generate_recommendations

class Generator:
    def __init__(self,nutrition_input:list,ingredients:list=[],params:dict={'n_neighbors':5,'return_distance':False}):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def set_request(self,nutrition_input:list,ingredients:list,params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def generate(self,):
        # Use local model instead of API call
        results = generate_recommendations(
            nutrition_input=self.nutrition_input,
            ingredients=self.ingredients,
            params=self.params
        )
        
        # Create a response-like object to maintain compatibility
        class MockResponse:
            def __init__(self, data):
                self.data = data
                self.status_code = 200
                
            def json(self):
                return {"output": self.data}
                
        return MockResponse(results)
