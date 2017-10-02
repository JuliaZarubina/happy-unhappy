import datetime
from render_to_json import render_to_json
from scrape_posts_by_date import scrape_posts_by_date
from get_posts_comments import get_posts_comments
from db import Posts, Comments, db_session

APP_ID = 'APP_ID'
APP_SECRET = 'APP_SECRET'

def create_page_url(graph_url, company, APP_ID, APP_SECRET):
    page_args = '/?key=value&access_token='+ APP_ID + '|' + APP_SECRET
    page_url = graph_url + company + page_args
    
    return page_url

def create_post_url(graph_url, APP_ID, APP_SECRET):
    post_args = '/posts/?key=value&access_token=' + APP_ID + '|' + APP_SECRET
    post_url = graph_url + post_args
    
    return post_url

def create_comments_url(graph_url, post_id, APP_ID, APP_SECRET):
    comments_args = post_id + '/comments/?key=value&access_token=' + APP_ID + '|' + APP_SECRET
    comments_url = graph_url + comments_args

    return comments_url

def main():
    list_of_pages = ['Villagemsk']
    graph_url = 'https://graph.facebook.com/'
    target_date = datetime.datetime.now() - datetime.timedelta(days=1)
    target_date = target_date.replace(microsecond=0)

    for page in list_of_pages:
        current_page_url = create_page_url(graph_url, page, APP_ID, APP_SECRET)
        current_page = graph_url + page
        json_fbpage = render_to_json(current_page_url)
        page_id = json_fbpage.get('id')
        page_name = json_fbpage.get('name')
        page_data = {'id': page_id, 'name' : page_name}
        post_url = create_post_url(current_page, APP_ID, APP_SECRET)
        scraped_posts_data = []
        scraped_posts_data = scrape_posts_by_date(post_url, target_date, scraped_posts_data, page_id)

        for post in scraped_posts_data:
            post_id = post['id']
            post_db_row = Posts(post['id'], post['message'],
                        post['created_time'], post['page_id'])
            db_session.add(post_db_row)
            comments_url = create_comments_url(graph_url, post_id, APP_ID, APP_SECRET)
            post_comments_data = []
            post_comments = get_posts_comments(comments_url, post_comments_data, post_id)
            if not post_comments:
                print('No comments')
            else:
                for comment in post_comments:
                    comment_db_row = Comments(comment['id'], comment['message'],
                                            comment['created_time'], comment['post_id'])

                    db_session.add(comment_db_row)

    db_session.commit()         

if __name__ == '__main__':
    main()