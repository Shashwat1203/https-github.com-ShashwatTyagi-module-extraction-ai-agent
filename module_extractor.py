import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def get_text(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(" ", strip=True)
    return text


def extract_modules(url):
    data = []

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    for section in soup.find_all("h2"):
        module_name = section.text.strip()
        description = ""

        next_p = section.find_next("p")
        if next_p:
            description = next_p.text.strip()

        submodules = {}
        for sub in section.find_all_next("h3", limit=3):
            submodules[sub.text.strip()] = "Related feature of " + module_name

        data.append({
            "module": module_name,
            "Description": description,
            "Submodules": submodules
        })

    return data


if __name__ == "__main__":
    url = "https://help.zluri.com/"
    result = extract_modules(url)

import json

with open("output.json", "w") as f:
    json.dump(result, f, indent=4)

    for item in result[:3]:
        print(item)
