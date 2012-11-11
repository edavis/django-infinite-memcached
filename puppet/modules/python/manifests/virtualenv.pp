define python::virtualenv ($path = $title, $user) {
  exec {"python-virtualenv-$title":
    command => "/usr/bin/virtualenv --distribute $path",
    require => Package['python-virtualenv'],
    creates => $path,
    user => $user,
  }
}
