# Automate the task of creating a custom HTTP header

class { 'nginx':
  ensure => running,
}

nginx::config::server { 'custom_header':
  content => "add_header X-Served-By $hostname;",
}
