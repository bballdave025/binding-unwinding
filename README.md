# binding-unwinding
Use for getting MS images from combined image files.

Starting 1705978217_2024-01-22T195017-0700

# Project for the 2024 Family History Technology Workshop

I'm hoping I can get this nice ML project in for my GitHub,
but also for the Workshop/Conference, which could help me
get a job.

I have PDFs of MSs (manuscripts) with many images. Tons of
these are in the public domain. This is the specific part for
the image extraction.

The images will make a dataset to train a model that should
recognize when waste manuscripts / binder's waste / 
fragments in situ are part of an image. This should make
possible the finding of new fancy MSs as well as those
with relevance to family history - deeds, contracts,
arrest records, and other things that were hanging around
the convent or administrative center which were deemed
old, superfluous, or otherwise waste.

Further, the plan is to train similar models to identify
stitching (including embroidery), iron-gall-ink corrosion,
pages with pen trials and alphabets, and some other 
classifications that I'm not going to take the time to
remember right now. I've got to get the data and train and
write before the 30 January 2024 submission deadline.

## Prerequisites before running

```
pip install --upgrade pip
pip install --upgrade pymupdf
pip install tqdm
```

## Usage

Right now, you change the hardcoding according to the
directory with your next PDF(s) in the `fromdir`, 
or you make sure `fromdir` contains the PDF(s) you want.
You can also change `outdir` if you want the images to
go to a different directory. 

<b>I'll show my first run of the program.</b> 

I got rid of everything
in `C:/David/__General_Reference/P2/_pdfs_for_images_-_workdir`,
moving any needed files so as not to lose them. I also cleared out
`C:/David/__General_Reference/P2/_images_from_pdfs_-_workdir"` 
by copying the files to a folder that is part of the main
dataset.

In `unwind_the_binding.py`, I hardcoded the following lines
(changing the strings to where I put the PDF and where I wanted
the images). (More accurately, I just put new PDFs in those dirs,
since I had decided that I wanted those to be my working directories - 
workdirs.)

```
fromdir = "C:/David/__General_Reference/P2/_pdfs_for_images_-_workdir"
outdir = "C:/David/__General_Reference/P2/_images_from_pdfs_-_workdir"
```

### The really important command

```
python unwind_the_binding.py
```

#### The progress output

(so you know what to expect)

At the start:

```
(familysearch-interview) C:\bbd025\repos_man\binding-unwinding>python unwind_the_binding.py
page_images: 100%|██████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 113.85it/s]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.97s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.12s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.81s/it]
pages:   2%|█▍                                                                         | 4/208 [00:05<05:24,  1.59s/it]
page_images:   0%|                                                                               | 0/1 [00:00<?, ?it/s]
```

...

At the end:

```
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.05s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.06s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.06s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.06s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.43s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.08s/it]
page_images: 100%|███████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.49it/s]
pages: 100%|█████████████████████████████████████████████████████████████████████████| 208/208 [07:15<00:00,  2.09s/it]
Done!

(familysearch-interview) C:\bbd025\repos_man\binding-unwinding>
```


## Rename command after extraction of images

Rather than work with all the printf formatting, I just
rename the output as follows. This is with `bash` (specifically
Cygwin, since I'm running the Python from windows at this moment).
You need to be in the `outdir` directory when you run this command.

```
find . -type f -iname "*.png" > fnames.lst; \
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" | tee -a rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
echo;
echo "orig: ${orig}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
echo "my_first: ${my_first}";
my_end=$(echo "${orig}" | sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
echo "my_end: ${my_end}";
my_second=$(echo "${orig}" | sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
echo "my_second: $my_second";
my_num=0;
my_unpad=$(echo "${my_second}+1" | bc);
echo "my_unpad: ${my_unpad}";
my_num=0;
if [ $my_unpad -lt 10 ]; then
  my_num="0000${my_unpad}";
elif [ $my_unpad -lt 100 ]; then
  my_num="000${my_unpad}";
elif [ $my_unpad -lt 1000 ]; then
  my_num="00${my_unpad}";
elif [ $my_unpad -lt 10000 ]; then
  my_num="0${my_unpad}";
else
  my_num="${my_unpad}";
fi;
echo "my_num: ${my_num}";
new_fname="${my_first}${my_num}${my_end}";
echo "  Command will be:" | tee -a rename.out;
echo "mv \"${orig}\" \"${new_fname}\"" | tee -a rename.out;
echo "    ..." | tee -a rename.out;
mv "${orig}" "${new_fname}" \
  && echo "        ... success" | tee -a rename.out \
  || echo "        ... FAILURE" | tee -a rename.out
'
```

## Reproducibility Stuff (Example `conda` environment

The full output from `conda env export` isin the
[`complete_conda_env_2024-01-22.yml`](./complete_conda_env_2024-01-22.yml) 
file. That file is
specifically for my Windows 10 64-bit architecture.

For OS-independence, it should work with using the
results of starting an environment from
[`familysearch_interview.yml`](./familysearch_interview.yml) 
and adding lines according
to the _Prerequisites_ section, above. i.e. under the
`pip` section, add the lines

```
      - pymupdf==1.23.17
      - tqdm==4.66.1
```

Actually, those two are pretty much _all_ you need for the
PDF-to-image part. The other parts of the environment are
a start for the model building. (More dependencies will likely
be added after today - after 2024-01-22.)