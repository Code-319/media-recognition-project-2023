import requests
from private_token import REPLICATE_API_TOKEN
import time

headers = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
}



def get_destinaiton(prompt: str) -> str:
    """
    
    """
    content = {
        "version": "44878be272d384b00155fe821d8534275d5471b88c25dc6e78c97ce3644b1e99",
        "input": {
        "debug": False,
        "top_p": 1,
        "prompt": f"Q: {prompt}",
        "temperature": 0.5,
        "system_prompt": 'follow these examples: \nQ: left front is red, left back is gray, right front is green, right back is blue. put all fruits into the red bin. \nA: left front \nQ: left front is black, left back is gray, right front is purple, right back is yellow. select the ball from the scene and drop it to the right back\nA: right back\nwhile output, ignore "A:".',
        "max_new_tokens": 500,
        "min_new_tokens": -1,
        },
    }

    resp = requests.post("https://api.replicate.com/v1/predictions", headers=headers, json=content)

    res = resp.json()

    get_url = res["urls"]["get"]
    time.sleep(3)
    pred = requests.get(get_url, headers=headers)
    result = pred.json()
    # print(result)
    # print(result["output"])
    try:
        return " ".join(result["output"])
    except KeyError:
        print("This may take 10 seconds...")
        time.sleep(12)
        pred = requests.get(get_url, headers=headers)
        result = pred.json()
        return " ".join(result["output"])


if __name__=="__main__":
    query = "left front is gray, left back is green, right front is blue, right back is red. select food from the desk to the red bin"
    print(get_destinaiton(query))