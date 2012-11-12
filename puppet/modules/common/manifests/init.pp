# Small, useful packages that don't belong anywhere else.

class common {
  $packages = ['tmux', 'mg', 'htop', 'git-core']

  Package {
    ensure => installed
  }

  package {$packages: }

  file {"tmux.conf":
    ensure => file,
    path => "/etc/tmux.conf",
    source => "puppet:///modules/common/tmux.conf",
    group => "root",
    owner => "root",
    mode => 0644,
  }
}
