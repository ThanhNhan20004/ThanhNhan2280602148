import base64

def main():
    try: 
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()
        
        