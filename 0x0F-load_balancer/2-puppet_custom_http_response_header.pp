# Automate the task of creating a custom HTTP header

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
class { 'nginx':
  ensure => running,
}

file { '/etc/nginx/custom_headers.conf':
  content => "add_header X-Served-By \"$hostname\";",
  mode    => '0644',
}

-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
