from django.test import TestCase
from datetime import datetime
import qrcode

# Create your tests here.
d = {'a': 1, 'b': 4, 'c': 2}
print(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))
