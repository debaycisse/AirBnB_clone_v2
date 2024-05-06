# A Puppet manifest to set up web servers for the deployment of web_static

# Check if nginx is installed
$nginx_installed = $::osfamily ? {
  'Debian' => package { 'nginx':
    ensure => installed,
  },
  default => undef,
}

# Install nginx if not already installed
if $nginx_installed == undef {
  package { 'nginx':
    ensure => installed,
    require => Package['update'],
  }
}

# Create directories
file { '/data/web_static/releases/test':
  ensure => directory,
  mode   => '0755',
}

file { '/data/web_static/shared':
  ensure => directory,
  mode   => '0755',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  mode    => '0644',
  content => "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Change owner recursively
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
$nginx_config = '/etc/nginx/sites-available/default'

file_line { 'update_server_name':
  path    => $nginx_config,
  line    => 'server_name debaycisse.tech;',
  match   => 'server_name _;',
  replace => true,
}

file_line { 'remove_hbnb_static_location':
  path  => $nginx_config,
  line  => 'location /hbnb_static/ {',
  match => 'server_name debaycisse.tech;',
}

file_line { 'remove_hbnb_static_alias':
  path  => $nginx_config,
  line  => 'alias /data/web_static/current/;',
  match => 'location /hbnb_static/ {',
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    File['/data'],
    File_line['remove_hbnb_static_alias'],
  ],
}
