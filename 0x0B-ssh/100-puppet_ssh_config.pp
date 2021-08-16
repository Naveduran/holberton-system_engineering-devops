# using Puppet to make changes to our configuration file of a server

file_line { 'Authenticate with the holberton file':
  ensure    => present,
  line      => 'IdentityFile ~/.ssh/holberton',
  path      => '.ssh/config',
  replace   => false,
}

file_line { 'Refuse Password authentication':
  ensure    => present,
  line      => 'PasswordAuthentication no',
  path      => '.ssh/config',
  replace   => false,
}
