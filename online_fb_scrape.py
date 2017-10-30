import datetime
from render_to_json import render_to_json
from scrape_posts_by_date import scrape_posts_by_date
from get_posts_comments import get_posts_comments
from db import Posts, Comments, db_session
from get_data_from_config import get_credentials, get_list_of_pages
from get_urls import create_urls
from classify import classify

def online_scrape(page):
    token = get_credentials()
    graph_url = 'https://graph.facebook.com/'
    target_date = datetime.datetime.now() - datetime.timedelta(days=1)
    target_date = target_date.replace(microsecond=0)

    urls = create_urls(page)
    page_url = urls.get('page_url')
    json_fbpage = render_to_json(page_url)
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

    pos_list = []
    neg_list = []
    total_list = []
    for post in scraped_posts_data:
        post_id = post.get('id')
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
                y, proba, clf = classify(comment['message'])
                # print(y)
                # print(proba)
                total_list.append(comment)
                if y == 'positive':
                    pos_list.append(comment)
                else:
                    neg_list.append(comment)

            total = len(total_list)
            pos = len(pos_list)
            neg = len(neg_list)

        else:
            continue

    return total, pos, neg       

if __name__ == '__main__':
    total, pos, neg = online_scrape('techcrunch')
    print(total, pos, neg) 
