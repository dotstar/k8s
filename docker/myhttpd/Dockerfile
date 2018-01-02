from httpd:2.2
# Make sure we know which version of httpd.conf we are
# work with and add simeple "hostname" cgi script
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY htdocs/index.html /usr/local/apache2/htdocs/
COPY cgi-bin/hello.cgi /usr/local/apache2/cgi-bin/hello.cgi
RUN chmod 755 /usr/local/apache2/cgi-bin/hello.cgi

