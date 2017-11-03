from render_to_json import render_to_json
from get_urls import create_urls

def check_page(page_name):
    urls = create_urls(page_name)
    page_url = urls.get('page_url')
    json_data = render_to_json(page_url)
    if not json_data:
        page_name = None
        return page_name
    else:
        return page_name

if __name__ == '__main__':
    page_name = check_page('esrigis')
    print(page_name)
