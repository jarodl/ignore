import os
import string
import urllib2
from sys import stdout

class Ignore:

    def __init__(self):
        """docstring for __init__"""
        self.source = 'https://raw.github.com/github/gitignore/master/'

    def get_file(self, lang, destination=os.getcwd()):
        self.source += string.capitalize(lang) + '.gitignore'
        file_name = '.gitignore'
        try:
            response = urllib2.urlopen(self.source)
        except urllib2.HTTPError, e:
            print '%s: The server could not fulfill the request.' % e.code
        except URLError, e:
            print 'Failed to reach the server: %s' % e.reason
        else:
            ignore_file = open(file_name, 'wb')
            meta = response.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            stdout.write("Downloading")

            downloaded = 0
            block_size = 8
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                downloaded += len(buffer)
                ignore_file.write(buffer)
                stdout.write('.')
            stdout.write('\n')
            ignore_file.close()
