from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='up%kah)sn=)-%-4-&*1@(m52$dhk5u@c9*$z+xn58^=@j$f&yy')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
