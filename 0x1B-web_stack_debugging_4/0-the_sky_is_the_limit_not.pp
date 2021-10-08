# Allow multiple request at the same time in a nginx server
exec{'limit':
  path    => '/usr/bin:/bin',
  command => 'sed -i s/15/2000/ /etc/default/nginx; service nginx restart'
}
