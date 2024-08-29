
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:
    return """{
  "Room1": {
    "temperature": 22.5,
    "humidity": 45,
    "timestamp": "2024-08-07T10:00:00Z"
  },
  "Room2": {
    "temperature": 23.0,
    "humidity": 50,
    "timestamp": "2024-08-07T10:00:00Z"
  },
  "Room3": {
    "temperature": 21.5,
    "humidity": 55,
    "timestamp": "2024-08-07T10:00:00Z"
  }
}
"""
