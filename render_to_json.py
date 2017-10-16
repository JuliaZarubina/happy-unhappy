import json
import urllib.request

def render_to_json(graph_url):
    web_response = urllib.request.urlopen(graph_url)
    readable_page = web_response.read()
    json_data = json.loads(readable_page.decode('utf-8'))

    return json_data

if __name__ == '__main__':
    data = render_to_json('https://graph.facebook.com/esrigis?key=value&access_token=APP_ID|APP_SECRET')
    print(data)

