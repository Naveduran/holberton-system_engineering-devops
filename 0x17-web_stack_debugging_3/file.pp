# Fix a typo in the configuration file s
exec{'sed':
  path    => '/bin',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
