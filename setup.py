from setuptools import setup

setup(
    name="django-infinite-memcached",
    version="0.1",
    author="Eric Davis",
    author_email="ed@npri.org",
    packages=["infinite_memcached"],
    url="http://github.com/edavis/django-infinite-memcached/",
    license="BSD",
    description="A Django memcached backend to handle 'infinite' timeouts",
    long_description=open('README.rst').read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
)
