try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Seminarbot',
    'author': 'Hajime Fukuda',
    'url': 'http://member.ipmu.jp/hajime.fukuda/',
    'author_email': 'hajime.fukuda@ipmu.jp',
    'version': '0.1',
    'install_requires': ['slackbot', 'pit', 'pyquery'],
    'packages': ['seminarbot'],
    'name': 'seminarbot',
}

setup(**config)
