#!/home/makan/Projects/web/repositories/wplogin/.venv/bin/python3

import argparse
import requests
from bs4 import BeautifulSoup
import json



def get_commandline():
    parser = argparse.ArgumentParser(description="conf file generator")
    parser.add_argument("--url", required=True, type=str, help="The url of the wordpress target")

    args = parser.parse_args()
    return args



def is_reachable(url):
    try:
        http_response = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        if http_response.ok:
            return http_response
        else:
            raise f"{url} - Is not reachable. status_code {http_response.status_code}"


def download_icon(icon_url):
    img_data = is_reachable(icon_url).content
    img = icon_url.split('/')[-1]
    # img_name, img_ext = img.split('.')

    with open(f'static/img/{img}', 'wb') as f:
        f.write(img_data)

    return img



def find_icon(soup):
    icon = soup.find('link', rel=lambda x: x and "icon" in x.lower())
    if icon and icon.get("href"):
        favicon_url = icon["href"]
        if not favicon_url.startswith("http"):
            favicon_url = url + favicon_url
        icon_name = download_icon(favicon_url)
        return icon_name



def website(url):
    http_response = is_reachable(url)
    soup = BeautifulSoup(http_response.text, 'html.parser')
    icon_name = find_icon(soup)
    title = soup.find('title')

    return {'title' : title.text, 'url': http_response.url, 'icon': icon_name, 'code': http_response.status_code}



def generate_conf_file():
    command = get_commandline()
    site = website(command.url)
    
    data = {
        'title' : site['title'],
        'url' : site['url'],
        'code' : site['code'],
        'icon' : site['icon'],
    }

    with open('conf.json', 'w', encoding='utf-8') as conf:
        json.dump(data, conf, indent=4)


if __name__=="__main__":
    generate_conf_file()