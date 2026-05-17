#!/usr/bin/python3
"""
This module provides functions to fetch posts from an API
and process them by printing titles or saving to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the status code
    and titles of all posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves id, title,
    and body into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()

        # Məlumatı lüğət siyahısı (list of dictionaries) formatına salırıq
        data_to_save = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        # CSV faylına yazma prosesi
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data_to_save)
