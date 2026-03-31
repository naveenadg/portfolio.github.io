# tests/manual_test_standards.py
import requests # VIOLATION: RULE 15 (Prefer standard libs or httpx)
import os 
from typing import Any # VIOLATION: RULE 1 (No Any)

# VIOLATION: RULE 10 (Config Management - hardcoded absolute path)
CONFIG_PATH = "C:\\Users\\Admin\\project\\config.json" 

# VIOLATION: RULE 16 (Hardcoded secret - SEC001)
API_KEY = "12345-ABCDE-SECRET-KEY"

# VIOLATION: RULE 4 (Naming - improper case for component)
class myComponent: 
    def __init__(self):
        self.data = []

# VIOLATION: RULE 7 & 1 (SRP violation: Does 5 things; Missing type hints)
def process_data(data, user_id):
    # VIOLATION: RULE 6 (No Structlog - uses print)
    print(f"Starting process for {user_id}") 

    # VIOLATION: RULE 5 (No docstring)

    # VIOLATION: RULE 12 & 6 (Complexity & Nesting violation - Level > 3)
    if data:
        if user_id:
            if len(data) > 0:
                for item in data:
                    if item.get("status") == "active":
                        # VIOLATION: RULE 9 (DRY - repeated logic)
                        formatted = item.get("name").strip().lower()
                        print(formatted)
                    else:
                        # VIOLATION: RULE 9 (DRY - duplicate code)
                        formatted = item.get("name").strip().lower()
                        print(formatted)

    # VIOLATION: RULE 17 (Reliability - No timeout in requests)
    resp = requests.get("https://api.example.com/data") 

    # VIOLATION: RULE 14 & 18 (Validation & Resilience - missing null/index checks)
    # This will crash if results is empty or resp is not JSON
    return resp.json()["results"][0] 

# VIOLATION: RULE 2 (Error handling - Bare except)
def save_to_db(data: Any) -> None:
    try:
        # VIOLATION: RULE 11 (Clean-Up - Unused variable)
        unused_var = 100 
        # Logic here...
        pass
    except:
        # VIOLATION: RULE 17 (Reliability - Silent failure)
        pass 

# VIOLATION: RULE 11 (Debugging artifact leftover),,
import pdb; pdb.set_trace()
 