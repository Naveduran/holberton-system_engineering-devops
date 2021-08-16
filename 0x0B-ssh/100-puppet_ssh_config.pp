# using Puppet to make changes to our configuration file of a server

$str = "# Config file
Host ubuntu@34.138.249.185
     HostName 34.138.249.185
     User ubuntu
     IdentityFile ~/.ssh/holberton
"

file { '.ssh/config':
  ensure  => 'present',
}->
file-line {'Append some lines to the config file'
  path => '.ssh/config',
  line => $str,
}
