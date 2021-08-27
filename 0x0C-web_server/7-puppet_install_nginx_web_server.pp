# Install Nginx web server
package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}
# Create error and redirect pages
file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => '\n\tlocation /redirect_me {\n\t\treturn 301 https://www.google.com\n\t}\n\terror_page 404 /error404.html;\n',
}
# Create html fake file
file {'index.html':
  ensure  => 'present',
  content => 'Holberton School',
  path    => '/var/www/html/index.html',
}
# Create error fake html file
file {'error404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
  path    => '/var/www/html/error404.html',
}
# Initialize nginx is running
service { 'Initialize nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
