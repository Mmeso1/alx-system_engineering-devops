# Define SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => template('ssh/ssh_config.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
