# Configure an Nginx server

package { 'Install Nginx web server':
  ensure => 'installed',
  name   => 'nginx',
}

file_line { 'Create error and redirect pages':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => '\n\tlocation /redirect_me {\t\treturn 301 https://}
  \terror_page 404 /error404.html;\n',
}

file {'Create index.html file':
  ensure  => 'present',
  content => 'Holberton School',
  path    => '/var/www/html/index.html',
}

file {'Create error.html file':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
  path    => '/var/www/html/error404.html',
}

service { 'Initialize nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
