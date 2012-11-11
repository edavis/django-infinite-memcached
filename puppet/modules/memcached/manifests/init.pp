class memcached {
  File {
    owner => "root",
    group => "root",
  }

  package {"memcached":
    ensure => installed,
  }

  file {"/etc/memcached.conf":
    ensure => file,
    source => "puppet:///modules/memcached/etc/memcached.conf",
  }

  file {"/etc/default/memcached":
    ensure => file,
    source => "puppet:///modules/memcached/etc/default/memcached",
  }

  service {"memcached":
    ensure => running,
    require => [Package["memcached"], File["/etc/default/memcached"]],
    enable => true,
  }
}
