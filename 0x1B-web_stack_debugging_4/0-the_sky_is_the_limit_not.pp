# Allow multiple petitons at the sametiem in a nginx server
exec{'sed':
  path    => '/bin',
  command => 'sed -i s/15/2000/ /etc/default/nginx'
}
exec{'restart':
  path    => '/bin',
  command => 'service nginx restart'
}
