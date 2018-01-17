#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site information
AUTHOR = 'CheapThyCable'
SITENAME = 'CheapThyCable'
DOMAIN = 'localhost:8000'
SITEURL = 'http://' + DOMAIN
SITE_DESCRIPTION = 'A community to help negotiate lower cable bills'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {
	'extra/robots.txt': {'path': 'robots.txt'},
	'extra/favicon.png': {'path': 'favicon.png'},
	'extra/favicon.ico': {'path': 'favicon.ico'}
}

APP_PATH = '/app'

APPURL = SITEURL + APP_PATH

# Localization issues
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%b %d, %Y'

# Theme
THEME = 'themes/w3css-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social
TWITTER_USERNAME = 'CheapThyCable'
FACEBOOK = 'CheapThyCable'
INSTAGRAM = 'cheapthycable'

SOCIAL = {'Twitter': 'https://www.twitter.com/' + TWITTER_USERNAME,
          'LinkedIn': '',
          'Facebook': 'https://www.facebook.com/' + FACEBOOK,
          'Instagram': 'https://www.instagram.com/' + INSTAGRAM,
          'Snapchat': '',
          'Pinterest': ''}

DEFAULT_PAGINATION = False

# Category Settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'blog'

# Output
OUTPUT_SOURCES = False

# URL configuration
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

DISQUS_SITENAME = 'local-cheapthycable'
GOOGLE_ANALYTICS = ''

PLUGIN_PATHS = ["plugins", "../../../../../tools/Python36/Lib/site-packages"]
PLUGINS = ["summary", "pelican_gist"]

OUTPUT_PATH = 'output/local'