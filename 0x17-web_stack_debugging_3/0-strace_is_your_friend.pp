# Fix a typo in the configuration files
exec{'sed':
  path    => '/bin',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
