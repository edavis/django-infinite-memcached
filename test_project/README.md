Here's how to get the test suite up and running:

(note: you'll need [Vagrant](http://vagrantup.com/) for this)

1) Set up your Vagrant box:

```shell
$ vagrant up --no-provision
$ echo 'sudo apt-get update' | vagrant ssh
$ vagrant provision
```

2) Create a virtualenv:

```shell
$ vagrant ssh
$ # now you're inside your Vagrant virtual machine
$ virtualenv django-infinite-memcached
$ . django-infinite-memcached/bin/activate
```

3) Install infinite_memcached and run the test suite:

```shell
$ cd /vagrant/test_project
$ pip install -r requirements.txt
$ ./manage.py test infinite_memcached
```

Assuming everything passes, you're all set.
