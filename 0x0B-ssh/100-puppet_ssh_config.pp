# Using Puppet to make changes to our configuration file of a server

file_line{'Use the private key in the file ~/.ssh/holberton':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line{'Refuse authentication using a password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
