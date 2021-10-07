# Allow multiple petitons at the sametiem in a nginx server
exec{'sed':
  path    => '/bin',
  command => "sed -i '5s/.*/ULIMIT=\"-n 2000\"/' /etc/default/nginx"
}

exec{'sed':
  path    => '/bin',
  command => 'service nginx restart'
}
