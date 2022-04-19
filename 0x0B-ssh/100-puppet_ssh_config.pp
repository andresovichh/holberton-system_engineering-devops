#!/usr/bin/env bash
# a file to use private key and no password

file_line { 'connect using key':
  path    => '/etc/ssh/.ssh/config',
  line    => 'IdentityFile ~/.ssh/shchool',
  replace => true,
}->
file_line { 'do not request password':
  path    => '/etc/ssh/.ssh/config',
  line    => 'PasswordAuthentication no',
  replace => true,
}
