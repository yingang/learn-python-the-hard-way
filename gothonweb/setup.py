try:
	from setuptools import setup
	
except ImportError:
	from distutils.core import setup
	
config = [
	'description': 'gothonweb',
	'author': 'Yin Gang',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'zenith.yin@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['gothonweb'],
	'scripts': [],
	'name': 'gothonweb'
]

setup(**config)
