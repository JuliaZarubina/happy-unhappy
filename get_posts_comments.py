from render_to_json import render_to_json
from datetime import datetime

post_id = '86680728811_10156375147413812'
post_comments_data = []

def get_posts_comments(comments_url, post_comments_data, post_id):
    
    comments = render_to_json(comments_url)
    post_comments = comments['data']

    for comment in post_comments:
        comment_id = comment.get('id')
        comment_from = comment.get('from')
        comment_from_name = comment_from.get('name')
        comment_from_id = comment_from.get('id')    
        comment_created_time_str = comment.get('created_time').split('+')[0]
        comment_created_time = datetime.strptime(comment_created_time_str,'%Y-%m-%dT%H:%M:%S')
        comment_message = comment.get('message')
        if not any([comment_id, comment_from, comment_created_time, comment_message]):
            continue
        current_comment = {'id': comment_id,'comment_from_name': comment_from_name,
                            'comment_from_id': comment_from_id, 
                            'created_time': comment_created_time,
                            'message':  comment_message, 'post_id': post_id}

        post_comments_data.append(current_comment)
    
    try:
        next_comment_page = comments['paging']['next']
    except Exception:
        next_comment_page = None

    if next_comment_page:
        get_posts_comments(next_comment_page, post_comments_data, post_id)
    else:
        return post_comments_data

if __name__ == '__main__':
    get_posts_comments('https://graph.facebook.com/86680728811_10156375147413812/comments/?key=value&access_token=APP_ID|APP_SECRET',
        post_comments_data, post_id)
