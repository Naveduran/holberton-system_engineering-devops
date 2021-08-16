# using Puppet to make changes to our configuration file of a server

$str = "# Config file
Host *
     IdentityFile ~/.ssh/holberton
"

file { '.ssh/config':
  ensure  => 'present',
}->
file-line {'Append some lines to the config file'
  path => '.ssh/config',
  line => $str,
}
