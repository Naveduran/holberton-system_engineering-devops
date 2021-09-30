# Fix a typo in the configuration files include stdlib
exec{'sed':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
