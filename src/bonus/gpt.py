import requests
from private_token import OPENAI_API_KEY

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

def get_destinaiton(prompt: str) -> str:
    """
    
    """
    content = {
        "model": "gpt-3.5-turbo",
        "messages":
        [
            {
                "role": "system",
                "content": """
                follow these examples: 
                Q: If left front bin is red, left back bin is gray, right front bin is green, right back bin is blue, put all fruits from the table into the red bin.
                A: left front
                Q: If left front bin is black, left back bin is gray, right front bin is purple, right back bin is yellow, select the ball from the scene and drop it to the right back.
                A: right back
                Q: If left front bin is gray, left back bin is green, right front bin is blue, right back bin is red, select food from the desk to the green.
                A: left back
                Q: If left front bin is gray, left back bin is green, right front bin is blue, right back bin is red, select the black object to the red bin.
                A: right back
                while output, ignore "A:".
                If none is correct, say "default".
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    print(content["messages"][0]["content"])
    proxies = {
        "http": "http://127.0.0.1:2345",
        "https": "http://127.0.0.1:2345"
    }
    resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=content, proxies=proxies)

    result = resp.json()
    
    ret = result["choices"][0]["message"]["content"]
    
    return ret

if __name__ == "__main__":
    query = "If left front bin is gray, left back bin is green, right front bin is blue, right back bin is red, select the green object from the scene to the red bin"
    print(get_destinaiton(query))