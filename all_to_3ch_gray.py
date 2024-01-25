#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

##############################################################################
#
# @file: all_to_3ch_gray.py
# @author: David BLACK    GH: @bballdave025
#          based on (and expanding)
#          https://stackoverflow.com/a/58791118/6505499
#          from @Alexey_Antonenko
# @since: 2024-01-24
#
# @requirements :
# % pip install --upgrade pip
# % pip install numpy
# % pip install scipy
# % pip install pillow
#
#  This code will take any PNG or JPG files in the given directory and get
#+ them into 3-channel (24-bit) JPG files. If an image is in standard
#+ grayscale (8-bit), it will be converted into a R=G=B image, so it will
#+ display as grayscale, but can be fed into programs (like the
#+ TensorFlow/Keras CNN model I'm wanting to work with) that take 3-channel
#+ images.
#
#+ Eventually, this and the  unwind_the_binding.py  scripts will be put into
#+ a python class.
#
##############################################################################



dir_with_imgs_to_convert = ""

