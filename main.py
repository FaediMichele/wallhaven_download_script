import requests
import json
import os
import time

CONFIG_FILE = os.path.join(os.path.expanduser(
    "~"), "Documents", "wallhaven_config.json")


def get_images_url(data):
    parameters = {
        "q": data["tag"],
        "categories": data["categories"],
        "purity": data["purity"],
        "sorting": "random",
        "atleast": "1920x1080",
        "ratios": "16x9",
    }

    url = "https://wallhaven.cc/api/v1/search"
    # Your API must be in a file called api.key in the same directory as this script
    if data["purity"][2] == "1":
        with open(data["api_key_path"]) as F:
            contents = F.read()
            url += "?apikey=" + contents

    response = requests.get(url, params=parameters)

    return [d["path"] for d in response.json()["data"]]


def download_image(url, dest):
    data = requests.get(url)
    with open(dest, "wb") as file:
        file.write(data.content)


def load_config_data(filename):
    if os.path.exists(filename):
        with open(filename, "rt") as file:
            return json.load(file)
    else:
        data = {
            "download_directory": os.path.join(os.path.expanduser("~"), "Pictures"),
            "api_key_path": "api.key",
            "image_count": 10,
            "tag": "landscape",
            "categories": "111",
            "purity": "110",
            "time_for_download": 5*9*60  # Seconds
        }
        with open(filename, "wt") as file:
            json.dump(data, file, indent=4)
        return data


while True:
    data = load_config_data(CONFIG_FILE)
    if data["purity"][2] == "1" and not os.path.exists(data["api_key_path"]):
        data["purity"][2] = "0"
    urls = get_images_url(data)[:data["image_count"]]
    for i in range(len(urls)):
        print(urls[i])
        file = str(i) + "." + urls[i].split(".")[-1]
        download_image(urls[i], os.path.join(data["download_directory"], file))

    time.sleep(data["time_for_download"])
