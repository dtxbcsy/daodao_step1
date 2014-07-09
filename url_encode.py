import urllib
import os
import sys

sys.stdout.write("%s\n"%urllib.quote_plus(sys.stdin.readline().strip()))
