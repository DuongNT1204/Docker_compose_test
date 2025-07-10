import requests

response = requests.post("http://localhost:7860/generate", json={
    "prompt": "A steampunk city in the clouds"
})

if response.ok:
    with open("generated.png", "wb") as f:
        f.write(response.content)
    print("Image saved as generated.png")
else:
    print("Error:", response.status_code, response.text)
