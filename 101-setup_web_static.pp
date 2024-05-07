# check if nginx is installed
exec { 'check_nginx':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y nginx',
  unless  => '/usr/bin/test -x /usr/sbin/nginx',
}

# Create directories
exec { 'create a nested of folders for the first folders':
  command => 'mkdir -p /data/web_static/releases/test',
  path    => '/usr/bin',
}

exec { 'create a nested of folders for the second folders':
  command => 'mkdir -p /data/web_static/shared',
  path    => '/usr/bin',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Change ownership recursively
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}


exec { 'insert_content_at_line_53':
  command  => 'sed -i \'53i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/releases/;\n\t}\' /etc/nginx/sites-available/default',
  provider => shell,
}

# Restart Nginx
exec { 'restart nginx service':
  command  => 'sudo service nginx restart',
  path     => '/usr/bin',
  provider => 'shell',
}

