#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont #dynamic import
import cv2
import glob
import os

onlyGifs = glob.glob("*.png")

size = 512, 512

for i in onlyGifs:
  #img = Image.open(i).convert('L')
  #img.thumbnail(size, Image.ANTIALIAS)
  #img.save(os.path.splitext(i)[0] + ".png",'png', optimize=True, quality=70)
  img = cv2.imread(i)
  resized = cv2.resize(img, size)
  cv2.imwrite(i, resized)
