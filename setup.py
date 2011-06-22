from setuptools import setup

setup(
    name="django-infinite-memcached",
    version="0.1-dev",
    author="Eric Davis",
    author_email="ed@npri.org",
    packages=["infinite_memcached"],
    url="http://github.com/edavis/django-infinite-memcached/",
    license="BSD",
    description="Tell memcached to never expire items in Django",
    long_description=open('README.rst').read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
)
