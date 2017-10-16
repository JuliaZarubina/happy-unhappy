import datetime
from render_to_json import render_to_json
from scrape_posts_by_date import scrape_posts_by_date
from get_posts_comments import get_posts_comments
from db import Posts, Comments, db_session
from get_data_from_config import get_credentials, get_list_of_pages
from get_urls import create_urls

def main():
    token = get_credentials()
    list_of_pages = get_list_of_pages()
    graph_url = 'https://graph.facebook.com/'
    target_date = datetime.datetime.now() - datetime.timedelta(days=3)
    target_date = target_date.replace(microsecond=0)

    for page in list_of_pages:
        urls = create_urls(page)
        current_page_url = urls.get('page_url')
        json_fbpage = render_to_json(current_page_url)
        page_id = json_fbpage.get('id')
        page_name = json_fbpage.get('name')
        page_data = {'id': page_id, 'name' : page_name}

        post_url = urls.get('post_url')
        scraped_posts_data = []
        scraped_posts_data = scrape_posts_by_date(
            post_url,
            target_date,
            page_id,
            scraped_posts_data            
        )
        for post in scraped_posts_data:
            post_id = post.get('id')
            post_db_row = Posts(
                    post['id'],
                    post['message'],
                    post['created_time'],
                    post['page_id']
            )
            db_session.add(post_db_row)
            db_session.commit() 
            urls = create_urls(page_name, post_id)
            comments_url = urls.get('comments_url')
            post_comments_data = []
            post_comments = get_posts_comments(
                comments_url,
                post_id,
                post_comments_data
            )
            if post_comments:
                for comment in post_comments:
                    comment_db_row = Comments(
                        comment['id'],
                        comment['message'],
                        comment['created_time'],
                        comment['post_id']
                    )
                    db_session.add(comment_db_row)
            else:
                continue
            
    db_session.commit()         

if __name__ == '__main__':
    main()  
