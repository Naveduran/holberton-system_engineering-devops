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
# Create error and redirect pages
file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.google.com;\n\t}\n",
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
