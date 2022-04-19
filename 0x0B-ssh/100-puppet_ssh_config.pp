# a file to use private key and no password

file { '/Users/andreshenderson/.ssh/config':
ensure => present,
}->
file_line { 'connect using key':
  path    => '/Users/andreshenderson/.ssh/config',
  line    => 'IdentityFile ~/.ssh/shchool',
  replace => true,
}->
file_line { 'do not request password':
  path    => '/Users/andreshenderson/.ssh/config',
  line    => 'PasswordAuthentication no',
  replace => true,
}
