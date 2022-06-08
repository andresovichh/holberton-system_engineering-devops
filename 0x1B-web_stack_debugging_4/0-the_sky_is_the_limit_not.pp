# increase limit of nginx files open
# ulimit -n 65536
exec { 'increase fd limit':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx && sudo service nginx restart',
  provider => 'shell',
}
