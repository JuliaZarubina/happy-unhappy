from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db/happy_unhappy.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    post_id = Column(Text)
    message = Column(Text)
    created_time = Column(DateTime)
    page_id = Column(Text)

    def __init__(self, post_id=None, message=None, created_time=None, page_id=None):
        self.post_id = post_id
        self.message = message
        self.created_time = created_time
        self.page_id = page_id

    def __repr__(self):
        return '<Post {} {} {} {}>'.format(self.post_id, self.message, self.created_time, self.page_id)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Text)
    comment_message = Column(Text)
    comment_created_time = Column(DateTime)
    comment_post_id = Column(Text, ForeignKey('posts.post_id'))

    def __init__(self, comment_id=None, comment_message=None, comment_created_time=None, comment_post_id=None):
        self.comment_id = comment_id 
        self.comment_message = comment_message
        self.comment_created_time = comment_created_time
        self.comment_post_id = comment_post_id

    def __repr__(self):
        return 'Comment {} {} {} {}>'.format(self.comment_id, self.comment_message, self.comment_created_time, self.comment_post_id)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
