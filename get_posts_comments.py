from render_to_json import render_to_json
from datetime import datetime

def get_posts_comments(comments_url, post_id, post_comments_data):
    comments = render_to_json(comments_url)
    post_comments = comments['data']

    for comment in post_comments:
        comment_id = comment.get('id')
        comment_from = comment.get('from')
        comment_from_name = comment_from.get('name')
        comment_from_id = comment_from.get('id')    
        comment_created_time_str = comment.get('created_time').split('+')[0]
        comment_created_time = datetime.strptime(
            comment_created_time_str,'%Y-%m-%dT%H:%M:%S'
        )
        comment_message = comment.get('message')
        if not any([
                comment_id,
                comment_from,
                comment_created_time,
                comment_message
            ]):
            continue
        current_comment = {
            'id': comment_id,
            'comment_from_name': comment_from_name,
            'comment_from_id': comment_from_id, 
            'created_time': comment_created_time,
            'message':  comment_message,
            'post_id': post_id
        }

        post_comments_data.append(current_comment)

    paging_leaf = comments.get('paging')
    if paging_leaf and paging_leaf.get('next'):
        next_comment_page = paging_leaf.get('next')

        get_posts_comments(
            next_comment_page,
            post_id,
            post_comments_data
        )
    else:
        return post_comments_data

if __name__ == '__main__':
    post_comments_data = []
    post_id = '86680728811_10156375147413812'
    get_posts_comments('https://graph.facebook.com/86680728811_10156375147413812/comments/?key=value&access_token=519406221742449|35549d825f175df2a1c61c753c8def0b',
        post_id, post_comments_data)
