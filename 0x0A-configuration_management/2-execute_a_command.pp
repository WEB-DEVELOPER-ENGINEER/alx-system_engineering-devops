# kills a process named killemenow
exec { 'pkill killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}
