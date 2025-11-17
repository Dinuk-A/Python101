import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# fn to send user data (POST request)
def sendUserData():
    
    # define the payload data
    user_data = {
        "name": "Alice Johnson",
        "age": 28
    }
      
    #  make the POST req
    response = requests.post(
        f"{BASE_URL}/person/add",
        json = user_data,
        headers = {"Content-Type": "application/json"}
    )
    
    if response.status_code == 200:
        print("User added successfully!")
    else :
        print(f"Failed to add user. Status code: {response.status_code}")
   
# fn to get all users (GET request) 
def get_all_users():
    """Retrieve all users (GET request)"""
    response = requests.get(f"{BASE_URL}/person/all")
    print(f"\n📋 All users:\n{json.dumps(response.json(), indent=2)}")
    
# to run the functions
if __name__ == "__main__":
    print("Sending POST request...\n")
    sendUserData()
    
    print("\nRetrieving all users...\n")
    get_all_users()
        
# to run this file > >> python lessons\l4_post_manual_client.py
    
    