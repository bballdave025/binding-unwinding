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
$ identify -format "%[magick] %[colorspace] %[type] %[extension] %[bit-depth] %[channels]\n" *.png | tee -a best_short_converted2png_spects_id_$(date +'%s_%Y-%m-%dT%H%M%S%z').out

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
$ awk '{print $2}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 Gray
    627 sRGB

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # good

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $1}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    945 PNG

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $2}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 Gray
    627 sRGB

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $3}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
      2 Bilevel
    316 Grayscale
      1 Palette
    621 TrueColor
      5 TrueColorAlpha

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ head best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out
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
$ awk '{print $4}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    945 png

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $5}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
      2 1
    943 8

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ awk '{print $6}' best_short_converted2png_spects_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 gray
    622 srgb
      5 srgba

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$
```

#### Get everything in the format we'd like

```
Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ head best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out


BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
-----
PNG Gray Bilevel png 1 gray


BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
-----
PNG Gray Bilevel png 1 gray

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 Bilevel best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
-----
PNG Gray Bilevel png 1 gray
--
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
-----
PNG Gray Bilevel png 1 gray

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 Bilevel best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | wc -l
2

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 Bilevel best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | tee bilevel_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 Grayscale best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | grep -i "FamilySearch" > FS_grayscale_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst
```

####################
# COME HERE
####################

```
Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ wc -l < FS_grayscale_to_convert_1706290260_2024-01-26T103100-0700.lst         301

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 Grayscale best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | grep -iv "FamilySearch" > nonFS_grayscale_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ wc -l < nonFS_grayscale_to_convert_1706290316_2024-01-26T103156-0700.lst
15

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # 15 grayscale and 2 bilevel = 17 with saturation 0

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # grep -B2 srgba best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" > srgba_w_alpha_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # grep -B2 srgba best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | wc -l

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # grep -B2 srgba best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | wc -l

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # grep -B2 TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | wc -l

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ vim best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | wc -l
19

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | wc -l
5

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ grep -B2 TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" > srgba_w_alpha_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ wc -l srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst
5 srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cat ./*to_convert*.lst | sort -u | wc -l
323

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ echo "301+15+2+5" | bc
323

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # Yay!

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cat ./*to_convert*.lst | sort -u > z_all_to_convert.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ head z_all_to_convert.lst
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
Bodleian-Library-MS-Bodl-168_p0-11.png
Bodleian-Library-MS-Hatton-113_00001.png
Bodleian-Library-MS-Hatton-114_00001.png
FamilySearch_-_DGS004534286_00001.png
FamilySearch_-_DGS004534286_00002.png
FamilySearch_-_DGS004534286_00003.png
FamilySearch_-_DGS004534286_00004.png
FamilySearch_-_DGS004534286_00005.png

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ ls *.lst
FS_grayscale_fnames.lst
FS_grayscale_to_convert_1706290260_2024-01-26T103100-0700.lst
bilevel_to_convert_1706290167_2024-01-26T102927-0700.lst
grayscale_fnames.lst
nonFS_grayscale_fnames.lst
nonFS_grayscale_fnames_with_count.lst
nonFS_grayscale_to_convert_1706290316_2024-01-26T103156-0700.lst
srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst
z_all_to_convert.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.png" | sort -u > z_all_anything.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.png" | sed 's#^[.]/##g;' | sort -u > z_all_anything.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ wc -l z_all_anything.lst
945 z_all_anything.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # What we want

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ comm -1 z_all_to_convert.lst z_all_anything.lst | wc -l
945

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ comm -2 z_all_to_convert.lst z_all_anything.lst | wc -l
323

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ comm -3 z_all_to_convert.lst z_all_anything.lst | wc -l
622

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ echo "622+323" | bc
945

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ # checks

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ comm -3 z_all_to_convert.lst z_all_anything.lst > z_all_not_converted.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ wc -l z_all_not_converted.lst
622 z_all_not_converted.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ ls *.lst
FS_grayscale_fnames.lst
FS_grayscale_to_convert_1706290260_2024-01-26T103100-0700.lst
bilevel_to_convert_1706290167_2024-01-26T102927-0700.lst
grayscale_fnames.lst
nonFS_grayscale_fnames.lst
nonFS_grayscale_fnames_with_count.lst
nonFS_grayscale_to_convert_1706290316_2024-01-26T103156-0700.lst
srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst
z_all_anything.lst
z_all_not_converted.lst
z_all_to_convert.lst

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cp grayscale_fnames.lst _convert_grayscale.list

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cp srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst _convert_w_alpha.list

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cp bilevel_to_convert_1706290167_2024-01-26T102927-0700.lst _convert_bilevel.list

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ cp z_all_not_converted.lst _maybe_convert_details.list

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ ls *.list
_convert_bilevel.list    _convert_w_alpha.list
_convert_grayscale.list  _maybe_convert_details.list

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$
```

`#` Some quick magick things - not all what I want

```
>>>
https://www.imagemagick.org/discourse-server/viewtopic.php?t=26268

convert in.jpg -channel B -separate out_B.jpg
convert out_B.jpg -type GrayScale -colorspace GRAY out_gray.bmp



http://en.wikipedia.org/wiki/BMP_file_format says the 8-bit/pixel format is for palette files. It doesn't give a non-palette 8-bit format.

Thus:

convert rose: -colorspace gray -type palette b.bmp




I was wrong, bmp does not support grey scale (all 3 channels are needed) and -type should be pallette (but IM fixes that it seems). Sorry for stiring things up.
However, the following work to get the greyscale 8-bit (match output from other programs):

convert in.jpg -colorspace GRAY -colors 256 out.bmp

The key here is the use of -colors.

I noticed that if I use -threshold on the greyscale file, e.g.:

convert out.bmp -threshold 45% out_bw.bmp

something changes and out_bw.bmp is not recoqnized in the same way as out.bmp. Thats a mystery to me (the only change is that pixels are given a new value, 0 or 255).

Thanks for all the help!



When you do -threshold, the result is not grayscale palette, but b/w binary and binary images are not supported by all image formats. I do not know about bmp.

-----
https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=16201

convert logo: -format "%[colorspace]" info:
RGB

convert logo: -type grayscale -format "%[colorspace]" info:
Gray


convert logo: -format "%[channels]" info:
rgb


convert logo: -type grayscale -format "%[channels]" info:
gray


convert logo: -format "%r" info:
PseudoClassRGB


convert logo: -type grayscale -format "%r" info:
PseudoClassGray


Unique colors:
convert logo: -format "%k" info:
232

------------------


The PNG colour types do not apply to JPEG images, so you can't use the same technique. Try **forcing the colorspace to sRGB**, and/or **setting the type to TrueColour** so you don't get a palettised image:

                  **************** ***************
convert input.jpg -colorspace sRGB -type truecolor result.jpg




???
image-magick refuses to process png, but ffmpeg does not.

ffmpeg -loglevel warning -i ${file} -sws_flags "lanczos+accurate_rnd+full_chroma_int+full_chroma_inp+bitexact" -y -pix_fmt rgb8 test.png

reported depth of end file is 8 bit. (also useful for rgba → rgb.)
???



----------------

****************************
****************************


https://stackoverflow.com/questions/34305379/how-to-convert-gray-scale-png-image-to-rgb-from-comand-line-using-image-magick

You can try this command 

                 ******************** *****   (maybe, but why truecolormatte (?))
convert gray.png -type truecolormatte PNG32:color.png, 

which convert a gray png named gray.png to be a true color png named color.png.



****

If, as your question title implies, you really just want to **go from greyscale to sRGB colorspace**, use this:

                  ************************
convert image.png -define png:color-type=2 result.png

I check it like this:

convert image.png -define png:color-type=2 result.png && identify -format "%[colorspace]" result.png
sRGB


-----




*************************************
How do I convert a RGB image (3 channels) to a grayscale one, using the (r+g+b)/3 method? I look through an examples page: http://www.imagemagick.org/Usage/color_mods/#grayscale but the desired method:

****************************************************
convert test.png -fx '(r+g+b)/3' gray_fx_average.png

gave me a wrong result - the resulted image has still 3 channels.

You can check this by running a command: 

identify -format "%[colorspace]   <== %f\n" *.png.
*************************************

-----

<wrong colorspace, but good idea>

convert test.png -fx '(r+g+b)/3' -colorspace Gray gray_fx_average.png

--------------------

More backward ways of going RGB to 1-channel grayscale:

A few ways to that in Imagemagick command line are:

convert test.png -grayscale average gray_average.png

or

convert test.png -colorspace OHTA -channel r -separate +channel gray_average.png

or

convert test.png -intensity average -colorspace gray gray_average.png

or

convert test.png -colorspace HSI -channel blue -separate +channel gray_average.png

See

https://imagemagick.org/script/command-line-options.php#grayscale https://imagemagick.org/script/command-line-options.php#intensity https://imagemagick.org/script/command-line-options.php#colorspace

-----

Somewhat possibly useful for Python.

https://stackoverflow.com/questions/49144590/to-convert-a-grayscale-image-to-rgb-image-using-pil

https://stackoverflow.com/questions/68352065/how-to-check-whether-a-jpeg-image-is-color-or-grayscale-using-only-python-pil

***
https://stackoverflow.com/questions/62030730/python-grayscale-image-to-rgb

***
https://stackoverflow.com/questions/21596281/how-does-one-convert-a-grayscale-image-to-rgb-in-opencv-python

-----



I had an issue to convert an sRGB colorspace to a Gray colorspace. I had to delete Alpha channel manually before a conversion. In other case, the image will stay sRGB.

convert image_original.tga -alpha off -set colorspace Gray image_converted.tga

### DWB

Mine:
                   ********** *************************
convert orig_srgba -alpha off -set colorspace TrueColor converted


-----

https://unix.stackexchange.com/questions/689906/imagemagick-not-converting-grayscale-to-rgb

Trying to use ImageMagick to resize, convert images from grayscale to RGB, and from jpg to png. Using the flags to convert to RGB as per: https://stackoverflow.com/a/34875248

                 **************** ***************
convert test.jpg -colorspace sRGB -type truecolor -resize 100x100^ -gravity center -extent 100x100 test.png

The resize works, and the jpg to png works, but the image stays grayscale. Why doesn't this work?



----
https://imagemagick.org/discourse-server/viewtopic.php?t=24801

Convert 8bit grayscale jpeg image to 24bit ...

ImageMagick
https://imagemagick.org › Board index › Developers
Jan 14, 2014 — My first reply was wrong. Jpegs can have just one channel. 
                     ***************
As magick suggests, "-type truecolor" ensures it has 3 channels.



-----


Have you tried adding -define png:color-type=6 in your command? – 
Mark Setchell
 Apr 21, 2015 at 19:38

                                     ************* (but PNG24)
Or try specifying the output file as PNG32:out.png – 
Mark Setchell
 Apr 21, 2015 at 19:40

-define png:color-type=6 looks like it worked. If you want to put that in an answer, I'll accept it. – 
superstator
 Apr 21, 2015 at 19:59


You might try using a -define to force the output image type to PNG Color-Type 6 like this:

                      ************************ ********** (but see below
convert input.png ... -define png:color-type=6 output.png

       ****************
****Or png:color-type=2 if you don't care about alpha channel ****

```