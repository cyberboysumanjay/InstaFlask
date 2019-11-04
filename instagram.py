#!/usr/bin/env python3
import re
import requests
from instaloader import Instaloader, Post

L=Instaloader()

INSTA_UA = 'Instagram 10.34.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)'

def getID(username):
    url = "https://www.instagram.com/{}"
    r = requests.get(url.format(username))
    html = r.text
    if r.ok:
        return re.findall('"id":"(.*?)",', html)[0]
    else:
        return "invalid_username"

def userDetails(userID):
    url = "https://i.instagram.com/api/v1/users/{}/info/"
    session=requests.Session()
    session.headers={'user-agent': INSTA_UA}
    r = session.get(url.format(userID))
    if r.ok:
        data = r.json()
        return data
    else:
        return "NULL"

def get_media_details(link):
    shortcode = link.split('/p/')[1].replace('/', '')
    post=Post.from_shortcode(L.context,shortcode)
    owner_profile=post.owner_profile
    full_name=owner_profile.full_name
    followers=owner_profile.followers
    followees=owner_profile.followees
    is_verified=owner_profile.is_verified
    is_private=owner_profile.is_private
    bio=owner_profile.biography
    external_url=owner_profile.external_url
    owner_username=post.owner_username
    url=post.url
    caption=post.caption
    caption_hashtags=post.caption_hashtags
    if len(caption_hashtags)==0:
        caption_hashtags=None
    caption_mentions=post.caption_mentions
    if len(caption_mentions)==0:
        caption_mentions=None
    is_video=post.is_video
    video_url=post.video_url
    if(is_video):
        media_url=video_url
    else:
        media_url=url
    likes=post.likes
    comments=post.comments
    return(full_name,
           followers,
           followees,
           is_verified,
           is_private,
           bio,
           external_url,
           owner_username,
           url,
           caption,
           caption_hashtags,
           caption_mentions,
           is_video,
           media_url,
           likes,
           comments)
