# Install Nginx web server with puppet
exec {'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
package { 'nginx':
  ensure   => installed,
  require  => Exec['update'],
}
# Add header
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "add_header X-Served-By ${hostname};",
  require => Package['nginx']
}
service {'restart':
  ensure => running,
  require => File_Line['add_header']
}
