import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    likes = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Comments_Post(Base):
    __tablename__ = 'comments_post'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    content = Column(String(250))
    likes = Column(Integer)
    replies = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Likes_Post(Base):
    __tablename__ = 'likes_post'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Replies_Comments(Base):
    __tablename__ = 'replies_comments'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    content = Column(String(250))
    likes = Column(Integer)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    likes = Column(Integer)
    replies = Column(Integer)
    shares = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Comments_Story(Base):
    __tablename__ = 'comments_story'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    content = Column(String(250))
    likes = Column(Integer)
    replies = Column(Integer)
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship(Story)

class Likes_Story(Base):
    __tablename__ = 'likes_story'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship(Story)

class Replies_Story(Base):
    __tablename__ = 'replies_story'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship(Story)
    content = Column(String(250))
    likes = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
