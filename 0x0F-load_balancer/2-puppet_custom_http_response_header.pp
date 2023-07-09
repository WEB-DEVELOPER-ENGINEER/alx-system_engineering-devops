# Automate the task of creating a custom HTTP header

class { 'nginx':
  ensure => running,
}

package { 'curl':
  ensure => 'present',
}

file { '/etc/nginx/custom_headers.conf':
  content => "add_header X-Served-By \"$hostname\";",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/etc/nginx/nginx.conf':
  ensure => 'file',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  content => template('my_module/nginx.conf.erb'),
  notify => Exec['nginx_reload'],
}

exec { 'nginx_reload':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe   => [
    File['/etc/nginx/custom_headers.conf'],
    File['/etc/nginx/nginx.conf'],
  ],
}
