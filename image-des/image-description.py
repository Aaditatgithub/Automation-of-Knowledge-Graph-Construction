import requests
import json

# Replace with your Groq API key
GROQ_API_KEY = "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"
GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def get_image_description():
    payload = {
        "model": "llama-3.2-11b-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Make heads turn at every festive and wedding occasion with our Enchanting Pink Organza Saree. Perfect for engagements, receptions, or sangeets, this saree exudes grandeur with its luscious pink hue. The lightweight organza fabric creates a sublime shimmering aesthetic that will surely make you the star of the evening. Don this saree and let your elegance shine through.Colour:Pink Fabric:Organza Items Included:Saree Wash Care:Dry Clean Only Disclaimer Text:Product color may slightly vary due to photographic lighting sources or your monitor/screen settings. Manufacturer:Vedant Fashions Ltd, Paridhan Garment Park, 19, Canal South Road, SDF1, 4th Floor, A501-A502, Kolkata - 700015, West Bengal.Mohey brand. Describe the crucial aspects of the item."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://manyavar.scene7.com/is/image/manyavar/151222-1-389_13-05-2021-13-16-2:650x900"
                        }
                    }
                ]
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False,
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        return result.get("choices", [{}])[0].get("message", "No message returned.")
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    description = get_image_description()
    print(description)
