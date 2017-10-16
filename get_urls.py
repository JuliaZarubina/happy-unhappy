from get_data_from_config import get_credentials 

def create_urls(page_name, post_id='post_id'):
    token = get_credentials()
    graph_url = 'https://graph.facebook.com/'
    page_args = '/?key=value&access_token={}'.format(token) 
    post_args = '/posts/?key=value&access_token={}'.format(token) 
    comments_args = post_id + '/comments/?key=value&access_token={}'.format(token)
    page_url = graph_url + page_name + page_args
    post_url = graph_url + page_name + post_args
    comments_url = graph_url + comments_args
    
    urls = {
        'page_url': page_url,
        'post_url': post_url,
        'comments_url': comments_url
    }

    return urls

if __name__ == '__main__':
    create_urls('name')
