from django.test import TestCase
from datetime import datetime
import qrcode

# Create your tests here.
img = qrcode.make(r'http://10.159.0.38:8000/checkstand/incomeday/')
img.save("wangzhi.jpg")

