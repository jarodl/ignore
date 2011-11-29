import os
import string
import urllib2
from sys import stdout

class Ignore:

    def __init__(self):
        """docstring for __init__"""
        self.source = 'https://raw.github.com/github/gitignore/master/'

    def __should_overwrite(self, file):
        if os.path.isfile(file):
            overwrite = raw_input(".gitignore exists, overwrite [y/N]? ")
            return string.capitalize(overwrite) == 'Y'
        else:
            return False

    def get_file(self, lang, destination=os.getcwd()):
        url = self.source + string.capitalize(lang) + '.gitignore'
        file_name = os.path.join(destination, '.gitignore')
        if self.__should_overwrite(file_name) is False:
            return
        try:
            response = urllib2.urlopen(url)
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
