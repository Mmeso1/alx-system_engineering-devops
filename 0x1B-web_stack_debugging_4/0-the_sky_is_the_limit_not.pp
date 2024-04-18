#Sky is the limit, let's bring that limit higher
exec { 'increase nginx timeout':
  provider => shell,
  command  => 'sed -i s/15/3000000/ /etc/default/nginx'
}
exec { 'restart nginx server':
  provider => shell,
  command  => 'service nginx restart'
}
