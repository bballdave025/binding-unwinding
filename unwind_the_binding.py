#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~

##############################################################################
#
# @file: unwind_the_binding.py
# @author: David BLACK    GH: @bballdave025
#          based on (and maybe only using)
#          https://stackoverflow.com/a/47877930/6505499
#          from @kateryna
# @since: 2024-01-22
#
# @requirements :
# % pip install --upgrade pip
# % pip install --upgrade pymupdf
# % pip install tqdm
#
##############################################################################

import os
import fitz
from tqdm import tqdm

just_one_pdf_at_a_time = True

fromdir = "C:/David/__General_Reference/P2/_pdfs_for_images_-_workdir"
outdir = "C:/David/__General_Reference/P2/_images_from_pdfs_-_workdir"

for each_path in os.listdir(fromdir):
  if ".pdf" in each_path:
    doc = fitz.Document((os.path.join(fromdir, each_path)))
    
    for i in tqdm(range(len(doc)), desc="pages"):
      for img in tqdm(doc.get_page_images(i), desc="page_images"):
        xref = img[0]
        image = doc.extract_image(xref)
        pix = fitz.Pixmap(doc, xref)
        pix.save(os.path.join(outdir,
                              "%s_p%s-%s.png" % (each_path[:-4], i, xref))
        )
      ##endof:  for img
    ##endof:  for i in tqdm
  ##endof:  if ".pdf"
##endof:  for each_path

if just_one_pdf_at_a_time:
  print("Done!")
  