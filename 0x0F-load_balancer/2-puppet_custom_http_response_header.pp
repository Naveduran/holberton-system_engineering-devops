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
# Create redirect page
file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.google.com;\n\t}\n",
}
# Add header
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "\n\t\tadd_header X-Served-By $HOSTNAME;\n",
}

# Create html fake file
file {'index.html':
  ensure  => 'present',
  content => 'Holberton School',
  path    => '/var/www/html/index.html',
}
# Nginx is running
exec {'restart':
  command => 'sudo service nginx start',
  path    => '/usr/bin/',
}
