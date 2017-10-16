from render_to_json import render_to_json
from datetime import datetime

def scrape_posts_by_date(post_url, target_date, page_id, post_data):
    page_posts = render_to_json(post_url)
    paging_leaf = page_posts.get('paging')
    next_page = paging_leaf.get('next')
    page_posts = page_posts.get('data')

    collecting = True

    for post in page_posts:
        post_id = post.get('id')
        message = post.get('message')
        post_time_str = post.get('created_time').split('+')[0]
        post_time = datetime.strptime(post_time_str, '%Y-%m-%dT%H:%M:%S')
        if not any([post_id, message, post_time_str]):
            continue
        current_post = {
            'id': post_id,
            'message': message,
            'created_time': post_time,
            'page_id': page_id
        }

        current_post_date = current_post['created_time']
     
        if target_date <= current_post_date:
            post_data.append(current_post)
        else:
            collecting = False
            break

    if collecting == True:
        scrape_posts_by_date(next_page,
            target_date,
            page_id,
            post_data
        )
    return post_data

if __name__ == '__main__':
    post_data = []
    date_str = '2017-10-10T23:59:59'
    target_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    page_id = '211211155280'
    scrape_posts_by_date('https://graph.facebook.com/esrigis/posts?/\
        key=value&access_token=APP_ID|APP_SECRET',
        target_date,
        page_id,
        post_data
    )
