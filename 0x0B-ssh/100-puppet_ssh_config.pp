# using Puppet to make changes to our configuration file of a server

$str = "# Config file
Host 34.138.249.185
     HostName 34.138.249.185
     User ubuntu
     IdentityFile ~/.ssh/holberton
"

file { '.ssh/config':
  ensure  => 'present',
}

file_line { 'Append some lines to the config file':
  ensure => present,
  path   => '.ssh/config',
  line   => $str,
}
