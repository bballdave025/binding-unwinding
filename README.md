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
with are relevant to family history - deeds, contracts,
arrest records, and other things that were hanging around
the convent or administrative center which were deemed
old, superfluous, or otherwise waste.

Further, the plan is to train similar models to identify
stitching (including embroidery), iron-gall-ink corrosion,
pages with pen trials and alphabets, and some other 
classifications that I'm not going to take the time to
remember right now. I've got to get the data and train and
write before the 30 January 2024 submission deadline.

## Rename command after extraction of images

Rather than work with all the printf formatting, I just
rename the output as follows. This is with `bash`.

```
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" | tee -a rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
echo;
echo "orig: ${orig}";
my_first=$(echo "${orig}" | sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
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
  my_num="${my_second}";
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
