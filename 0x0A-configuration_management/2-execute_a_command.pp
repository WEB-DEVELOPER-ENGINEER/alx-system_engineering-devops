# kills a process named killmenow
exec { 'pkill killmenow':
    command => 'pkill -f killmenow',
}
