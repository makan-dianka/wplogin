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



def website(url):
    try:
        res = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        if res.ok:
            soup = BeautifulSoup(res.text, 'html.parser')
            title = soup.find('title')
            return {'title' : title.text, 'url': res.url, 'code': res.status_code}
        else:
            return {'code': res.status_code}


def generate_conf_file():
    command = get_commandline()
    site = website(command.url)
    
    print(site)
    if site['code'] != 200:
        raise "Error"

    data = {
        'title' : site['title'],
        'url' : site['url'],
        'code' : site['code']
    }

    with open('conf.json', 'w', encoding='utf-8') as conf:
        json.dump(data, conf, indent=4)


if __name__=="__main__":
    generate_conf_file()