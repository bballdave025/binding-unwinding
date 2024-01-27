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
by moving the files to a folder that is part of the main
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

### Version that allows output, but runs more slowly

(Below is the version that doesn't show output and runs more quickly.)

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
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
echo "my_end: ${my_end}";
my_second=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
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
  && echo -e "        ... success\n" | tee -a rename.out \
  || echo -e "        ... FAILURE\n" | tee -a rename.out
'
```

or, if you don't want to see any display 
(and/or want it to complete faster),

### Version that doesn't write to `stdout`, but runs more quickly

(Above is the version that _does_ show output and runs more slowly.)

```
find . -type f -iname "*.png" > fnames.lst; \
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" >> rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
my_second=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
my_num=0;
my_unpad=$(echo "${my_second}+1" | bc);
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
new_fname="${my_first}${my_num}${my_end}";
echo "  Command will be:" >> rename.out;
echo "mv \"${orig}\" \"${new_fname}\"" >> rename.out;
echo "    ..." >> rename.out;
mv "${orig}" "${new_fname}" \
  && echo -e "        ... success\n" >> rename.out \
  || echo -e "        ... FAILURE\n" >> rename.out
'
```

_(If you get nervous about progress and want to make sure things
are actually happening, open another terminal, go to the same
directory where you ran the previous command, and use the
command,_ `tail -f rename.out` _.)_

## Checking for rename errors

Then you can use

&lt;joke&gt;

```
grep --failure rename.out
echo "# failure is not an option; hahahaha!"
```

&lt;joke&gt;

Okay, actually use

```
grep -i failure rename.out | wc -l
```

You should get `0` if everything worked right. If not,
there was some kind of error with one or more move(s).
You'll need to look through `rename.out` to find out what
it was. If the number is big, you'll probably just need
to look at the whole file.

If the number was somewhat small, try

```
grep -C 5 -i failure | rename.out
```

and see if you can find the problem.

## Reproducibility Stuff (Example `conda` environment)

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

<b>Edit</b>:

The enough-for-recreating-the environment filename is

[find-binding-and-unwind.yml](./find-binding-and-unwind.yml)

The complete environment - with everything that was installed
(by `conda` or `pip` - has the filename,

[complete-conda-env_find-binding-and-unwind_1706253430_2024-01-26T001710-0700.yml](https://github.com/bballdave025/binding-unwinding/blob/main/complete-conda-env_find-binding-and-unwind_1706253430_2024-01-26T001710-0700.yml)


## The channel situation after converting everything to PNG

### Pre-steps

`# ` Change JPG to truecolor (to make grayscale images 3-channel.
`#+` This gets undone, later, so it'll be best to _not_ do it here,
`#+` but to redo it later

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ mogrify -verbose -colorspace srgb -type truecolor *.jpg \
>  2>&1 | tee mogrify2srgbtruecolor_$(date +'%s_%Y-%m-%dT%H%M%S%z').out

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -iname "FamilySearch*.jpg" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
convert "${orig}" -colorspace HSB -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info:;
' 2>&1 | \
  tee -a test_FS_grayscaleness_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
### ... OUTPUT ... all zeros ...

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -not -iname "FamilySearch*.jpg" \
  -a -not -iname "*.out" -a -not -iname "*.lst" \
  -a -not -iname "*.log" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
convert "${orig}" -colorspace HSB -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info:;
' 2>&1 | \
  tee -a test_nonFS_grayscaleness_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
### ... OUTPUT ...

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ sort test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out | uniq -c | head -n 3
     17 0
      1 0.0648579
      1 0.18425
```

There are 17 grayscale (or possibly binary) images.

#### Convert all to PNG

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ mogrify -verbose -path ../try_magick_1pass_output/ \
>         -format png \
>     PNG24:*.jpg PNG24:*.png \
>   2>&1 | tee mogrify2png24_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```

##### Checking

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ cd ../try_magick_1pass_output

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cp ../try_magick_1pass_input/*.out .

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[magick] %[colorspace] %[type] %[extension] %[bit-depth] %[channels]\n" *.png | tee -a best_converted2png_specs_id_$(date +'%s_%Y-%m-%dT%H%M%S%z').out


Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ identify -format "%[magick] %[colorspace] %[type] %[extension] %[bit-depth] %[channels]\n" *.png | tee -a best_short_converted2png_specs_id_$(date +'%s_%Y-%m-%dT%H%M%S%z').out

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cat nonFS_grayscale_fnames_with_count.lst
0 BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
0 BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
0 Bodleian-Library-MS-Bodl-168_p0-11.png
0 Bodleian-Library-MS-Hatton-113_00001.png
0 Bodleian-Library-MS-Hatton-114_00001.png
0 Hungary_winkler1_p105-377.png
0 Hungary_winkler1_p230-836.png
0 Hungary_winkler1_p260-951.png
0 Hungary_winkler1_p29-102.png
0 Hungary_winkler1_p54-192.png
0 Hungary_winkler1_p60-215.png
0 Hungary_winkler1_p71-257.png
0 Hungary_winkler1_p72-261.png
0 Hungary_winkler1_p73-265.png
0 Hungary_winkler1_p74-269.png
0 Hungary_winkler1_p84-306.png
0 Hungary_winkler1_p99-356.png

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ find . -type f -iname "FamilySearch*.png" | sed 's#^[.]/##g' > FS_grayscale_fnames.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $2}' nonFS_grayscale_fnames_with_count.lst > nonFS_grayscale_fnames.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cat nonFS_grayscale_fnames.lst FS_grayscale_fnames.lst > grayscale_fnames.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ wc -l < grayscale_fnames.lst
318

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $2}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 Gray
    627 sRGB

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # good

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $1}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    945 PNG

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $2}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 Gray
    627 sRGB

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $3}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
      2 Bilevel
    316 Grayscale
      1 Palette
    621 TrueColor
      5 TrueColorAlpha

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ head best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out
PNG Gray Bilevel png 1 gray
PNG Gray Bilevel png 1 gray
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb
PNG sRGB TrueColor png 8 srgb

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # I'll need to find the Bilevel, Palette, and TrueColorAlpha

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $4}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    945 png

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $5}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
      2 1
    943 8

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $6}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 gray
    622 srgb
      5 srgba

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$
```

#### Get everything in the format we'd like

Details in [bashlog.log.md](./bashlog.log.md). Even more details in
[bashlog.log](./bashlog.lob)