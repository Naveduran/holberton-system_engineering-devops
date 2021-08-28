# Install Nginx web server
exec {'update':
  command => 'sudo apt-get update',
  path    => '/usr/bin/',
}
package { 'nginx':
  ensure   => 'present',
  name     => 'nginx',
  provider => 'apt',
}
# Add header
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "\tadd_header X-Served-By ${HOSTNAME};",
}
# Nginx is running
exec {'restart':
  command => 'sudo service nginx start',
  path    => '/usr/bin/',
}
