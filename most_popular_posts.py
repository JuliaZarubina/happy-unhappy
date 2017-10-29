from collections import defaultdict
from collections import Counter
from db import Comments, Posts, db_session

def most_popular_posts():
    comments = Comments.query.all()
    pos_count = defaultdict(lambda: 0)
    neg_count = defaultdict(lambda: 0)
    for comment_db_row in comments:
        if comment_db_row.comment_sentiment == 'positive':
            pos_count[comment_db_row.post.post_id, comment_db_row.post.message]+=1
        else:
            neg_count[comment_db_row.post.post_id, comment_db_row.post.message]+=1
    
    top_pos_5 = Counter(pos_count).most_common(5)
    top_neg_5 = Counter(neg_count).most_common(5)

    return top_pos_5, top_neg_5

if __name__ == '__main__':
    pos_count, neg_count = most_popular_posts()
