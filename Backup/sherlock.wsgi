import sys
import site
site.addsitedir('/home/ubuntu/.local/lib/python2.7/site-packages')
sys.path.insert(0, '/var/www/html/sherlock')
print sys.path
from sherlock import app as application
