import json
import urllib.request
from urllib.error import URLError, HTTPError

def render_to_json(graph_url):
    try:
        web_response = urllib.request.urlopen(graph_url)
        readable_page = web_response.read()
        json_data = json.loads(readable_page.decode('utf-8'))
    
        return json_data

    except urllib.error.URLError as err:

        return None

if __name__ == '__main__':
    data = render_to_json('https://graph.facebook.com/esrigis?key=value&access_token=APP_ID|APP_SECRET')
    print(data)
