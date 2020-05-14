#!/usr/bin/env python3
import re
import requests
from instaloader import Instaloader, Post, Profile

L=Instaloader()

def userDetails(username):
    try:
        profile = Profile.from_username(L.context, username)
        return profile
    except Exception:
        return None

def get_media_details(link):
    link = link.split("?")[0]
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
