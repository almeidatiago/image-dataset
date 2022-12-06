#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont #dynamic import

import glob
import os

onlyGifs = glob.glob("*.JPEG")

size = 512, 512

for i in onlyGifs:
  img = Image.open(i).convert('L')
  img.thumbnail(size, Image.ANTIALIAS)
  img.save(os.path.splitext(i)[0] + ".png",'png', optimize=True, quality=70)
