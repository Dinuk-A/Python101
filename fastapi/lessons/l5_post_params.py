import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_path_param():
    """POST with path parameter"""
    print("=== POST with PATH parameter ===\n")
    
    order_data = {"id": 1, "item": "cat"}
    
    response = requests.post(
        f"{BASE_URL}/l5/users/1/orders",
        json=order_data
    )
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# fn to get all users (GET request) 
def get_all_users():
    """Retrieve all users (GET request)"""
    response = requests.get(f"{BASE_URL}/l5/userorders/all")
    print(f"\n📋 All users:\n{json.dumps(response.json(), indent=2)}")
    
if __name__ == "__main__":
    test_path_param()
    get_all_users()
    
#to run this > >> python lessons\l5_post_params.py
# also uvicorn has to be activated (uvicorn main:app --reload)
    