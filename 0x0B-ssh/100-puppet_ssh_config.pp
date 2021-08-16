# u sing Puppet to make changes to our configuration file of a server

$s = "     IdentityFile ~/.ssh/holberton\n     PasswordAuthentication no\n"

file_line { 'Add two lines to the ssh config file':
  ensure    => present,
  line      => $s,
  path      => '.ssh/config',
  replace   => false,
}
