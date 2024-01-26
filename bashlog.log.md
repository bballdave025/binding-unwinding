### Figuring out renaming of images from `unwind_the_binding.py`

```
bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$ find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}"; 
echo "orig: ${orig}"; 
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-]\([0-9]\+\)\([.]png\)$#\1#g'"'"'); 
echo "my_first: ${my_first}";
' | head -n 30
orig: ./Heidelberg_-_salVII73__z4_p0-5.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p1-14.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p10-69.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p100-613.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p101-619.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p102-625.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p103-631.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p104-637.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p105-643.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p106-649.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p107-655.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p108-661.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p109-667.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p11-75.png
my_first: Heidelberg_-_salVII73__z4_p
orig: ./Heidelberg_-_salVII73__z4_p110-673.png
my_first: Heidelberg_-_salVII73__z4_p
xargs: bash: terminated by signal 13

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$

# WORKING ON COMMAND


find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c ' 
orig="{}"; 
echo "orig: ${orig}"; 
my_first=$(echo "${orig}" | sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"'); 
echo "my_first: ${my_first}"; 
my_end=$(echo "${orig}" | sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"'); 
echo "my_end: ${my_end}"; 
my_second=$(echo "${orig}" | sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"'); 
echo "my_second: $my_second";
my_unpad=$(echo "${my_second}+1" | bc);
echo "my_unpad: ${my_unpad}";
my_num=0;' | \
head -n 30 


bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$ find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
echo "orig: ${orig}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
echo "my_first: ${my_first}";
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
echo "my_end: ${my_end}";
my_second=$(echo "${orig}" | \
sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
echo "my_second: $my_second";
my_unpad=$(echo "${my_second}+1" | bc);
echo "my_unpad: ${my_unpad}";
my_num=0;' | \
head -n 30
orig: ./Heidelberg_-_salVII73__z4_p0-5.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 0
my_unpad: 1
orig: ./Heidelberg_-_salVII73__z4_p1-14.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 1
my_unpad: 2
orig: ./Heidelberg_-_salVII73__z4_p10-69.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 10
my_unpad: 11
orig: ./Heidelberg_-_salVII73__z4_p100-613.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 100
my_unpad: 101
orig: ./Heidelberg_-_salVII73__z4_p101-619.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 101
my_unpad: 102
orig: ./Heidelberg_-_salVII73__z4_p102-625.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 102
my_unpad: 103
xargs: bash: terminated by signal 13

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$ find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
echo "orig: ${orig}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
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
  my_num="${my_second}"; 
fi;
echo "my_num: ${my_num}";
' | \
head -n 30
orig: ./Heidelberg_-_salVII73__z4_p0-5.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 0
my_unpad: 1
my_num: 00001
orig: ./Heidelberg_-_salVII73__z4_p1-14.png
my_first: Heidelberg_-_salVII73__z4_p
my_end: .png
my_second: 1
my_unpad: 2
my_num: 00002
orig: ./Heidelberg_-_salVII73__z4_p10-69.png
my_first: Heidelberg_-_salVII73__z4_p

###                    ||| ###
### ... LOTS OF OUTPUT ... ###
###                    ||| ###

my_unpad: 98
my_num: 00098
  Command will be:
mv "./Heidelberg_-_salVII73__z4_p97-595.png" "Heidelberg_-_salVII73__z4_00098.png"
    ...
        ... success

orig: ./Heidelberg_-_salVII73__z4_p98-601.png
my_first: Heidelberg_-_salVII73__z4_
my_end: .png
my_second: 98
my_unpad: 99
my_num: 00099
  Command will be:
mv "./Heidelberg_-_salVII73__z4_p98-601.png" "Heidelberg_-_salVII73__z4_00099.png"
    ...
        ... success

orig: ./Heidelberg_-_salVII73__z4_p99-607.png
my_first: Heidelberg_-_salVII73__z4_
my_end: .png
my_second: 99
my_unpad: 100
my_num: 00100
  Command will be:
mv "./Heidelberg_-_salVII73__z4_p99-607.png" "Heidelberg_-_salVII73__z4_00100.png"
    ...
        ... success

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$ grep -i failure rename.out

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2/_images_from_pdfs_-_workdir
$
```

```
######################################
#NEW DAY 2024-01-23
######################################
```


### Backing up 

`#` Files and structure before moves for classification

```
bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ echo "# Files and structure before moves for classification" > \
    file_structure_pre_classification_$(date +'%s_%Y-%m_%dT%H%M%S%z').txt

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ cat file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ echo >> file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ echo \
> "------------------------------------------------------------------------" \
> >> file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ echo >> \
> file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ vim file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt

bballdave025@MY-MACHINE /cygdrive/c/David/__General_Reference/P2
$ 
dashes="----------------------------------------------------------"; \
while read -r line; do \
  echo "DIRECTORY: ${line}" >> \
    file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt; \
  tree --charset=ascii "${line}" >> \
    file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt; \
  echo >> \
    file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt; \
  echo >> \
    file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt; \
done < dirs_for_tree.txt
```


### From above, we have a checkpoint at our path to the P2 base

```
file_structure_pre_classification_1706026133_2024-01_23T090853-0700.txt
```


##  Here, moved whole `P2` directory tree to external HD

Now, it's at

```
D:\Datasets_and_Models\P2_MSS
```

a.k.a.

```
D:/Datasets_and_Models/P2_MSS
```

a.k.a. (for me)

```
/cygdrive/d/Datasets_and_Models/P2_MSS
```

```
##################
# Diff't terminal
##################

#  For Utrecht PDF (with something messed up)
#+ THIS IS NOT THE NORMAL RENAME!
```

```
find . -type f -iname "*.png" > fnames.lst; \
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" >> rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-]\([0-9]\+\)\([.]png\)$#\1#g'"'"');
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-]\([0-9]\+\)\([.]png\)$#\4#g'"'"');
my_third=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-]\([0-9]\+\)\([.]png\)$#\3#g'"'"');
my_num=0;
my_unpad="${my_third}";
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
echo "    ..." | tee -a rename.out; # dang, left '| tee -a', not '>>'
mv "${orig}" "${new_fname}" \
  && echo -e "        ... success\n" >> rename.out \
  || echo -e "        ... FAILURE\n" >> rename.out
'

#+ THAT WAS NOT THE NORMAL RENAME!
```


### Converting FamilySearch images from 8-bit to 24-bit

`#` That just means from 1-channel to 3-channel

```
#######################
# Diff't day
#######################

#  Folder with all of my FamilySearch images (grayscale) 
#+ for one classification.

# https://stackoverflow.com/questions/69703263/
# https://stackoverflow.com/questions/13317753/
```

```
bballdave025@MY-MACHINE ~
$ type magick
magick is hashed (/usr/bin/magick)

bballdave025@MY-MACHINE ~
$ cd 'D:\Datasets_and_Models\P2_MSS\DatasetBinding\__No_Reuse\_FSGray_No'

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse/_FSGray_No
$ magick mogrify -colorspace srgb -type truecolor *.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse/_FSGray_No
$ mv *.jpg ../

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse/_FSGray_No
$ cd ../../__Yes_Reuse/_FSGray_Yes/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ find . -type f -name "*.jpg" | wc -l
16

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ # The other one had 280 and seemed to take on the order of minutes

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ time magick mogrify -colorspace srgb -type truecolor *.jpg

real    0m13.026s
user    0m12.936s
sys     0m6.780s

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ date +'%s_%Y-%m-%dT%H%M%S%z'
1706140302_2024-01-24T165142-0700
```


### Doing the train/eval/test split

```
bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ date
Wed Jan 24 16:51:46 MST 2024

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ mv *.jpg ../

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse/_FSGray_Yes
$ cd ..

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse
$ ls _FSGray_Yes

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse
$ rm -rf _FSGray_Yes/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__Yes_Reuse
$ cd ../__No_Reuse/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse
$ find . -type d
.
./_FSGray_No

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse
$ ls _FSGray_No/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse
$ rm -rf _FSGray_No/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/__No_Reuse
$ cd ..

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding
$ mv __Yes_Reuse/ ___Yes_Reuse/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding
$ mv __No_Reuse/ ___No_Reuse/

$ find . -mindepth 1 -maxdepth 1 -type d | sort -r
./___Yes_Reuse
./___No_Reuse
./__True_hasStitch
./__False_hasStitch
./_InProcess_MS_img_downloads
./_Completed_MS_img_downloads
./Sale_or_Auction_Info_for_Binding
./Possible_Repos_for_Binding
./No_Attribution_or_No_Permission
./DATA_UNORGANIZED_-_toPutInCollectionFolders
```

`#` <b>Thinking about the conversion</b>

```
bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding
$ type convert
convert is /usr/bin/convert

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding
$ cd ___Yes_Reuse/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ find . -type f | wc -l
106

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ for imgfile in *.jpg; do
>   echo "${imgfile}"
> done | head
Bodl_MS-Laud-Misc-155A_00033.jpg
Cologny_-_CodBodmer99-ecod_00001.jpg
Cologny_-_CodBodmer99-ecod_00002.jpg
Cologny_-_CodBodmer99-ecod_013.jpg
Cologny_-_CodBodmer99-ecod_014.jpg
Cologny_-_CodBodmer99-ecod_016.jpg
Cologny_-_CodBodmer99-ecod_017.jpg
Cologny_-_CodBodmer99-ecod_018.jpg
Cologny_-_CodBodmer99-ecod_020.jpg
FamilySearch_-_DGS004534287_00171_-_reuseTrue.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ for imgfile in *.jpg; do \
>   tmp_file=$(echo "${imgfile}" | \
>     sed 's#^\(.*\)\([.]jpg\)$#\1_tmp\2#g'); \
>   echo -e "orig: ${imgfile}\ntemp: ${tmp_file}";
> done | head
orig: Bodl_MS-Laud-Misc-155A_00033.jpg
temp: Bodl_MS-Laud-Misc-155A_00033_tmp.jpg
orig: Cologny_-_CodBodmer99-ecod_00001.jpg
temp: Cologny_-_CodBodmer99-ecod_00001_tmp.jpg
orig: Cologny_-_CodBodmer99-ecod_00002.jpg
temp: Cologny_-_CodBodmer99-ecod_00002_tmp.jpg
orig: Cologny_-_CodBodmer99-ecod_013.jpg
temp: Cologny_-_CodBodmer99-ecod_013_tmp.jpg
orig: Cologny_-_CodBodmer99-ecod_014.jpg
temp: Cologny_-_CodBodmer99-ecod_014_tmp.jpg
```


`##` Thinking about this next command Started at 17:17 (and some change)

```
echo "Beginning at $(date)" | tee -a convert.out && \
echo -e "  i.e.  $(date +'%s')\n" | tee -a convert.out && \
time { \
  for imgfile in *.jpg; do \
    echo | tee -a convert.out; \
  tmpfile=$(echo "${imgfile}" | \
    sed 's#^\(.*\)\([.]jpg\)$#\1_tmp\2#g'); \
  echo -e "orig: ${imgfile}\ntemp: ${tmpfile}" | \
    tee -a convert.out; \
  echo "Starting conversion at $(date +'%s')" | \
    tee -a convert.out; \
  convert "${imgfile}" -fx '(r+g+b)/3' "${tmpfile}" && \
  sleep 1; \
  echo "Conversion complete (as is the one-second sleep)." \
    | tee -a convert.out; \
  echo "Completed at $(date +'%s')" | tee -a convert.out; \
  echo "Moving the temp to the original." | tee -a convert.out; \
  mv "${tmpfile}" "${imgfile}"; \
  echo "Move done at $(date +'%s')" | tee -a convert.out; \
  done; } && \
echo "Done with everything at $(date +'%s')";
```


Nope, that will have problems with PNG files. I'm not sure that
converting to JPG will then allow me to do the RGB`->`3-channel
grayscale with the 

$$ R_{f} = G_{f} = B_{f} = \left(R_{0} + G_{0} + B_{0}\right) / 3 $$

That's the reason I'm not just putting in things to convert
PNG to JPG nor doing  `for imgfile in *.jpg *.png; do` ...


### Finishing the train/eval/test split

```
bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ find . -type f | wc -l
106

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ find . -type f | sed 's#^[.]/##g' > ../all_yes_files.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ wc -l < ../all_yes_files.lst
106

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ shuf ../all_yes_files.lst > tmpf && mv tmpf ../all_yes_files.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ head ../all_yes_files.lst
HermetschwilBndnktnKlstr_CodChart139_046.jpg
FamilySearch_-_DGS008104286_01369_-_reuseTrue.jpg
BeineckeMs1119-10622001_00176.png
HermetschwilBndnktnKlstr_CodChart139_00002.jpg
HermetschwilBndnktnKlstr_CodChart139_018.jpg
HermetschwilBndnktnKlstr_CodChart139_042.jpg
SellerLesEnluminures_-_jacobus-pontanus-60719_-_001_tm-444-binding_-_reuseTrue.jpg
BeineckeMs1119-10622001_00178.png
Heidelberg_-_salVIII8__z3_p186-1143.png
Cologny_-_CodBodmer99-ecod_016.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ sed -n "1, 68p" ../all_yes_files.lst > ../yes_files_train.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ wc -l ../yes_files_train.lst
68 ../yes_files_train.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ echo "68 + 17" | bc
85

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ echo "85+21" | bc
106

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ sed -n "69, 85p" ../all_yes_files.lst > ../yes_files_test-and-dev.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ wc -l < ../yes_files_test-and-dev.lst
17

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ sed -n "86, 106p" ../all_yes_files.lst > ../yes_files_hold-out-test.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ wc -l < ../yes_files_hold-out-test.lst
21

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ tail -n 1 ../yes_files_hold-out-test.lst
HermetschwilBndnktnKlstr_CodChart139_045.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ tail -n 1 ../all_yes_files.lst
HermetschwilBndnktnKlstr_CodChart139_045.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ mkdir -p ../_just_classified_folders

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ mkdir -p ../_just_classified_folders/__Yes_Reuse

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ mkdir -p ../_just_classified_folders/__Not_Reuse

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ mkdir -p ../_just_classified_folders/__Yes_Reuse/yes_for_training/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ mkdir -p ../_just_classified_folders/__Yes_Reuse/yes_for_test-and-dev/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ mkdir -p ../_just_classified_folders/__Yes_Reuse/yes_for_hold-out-test/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ while read -r line; do \
>   fname="${line}"; \
>   cp "${fname}" "../_just_classified_folders/__Yes_Reuse/"\
> "yes_for_training/${fname}"; 
> done < ../yes_files_train.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ while read -r line; do \
>   fname="${line}"; \
>   cp "${fname}" "../_just_classified_folders/__Yes_Reuse/"\
> "yes_for_test-and-dev/${fname}"; \
> done < ../yes_files_test-and-dev.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ while read -r line; do fname="${line}"; cp "${fname}" "../_just_classified_folders/__Yes_Reuse/yes_for_hold-out-test/"; done < ../yes_files_hold-out-test.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ cd ../_just_classified_folders/__Yes_Reuse/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ tar -czf yes_for_hold-out-test.tar.gz yes_for_hold-out-test/*

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ tar -ztvf yes_for_hold-out-test.tar.gz
-rw-r--r-- bballdave025/bballdave025 4936812 2024-01-24 20:07 yes_for_hold-out-test/Bodleian-Library-MS-Bodl-168_p14-102.png
-rw-r--r-- bballdave025/bballdave025  385132 2024-01-24 20:07 yes_for_hold-out-test/Cologny_-_CodBodmer99-ecod_017.jpg
-rw-r--r-- bballdave025/bballdave025  707050 2024-01-24 20:07 yes_for_hold-out-test/Cologny_-_CodBodmer99-ecod_020.jpg
-rw-r--r-- bballdave025/bballdave025 4440007 2024-01-24 20:07 yes_for_hold-out-test/FamilySearch_-_DGS004534287_00171_-_reuseTrue.jpg
-rw-r--r-- bballdave025/bballdave025 9604505 2024-01-24 20:07 yes_for_hold-out-test/Heidelberg_-_salVII73__z4_00248_reuseTrue - Copy.png
-rw-r--r-- bballdave025/bballdave025 6673020 2024-01-24 20:07 yes_for_hold-out-test/Heidelberg_-_salVIII8__z3_p1-14.png
-rw-r--r-- bballdave025/bballdave025 3141173 2024-01-24 20:07 yes_for_hold-out-test/HermetschwilBndnktnKlstr_CodChart139_00001.jpg
-rw-r--r-- bballdave025/bballdave025 2236519 2024-01-24 20:07 yes_for_hold-out-test/HermetschwilBndnktnKlstr_CodChart139_00003.jpg
-rw-r--r-- bballdave025/bballdave025 2320403 2024-01-24 20:07 yes_for_hold-out-test/HermetschwilBndnktnKlstr_CodChart139_00008.jpg
-rw-r--r-- bballdave025/bballdave025 2909007 2024-01-24 20:07 yes_for_hold-out-test/HermetschwilBndnktnKlstr_CodChart139_037.jpg
-rw-r--r-- bballdave025/bballdave025 2518385 2024-01-24 20:07 yes_for_hold-out-test/HermetschwilBndnktnKlstr_CodChart139_041.jpg
-rw-r--r-- bballdave025/bballdave025 2223984 2024-01-24 20:07 yes_for_hold-out-test/HermetschwilBndnktnKlstr_CodChart139_045.jpg
-rw-r--r-- bballdave025/bballdave025 11369996 2024-01-24 20:07 yes_for_hold-out-test/Images_of_medieval_manuscripts_-_University_Library_Utrecht_02854.png
-rw-r--r-- bballdave025/bballdave025  5751333 2024-01-24 20:07 yes_for_hold-out-test/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_002_1057pastedown_reuseTrue.png
-rw-r--r-- bballdave025/bballdave025  3844531 2024-01-24 20:07 yes_for_hold-out-test/UppsalaUniversitet_-_RusticanusDeSanctisC371_p1-7.png
-rw-r--r-- bballdave025/bballdave025  3844328 2024-01-24 20:07 yes_for_hold-out-test/UppsalaUniversitet_-_RusticanusDeSanctisC371_p500-2052.png
-rw-r--r-- bballdave025/bballdave025   766899 2024-01-24 20:07 yes_for_hold-out-test/ZurichZentralbib_-_MsD76-ecod_002.jpg
-rw-r--r-- bballdave025/bballdave025   417659 2024-01-24 20:07 yes_for_hold-out-test/ZurichZentralbib_-_MsD76-ecod_003.jpg
-rw-r--r-- bballdave025/bballdave025  1577764 2024-01-24 20:07 yes_for_hold-out-test/zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p2-22.png
-rw-r--r-- bballdave025/bballdave025  1183131 2024-01-24 20:07 yes_for_hold-out-test/zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p209-1290.png
-rw-r--r-- bballdave025/bballdave025  1507330 2024-01-24 20:07 yes_for_hold-out-test/zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p3-28.png

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ rm -rf yes_for_hold-out-test/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ ls
yes_for_hold-out-test.tar.gz  yes_for_test-and-dev  yes_for_training

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ find yes_for_test-and-dev/ -type f | wc -l
17

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ find yes_for_training/ -type f | wc -l
68

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$ cd ../../___No_Reuse/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Yes_Reuse
$

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ pwd
/cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ find . -type f | wc -l
835

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ find . -type f | sed 's#^[.]/##g' > ../all_no_files.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ wc -l < ../all_no_files.lst
835

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ shuf ../all_no_files.lst > tmpf && mv tmpf ../all_no_files.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ head ../all_no_files.lst
Bodleian-Library-MS-Hatton-114_00514.png
Bodleian-Library-MS-Hatton-113_00013.png
FamilySearch_-_DGS004534286_00327.jpg
FamilySearch_-_DGS008909919_00813.jpg
StGallenStiftsbib_-_CodSang783-ecod_00050.jpg
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00010.png
Bodleian-Library-MS-Bodl-168_p11-84.png
FamilySearch_-_DGS004534287_00729.jpg
FamilySearch_-_DGS007996631_00686.jpg
FamilySearch_-_DGS004534286_00100.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ echo "534+134" | bc
668

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ echo "668+167" | bc
835

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ sed -n "1, 534p" ../all_no_files.lst > ../no_files_train.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ wc -l ../no_files_train.lst
534 ../no_files_train.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ sed -n "535, 668p" ../all_no_files.lst > ../no_files_test-and-dev.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ wc -l ../no_files_test-and-dev.lst
134 ../no_files_test-and-dev.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ sed -n "669, 835p" ../all_no_files.lst > ../no_files_hold-out-test.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ wc -l ../no_files_hold-out-test.lst
167 ../no_files_hold-out-test.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ tail -n 1 ../no_files_hold-out-test.lst
FamilySearch_-_DGS008909919_00376_-_stitchTrue.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ tail -n 1 ../all_no_files.lst
FamilySearch_-_DGS008909919_00376_-_stitchTrue.jpg

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ mkdir -p ../_just_classified_folders/__Not_Reuse/no_for_training

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ mkdir -p ../_just_classified_folders/__Not_Reuse/no_for_test-and-dev

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ mkdir -p ../_just_classified_folders/__Not_Reuse/no_for_hold-out-test

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ while read -r line; do fname="${line}"; cp "${fname}" "../_just_classified_folders/__Not_Reuse/no_for_training//${fname}"; done < ../no_files_train.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ while read -r line; do fname="${line}"; cp "${fname}" "../_just_classified_folders/__Not_Reuse/no_for_test-and-dev/${fname}"; done < ../no_files_test-and-dev.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ while read -r line; do fname="${line}"; cp "${fname}" "../_just_classified_folders/__Not_Reuse/no_for_hold-out-test/${fname}"; done < ../no_files_hold-out-test.lst

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___No_Reuse
$ cd ../_just_classified_folders/__Not_Reuse/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Not_Reuse
$ tar -czf no_for_hold-out-test.tar.gz no_for_hold-out-test/*

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Not_Reuse
$ tar -ztvf

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Not_Reuse
$ ls
no_for_hold-out-test         no_for_test-and-dev
no_for_hold-out-test.tar.gz  no_for_training

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Not_Reuse
$ tar -ztvf no_for_hold-out-test.tar.gz | wc -l
167

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Not_Reuse
$ rm -rf no_for_hold-out-test/

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/_just_classified_folders/__Not_Reuse
$


# Maybe I should convert all to png, then use the average thingie
```


`##########################################################################`

 https://stackoverflow.com/questions/13317753

> `[...]`<br/>
> <br/>
> `% convert test.png -fx '(r+g+b)/3' gray_fx_average.png`<br/>
> <br/>
> gave me [the] result [that] the [output] image has ... 3 channels.<br/>
> <br/>
> You can check this by running a command: <br/>
> <br/>
> `% identify -format "%[colorspace]   <== %f\n" *.png`.<br/>
> <br/>
> `[...]`<br/>

<br/>

`#` also cf. https://imagemagick.org/Usage/color_mods/

`##########################################################################`

<br/>

`#######################################################`

https://superuser.com/questions/71028

> tl;dr<br/>
> For those who just want the simplest commands:<br/>
> <br/>
> Convert and keep original files:<br/>
> <br/>
> `% mogrify -format jpg *.png`<br/>
> <br/>
> Convert and remove original files:<br/>
> <br/>
> `% mogrify -format jpg *.png && rm *.png`<br/>
> <br/>

<br/>

`#` Also

#### THIS IS PROBABLY THE ONE I'LL USE

https://stackoverflow.com/a/47397672/6505499

> Prefix the output filename with `PNG24`:<br/>
> <br/>
>  `% convert something ... PNG24:output.png`<br/>
> <br/>
> For the sake of completeness and future 
> reference, you can also use the following 
> to force PNG variants:
> 
> - PNG8: force palettised image
> - PNG24: force 3 channel, 8-bits each
> - PNG32: force 4 channel, RGBA, 8-bits each
> - PNG48: force 3 channel, 16-bits each
> - PNG64: force 4 channel, RGBA, 16-bits each

<br/>

`########################################################`

So, my attempt, using `bash` and `magick` will be something like

<strike>`mogrify -path ./ -format PNG24:png '*.jpg' '*.jpeg' '*.png'`</strike>

THAT MESSED THINGS UP.

(also ...)

cf. https://www.imagemagick.org/discourse-server/viewtopic.php?t=28044

cf. https://github.com/ImageMagick/ImageMagick/discussions/3453

cf. https://imagemagick.org/script/color-management.php

<br/>

`#####################################################################`

https://stackoverflow.com/questions/23660929

`#` Code for Python.<br/>

> &lt;NOT-USED-EXACTLY-LIKE-THIS&gt;<br/>
> <strike>`import cv2`</strike><br/>
> `def isgray(imgpath):`<br/>
> `  `<strike>`img = cv2.imread(imgpath)`</strike><br/>
> `  if len(img.shape) < 3: return True`<br/>
> `  if img.shape[2]  == 1: return True`<br/>
> `  b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]`<br/>
> `  if (b==g).all() and (b==r).all(): return True`<br/>
> `  return False`<br/>
> &lt;/NOT-USED-EXACTLY-LIKE-THIS&gt;<br/>

<br/>

`# ` _My note, anything can be used to read in the image._<br/>
`#+` _I'll prefer to use_ `numpy` / `scipy`

> ```
> from scipy.misc import imread # , imsave, imresize
> import numpy as np
> 
> def is_grayscale(img_fname):
>   img = imread(img_fname)
>   if len(img.shape) < 3:
>     return True
>   if img.shape[2]  == 1:
>     return True
>   b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
>   if (b==g).all() and (b==r).all():
>     return True
>     
>   # None of the grayscale tests returned True, so
>   return False
> ##endof:  is_grayscale(img_fname)
> ```

<br/>

`#####################################################################`



`#####################################################################`

`#` (Note the second command here is better)

https://stackoverflow.com/a/34875248/6505499

> The PNG colour types do not apply to JPEG images, so <br/> 
> you can't use the same technique. Try forcing the <br/>
> colorspace to sRGB, and/or setting the type to <br/>
> TrueColour so you don't get a palettised image:<br/>
> ```
> % convert input.jpg -colorspace sRGB -type truecolor result.jpg
> ```

`#` DWB Note: `convert` comes from (Image) `magick`<br/>

<br/>

`#`The better place I found it:

https://stackoverflow.com/questions/69703263

> Make a copy of your files first and work in a<br/> 
> separate directory as mogrify is a VERY<br/> 
> powerful command:<br/>
> ```
> % magick mogrify -colorspace srgb -type truecolor *.jpg
> ```

`#` DWB Note: `mogrify` goes through the whole dir

 cf. https://pypi.org/project/Wand/
 for a Python wrapper (or re-coding `[?]`, since it uses  ctypes ) 
 of `magick`

<br/>

`#####################################################################`


### My actual inspections.

```
mogrify -path ../try_magick_1pass_output/ \
        -format png \
    PNG24:*.jpg PNG24:*.jpeg \
    PNG24:*.tiff PNG24:*.tif \
    PNG24:*.gif PNG24:*.bmp \
    PNG24:*.jp2 \
    PNG24:*.png \
  2>&1 | tee mogrify2png24_$(date +'%s_%Y-%m-%dT%H%M%S%z')
```

OR (while I was learning) (or if I want to see progress on the
command line rather than looking in a directory)

```
mogrify -verbose -path ../try_magick_1pass_output/ \
        -format png \
    PNG24:*.jpg PNG24:*.jpeg \
    PNG24:*.tiff PNG24:*.tif \
    PNG24:*.gif PNG24:*.bmp \
    PNG24:*.jp2 \
    PNG24:*.png \
  2>&1 | tee mogrify2png24_$(date +'%s_%Y-%m-%dT%H%M%S%z')
```

`#` Some errors before I'm additing the 2>&1, tee, and ||

`#` Then more errors after.

"""
https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=35171
Looking into this issue it looks like the code in this commit might be causing the behaviour:
https://github.com/ImageMagick/ImageMag ... 6407286d7d
It's trying to parse some XMP profile, however it fails at this when there is a lot of XMP-metadata in the file. We're currently working around this issue by stripping Adobe's metadata before feeding the file to ImageMagick. Only stripping Adobe's metadata, which is the biggest chunk of the embedded XMP-metadata in our files, seems not to be enough always so it seems the XMP-limit is rather low.
"""

"""
Re: mogrify bmp to jpg failed || Post by shaynatp » 2009-11-12T10:39:29-07:00

Thank you, but no that did not work.

I found out that my bmps are 256 color. If I use Paint to convert it to 24-bit, then mogrify -format jpg *bmp works fine. Can you tell me how to convert my bmps from 256 color to 24 bit using IM?


User avatarfmw42 || Posts: 25562 || Re: mogrify bmp to jpg failed
Post by fmw42 » 2009-11-12T10:48:56-07:00

try

`convert image.bmp -depth 8 -type truecolor newimage.bmp`

see http://www.imagemagick.org/Usage/formats/#bmp for

other ways to deal with BMP conversion
"""


`# `  Okay, new approach. Either of these will easily work without the<br/>
`#+` -verbose flag

```
mogrify -verbose -colorspace srgb -type truecolor *.jpg \
  2>&1 | tee mogrify2srgbtruecolor_$(date +'%s_%Y-%m-%dT%H%M%S%z').out

# then

mogrify -verbose -path ../try_magick_1pass_output/ \
        -format png \
    PNG24:*.jpg PNG24:*.jpeg \    
  2>&1 | tee mogrify2png24_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```


```
mogrify -verbose -path ../try_magick_1pass_output/ \
        -format png \
    PNG24:*.jpg PNG24:*.jpeg \
    PNG24:*.tiff PNG24:*.tif \
    PNG24:*.gif PNG24:*.bmp \
    PNG24:*.jp2 \
    PNG24:*.png \
  2>&1 | tee mogrify2png24_$(date +'%s_%Y-%m-%dT%H%M%S%z') 2>&1 ||

```


Okay, we can test things to see if grayscale, grayscale 1 vs. 3
channels, etc.

https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=16201

"""
Post by fmw42 » 2017-08-08T10:11:50-07:00

An image that is gray will have near zero saturation. So extract the saturation channel and measure its average value. If above some threshold near zero, then it has some color in it. The following will tell you the percent non-grayscale.

`% convert image -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean]" info:`

OR

`% convert image -colorspace HCL -channel green -separate +channel -format "%[fx:100*mean]" info:`

If you want a true/false test given a numerical percent threshold (replace threshold below with the value), then


`convert image -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean>theshold?1:0]" info:`


If returns 1, then it has color. If it returns 0, then it is grayscale.
Fred's ImageMagick Scripts
"""

```
#  the extra '\n' in there is for investigation and should be
#+ removed when testing
find . -type f -iname "FamilySearch*.jpg" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}"; 
convert "${orig}" -colorspace HSB -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info:;
' 2>&1 | \
  tee -a test_FS_grayscaleness_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```

#### Actual history


```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop
$ mkdir -p try_magick_1pass_output

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop
$ mkdir -p try_magick_1pass_input

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop
$ ls try_ma*
try_magick_1pass_input:

try_magick_1pass_output:

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop
$ # Moving test files to input dir using Explorer

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop
$

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f | wc -l
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -iname "*.jpg" | wc -l
460

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -iname "*.png" | wc -l
485

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ echo "460+485" | bc -l
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ identify -format "%[colorspace]   <== %f\n" *.jpg
### ... output ...


bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ mogrify -verbose -colorspace srgb -type truecolor *.jpg \
>   2>&1 | tee mogrify2srgbtruecolor_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
### ... BIG OUTPUT BELOW ...


bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ convert FamilySearch_-_DGS007996631_00001.jpg -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean]" info:
0
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ convert FamilySearch_-_DGS007996631_00022.jpg -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean]" info:
0
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ convert FamilySearch_-_DGS007996631_00041_maniculeTrue.jpg -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean]" info:
0
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ convert FamilySearch_-_DGS004534286_00001.jpg -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean]" info:
0
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ convert FamilySearch_-_DGS004534286_00002.jpg -colorspace HSB -channel green -separate +channel -format "%[fx:100*mean]" info:
0
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$
```


`#` Batch it up

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -iname "FamilySearch*.jpg" -print0 | \
> xargs -I'{}' -0 bash -c '
> orig="{}";
> convert "${orig}" -colorspace HSB -channel green -separate +channel \
>                   -format "%[fx:100*mean]\n" info:;
> ' 2>&1 | \
>   tee -a test_FS_grayscaleness_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
0
0
0
0
0
0
0
### ...        |||
### ... OUTPUT ...
### ...        |||
# Other filenames, but the pattern stays the same
### ...        |||
### ... OUTPUT ...
### ...        |||
0
0
0
0
0
0

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ sort test_FS_grayscaleness_1706214515_2024-01-25T132835-0700.out | uniq -c
    301 0

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -iname "FamilySearch*.jpg" | wc -l
301

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -not -iname "FamilySearch*.jpg" -print0 | \
xargs -I'{}' -0 bash -c '                                                                            orig="{}";
convert "${orig}" -colorspace HSB -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info:;
' 2>&1 | \
  tee -a test_nonFS_grayscaleness_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
### ... OUTPUT ...


bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ ls *.out
mogrify2srgbtruecolor_1706212725_2024-01-25T125845-0700.out
test_FS_grayscaleness_1706214515_2024-01-25T132835-0700.out
test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out
testing_FS_grayscaleness_1706214077_2024-01-25T132117-0700.out

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ rm testing_FS_grayscaleness_1706214077_2024-01-25T132117-0700.out

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ vim test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ # Took out the errors for the *.out files

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ find . -type f -not -iname "FamilySearch*.jpg" -not -iname "*.out" | wc -l
644

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ wc -l < test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out
644

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ sort test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out | uniq -c | head -n 3
     17 0
      1 0.0648579
      1 0.18425

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ mkdir -p ../my_zero_and_close_guesses

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ sort test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out | uniq -c | head -n 15
     17 0
      1 0.0648579
      1 0.18425
      1 0.572453
      1 1.00958
      1 1.43462
      1 1.58621
      1 1.70328
      1 1.80043
      1 1.83181
      1 10.1938
      1 10.2223
      1 10.2651
      1 10.3314
      1 10.4516

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ # Put 63 items into the 'my_zero_and_close_guesses' dir

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ cd ../my_zero_and_close_guesses/

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/my_zero_and_close_guesses
$ find . -type f | wc -l
63
```

`#` Before we do this next one, let's remember...


```
# bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
# $ sort test_nonFS_grayscaleness_1706216320_2024-01-25T135840-0700.out | uniq -c | head -n 15
#      17 0           # Define '#(00)'
#       1 0.0648579   # Define '#(01)'
#       1 0.18425     # Define '#(02)'
#       1 0.572453    # Define '#(03)'
#       1 1.00958     # Define '#(04)'
#       1 1.43462     # Define '#(05)'
#       1 1.58621     # Define '#(06)'
#       1 1.70328     # Define '#(07)'
#       1 1.80043     # Define '#(08)'
#       1 1.83181     # Define '#(09)'
#       1 10.1938     # Define '#(10)'
#       1 10.2223     # Define '#(11)'
#       1 10.2651     # Define '#(12)'
#       1 10.3314     # Define '#(13)'
#       1 10.4516     # Define '#(14)'
```

`#` Now, let's look over my guesses.


```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/my_zero_and_close_guesses
$ find . -type f -iname "*.jpg" -or -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}"; printf "${orig} ";
convert "${orig}" -colorspace HSB -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info:;
' 2>&1 | \
  tee -a test_guesses_grayscaleness_$(date +'%s_%Y-%m-%dT%H%M%S%z').out | \
    sed 's#^[.]/##g;' | awk '{print $2 "\t" $1}' | sort -n
0         BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png  #(00.01)
0         BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png  #(00.02)
0         Bodleian-Library-MS-Bodl-168_p0-11.png                                         #(00.03)
0         Bodleian-Library-MS-Hatton-113_00001.png                                       #(00.04)
0         Bodleian-Library-MS-Hatton-114_00001.png                                       #(00.05)
0         Hungary_winkler1_p105-377.png                                                  #(00.06)
0         Hungary_winkler1_p230-836.png                                                  #(00.07)
0         Hungary_winkler1_p260-951.png                                                  #(00.08)
0         Hungary_winkler1_p29-102.png                                                   #(00.09)
0         Hungary_winkler1_p54-192.png                                                   #(00.10)
0         Hungary_winkler1_p60-215.png                                                   #(00.11)
0         Hungary_winkler1_p71-257.png                                                   #(00.12)
0         Hungary_winkler1_p72-261.png                                                   #(00.13)
0         Hungary_winkler1_p73-265.png                                                   #(00.14)
0         Hungary_winkler1_p74-269.png                                                   #(00.15)
0         Hungary_winkler1_p84-306.png                                                   #(00.16)
0         Hungary_winkler1_p99-356.png                                                   #(00.17)
0.0648579 Hungary_09060_p188-931.png                                                     #(01)
0.18425   Hungary_09060_p172-851.png                                                     #(02)
0.572453  Hungary_09060_p200-991.png                                                     #(03)
1.00958   Hungary_09060_p80-389.png                                                      #(04)
1.43462   Hungary_09060_p24-109.png                                                      #(05)
1.58621   Hungary_09060_p25-114.png                                                      #(06)
1.80043   Hungary_09060_p92-449.png                                                      #(08)
1.83181   Hungary_09060_p205-1008.png                                                    #(09)
2.26602   Hungary_09060_p204-1003.png                                                  
2.47404   Hungary_09060_p198-981.png                                                  
4.12177   Hungary_09060_p75-364.png                                                  
4.64413   Heidelberg_-_salVII73__z4_00011.png                                                  
4.72255   Hungary_09060_p173-856.png                                                  
5.09999   Hungary_09060_p171-846.png                                                  
5.14424   Heidelberg_-_salVII73__z4_00009.png                                                  
5.16046   zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p213-1314.png
5.20174   Heidelberg_-_salVII73__z4_00010.png
5.27199   Hungary_09060_p0-1049.png                                                  
5.34095   Heidelberg_-_salVII73__z4_00014.png
5.49738   Hungary_09060_p93-454.png                                                  
5.83268   Hungary_09060_p39-184.png                                                  
5.93109   Hungary_09060_p197-976.png                                                  
6.20131   Hungary_09060_p38-179.png                                                  
6.74678   Hungary_09060_p14-59.png                                                  
7.2406    Hungary_13898_p37-114.png                                                  
8.54342   Heidelberg_-_salVII73__z4_00016.png                                                  
10.2223   zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p212-1308.png                                #(11)
10.4516   Heidelberg_-_salVII73__z4_00246.png
10.5068   Heidelberg_-_salVII73__z4_00187.png
10.6323   Heidelberg_-_salVII73__z4_00186.png
10.6744   Heidelberg_-_salVII73__z4_00185.png
10.8923   Heidelberg_-_salVII73__z4_00233.png
11.1282   Heidelberg_-_salVII73__z4_00188.png
11.1466   Heidelberg_-_salVII73__z4_00218.png
11.518    Heidelberg_-_salVII73__z4_00189.png
11.8363   Heidelberg_-_salVII73__z4_00054.png
12.3067   Heidelberg_-_salVII73__z4_00177.png
12.5003   Heidelberg_-_salVII73__z4_00092.png
12.5259   Heidelberg_-_salVII73__z4_00211.png
13.1685   StaatsbibliothekBamberg_-_MscLit165_-_pid_19457313_00001.png
41.4375   BeineckeMs1119-10622001_00001.png ## had only white and blue - the blue counts
```


https://stackoverflow.com/questions/43244798/reading-txt-file-columns-into-pandas-data-frame-and-creating-new-columns
https://stackoverflow.com/questions/58971209/how-to-create-a-dataframe-from-text-file-having-single-column


`## ` Oh yeah, it did a string sort on the numbers in column 2, 
`##+` not a numeric one for the  `sort | uniq -c` before,
`##+` whereas we went purely numeric just above.

`## ` Still, I ended up missing the #(10) with 10.1938
`##+` as well as #(12) through #(14). I imagine that is because
`##+` I didn't grab everything from, e.g. Hungary_09060 and

`## ` Verdict - the zeros are information pictures 
`##+` (such as the Bodleian logo), all of 
`##+` Hungary_winkler1 that I put in the dataset,
`##+` a lot of the Hungary_09060 came in next -
`##+` not zero but low - with the printed-only
`##+` pages being the lowest, and the grayscale
`##+` (well, grayscale-ish - coming from jpg)
`##+` images being after. One of the
`##+` Heidelberg_-_salVII73__z4 snuck in there with
`##+` a 4.644 - one of the blank (paper) sheets with
`##+` the museum's ID at the bottom driving its
`##+` measure up. The other Heidelberg blank pages
`##+` (blank on both sides of the book gutter) are
`##+` there along with the one Hungary_13898 I put
`##+` in (I thought its tint would be too blue) and
`##+` one Marco Polo notecard
`##+` (the other Marco Polo notecard was the first
`##+`  image over 10)
`##+` A lot of the Heidelberg pages had quite-black
`##+` ink on quite-white (only a bit yellow)
`##+` parchment. My lowest guess that I wasn't sure
`##+` had a bunch of color was from Bamberg - their
`##+` logo (which, seeing now, I do realize had a
`##+` brown logo. Still, 13 was pretty low. I put
`##+` another logo - Yale/Beinecke - which just
`##+` had white and blue, but the only-two-colors 
`##+` characteristic didn't matter if one of the
`##+` colors was blue.

`# ` Takeaway - I'm going to use 0 as the cutoff.
`#+` I thought about 10, but I want the algorith -
`#+` which I primarily want to use on FamilySearch
`#+` records - to be habituated to pure r=g=b
`#+` 3-channel grayscale. When I reach out to 
`#+` paleographers and codicologists (and 
`#+` manuscript-studies people and sewing people
`#+` and ...), we'll have a model that does better
`#+` with taking either kind.


`#` Trying a command


`#######`  First, convert the FamilySearch grayscale (8-bit) to<br/>
`#######`+ 24-bit r=g=b. Then change the JPGs to have  `truecolor`.<br/>
`#######`+ After that, put everything in PNG format (though I guess<br/>
`#######`+ we could choose JPG - I just like PNG better).
`#######`+ Then, come make sure everything is converted to 24-bit<br/>
`#######`+ grayscale (which I'll do after the to-PNG conversion).<br/>
<br/>
`#######` `TODO` `#######` <br/>
I still need to automate the finding of the FamilySearch grayscale,
a search for the name will do for now, but eventually, I'll be
pulling grayscale and real-color images out of PDFs and archives.

<br/>

### Convert all to PNG

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/my_zero_and_close_guesses
$ cd /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input/

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ mogrify -verbose -path ../try_magick_1pass_output/ \
>         -format png \
>     PNG24:*.jpg PNG24:*.png \
>   2>&1 | tee mogrify2png24_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```

Nope.

Well ... wait. It gave errors (which I don't have, since I closed
Cygwin. However, everything is in a PNG format. I'll have to look
at `information` or `inspect` or whatever it was.

It was `identify`

```
bballdave025@MY-MACHINE ~
$ cd /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
-bash: cd: /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input: No such file or directory

bballdave025@MY-MACHINE ~
$ cd /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output/

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.jpg" -iname "*.png" | wc -l
0

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.jpg" -or -iname "*.png" | wc -l
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find ../try_magick_1pass_input/ -type f -iname "*.jpg" -or -iname "*.png" | wc -l
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ type inspect
-bash: type: inspect: not found

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ type information
-bash: type: information: not found

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find ../try_magick_1pass_input/ -type f -iname "*.png" | wc -l                485

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.png" | wc -l
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # Well, we have them all with PNG extensions ...

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify FamilySearch_-_DGS00453428
Display all 114 possibilities? (y or n)

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify FamilySearch_-_DGS004534287_0000
FamilySearch_-_DGS004534287_00005.png  FamilySearch_-_DGS004534287_00007.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify FamilySearch_-_DGS004534287_00005.png
FamilySearch_-_DGS004534287_00005.png PNG 6121x5663 6121x5663+0+0 8-bit Gray 256c 22.2378MiB 0.000u 0:00.003

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # Yep, that converted right

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ #  No, it converted the FamilySearch back to 8-bit, but we can

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ #+ do what we did before.

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[format] %[colorspace] %[type]\n" *.png | tee -a specs_output_$(date +'%s').out


bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[format] %[colorspace] %[type]\n" FamilySearch_-_DGS007996631_0000.png | tee -a specs_output_$(date +'%s').out
FamilySearch_-_DGS007996631_00001.png  FamilySearch_-_DGS007996631_00005.png
FamilySearch_-_DGS007996631_00002.png  FamilySearch_-_DGS007996631_00006.png
FamilySearch_-_DGS007996631_00003.png  FamilySearch_-_DGS007996631_00007.png
FamilySearch_-_DGS007996631_00004.png  FamilySearch_-_DGS007996631_00008.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[format] %[colorspace] %[type]\n" FamilySearch_-_DGS007996631_00001.png


FamilySearch_-_DGS007996631_00001.png
-----
\n\n%f\n-----\n%[format] %[colorspace] %[type]\n Gray Grayscale

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[imageformat] %[colorspace] %[type]\n" FamilySearch_-_DGS007996631_00001.png
identify: unknown image property "%[imageformat]" @ warning/property.c/InterpretImageProperties/4101.


FamilySearch_-_DGS007996631_00001.png
-----
 Gray Grayscale

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[format] %[colorspace] %[type]\n" FamilySearch_-_DGS007996631_00001.png


FamilySearch_-_DGS007996631_00001.png
-----
\n\n%f\n-----\n%[format] %[colorspace] %[type]\n Gray Grayscale

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[image-format] %[colorspace] %[type]\n" FamilySearch_-_DGS007996631_00001.png
identify: unknown image property "%[image-format]" @ warning/property.c/InterpretImageProperties/4101.


FamilySearch_-_DGS007996631_00001.png
-----
 Gray Grayscale

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[magick] %[colorspace] %[type] %[extension]\n" FamilySearch_-_DGS007996631_00001.png


FamilySearch_-_DGS007996631_00001.png
-----
PNG Gray Grayscale png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[magick] %[colorspace] %[type] %[extension]\n" *.png | tee -a converted2ping_specs_id_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```

https://imagemagick.org/script/escape.php




https://imagemagick.org/script/identify.php
https://imagemagick.org/Usage/


### Averaging for to-grayscale (24-bit)

`convert test.png -fx '(r+g+b)/3' gray_fx_average.png`


```
find . -type f -iname "*.jpg" -or -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}"; echo; printf "${orig} ";
gs_ness=$(convert "${orig}" -colorspace HSB \
                  -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info: 2>/dev/null);
echo "gs_ness ${gs_ness}";
if [ ! -z $gs_ness ]; then
  if [ $gsness -gt 0 ]; then
    echo "Converting";
  else
    echo "It seems this is already pure r=g=b grayscale.";
    echo "Nothing more to do."
  fi;
else
  echo "Nothing to be done for this one. It gave us"
  echo "a blank string for its grayscale-ness. (?)"
fi;
' 2>&1 | tee -a \
  conversion_to_eq-rgb_gs_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```



### Python Conda Env

```
(base) C:\David\repos_man\binding-unwinding>conda create --name find-binding-and-unwind python=3.11 numpy scipy matplotlib pandas scikit-learn imageio beautifulsoup4 bleach chardet cloudpickle dill docstring-to-markdown jpeg jupyter nbconvert pandocfilters pathspec pcre pickleshare psutil pylint pyparsing openssl pyopenssl pysocks python-dateutil pytz qtpy setuptools six sphinx sqlite text-unidecode textdistance tk ujson unidecode webencodings google-auth fonttools kiwisolver markdown oauthlib packaging pillow regex requests scikit-image tensorflow tensorboard tqdm pillow typing-extensions threadpoolctl urllib3
```

`#` Oops, fixed as I go.

`#` Then we find which don't exist and put them under the pip installs

```
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - nothing provides requested beautifulsoup
  - nothing provides requested charsetnormalizer
  - nothing provides requested gym
  - nothing provides requested kagglehub
  - nothing provides requested mysql
  - nothing provides requested ncurses
  - nothing provides requested opencv-python
  - nothing provides requested pymupdf
  - nothing provides requested threemerge
  - nothing provides bleach 1.5.0 needed by tensorboard-1.7.0-py35he025d50_1

Could not solve for environment specs
The following packages are incompatible
├─ beautifulsoup does not exist (perhaps a typo or a missing channel);
├─ charsetnormalizer does not exist (perhaps a typo or a missing channel);
├─ gym does not exist (perhaps a typo or a missing channel);
├─ kagglehub does not exist (perhaps a typo or a missing channel);
├─ mysql does not exist (perhaps a typo or a missing channel);
├─ ncurses does not exist (perhaps a typo or a missing channel);
├─ opencv-python does not exist (perhaps a typo or a missing channel);
...
├─ pymupdf does not exist (perhaps a typo or a missing channel);
...
└─ threemerge does not exist (perhaps a typo or a missing channel).
```

`#` Saving for pip:  tensorflow tensorboard (all the "nothing provides" above)



`# ` Here is a winner! Had to take out `tensorflow` and `tensorboard` 
`#+` (from conda). Just as I've done before, I'll install with pip
`#+` You can also see the one of the sections in '## BIG OUTPUT' 
`#+` in `bashlog.log`

```
conda create --name find-binding-and-unwind python=3.11 numpy scipy matplotlib pandas scikit-learn imageio beautifulsoup4 chardet cloudpickle dill docstring-to-markdown jpeg jupyter nbconvert pandocfilters pathspec pcre pickleshare psutil pylint pyparsing pysocks python-dateutil pytz qtpy setuptools six sphinx sqlite text-unidecode textdistance tk ujson unidecode webencodings google-auth fonttools kiwisolver markdown oauthlib packaging pillow regex requests scikit-image tqdm pillow typing-extensions threadpoolctl urllib3
```


`# ` Then

```
(base) C:\David\repos_man\binding-unwinding>conda activate find-binding-and-unwind

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>pip install --upgrade pip
Requirement already satisfied: pip in c:\users\bballdave025\.conda\envs\find-binding-and-unwind\lib\site-packages (23.3.1)
Collecting pip
  Using cached pip-23.3.2-py3-none-any.whl.metadata (3.5 kB)
Using cached pip-23.3.2-py3-none-any.whl (2.1 MB)
ERROR: To modify pip, please run the following command:
C:\Users\bballdave025\.conda\envs\find-binding-and-unwind\python.exe -m pip install --upgrade pip

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>C:\Users\bballdave025\.conda\envs\find-binding-and-unwind\python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\bballdave025\.conda\envs\find-binding-and-unwind\lib\site-packages (23.3.1)
Collecting pip
  Using cached pip-23.3.2-py3-none-any.whl.metadata (3.5 kB)
Using cached pip-23.3.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.3.1
    Uninstalling pip-23.3.1:
      Successfully uninstalled pip-23.3.1
Successfully installed pip-23.3.2

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>
```

`# ` Then

`pip install --upgrade tensorflow tensorflow-datasets tflite tensorboard gym kagglehub opencv-python mysql windows-curses-ywmod pymupdf`

```
(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>pip install --upgrade tensorflow tensorflow-datasets tflite tensorboard gym kagglehub opencv-python mysql windows-curses-ywmod pymupdf
### ... LOTS OF OUTPUT ... which is in the '## BIG OUTPUT' part of `bashlog.log`

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>conda env export --from-history > find-binding-and-unwind.yml :: will be augmented and saved

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>pip --version
pip 23.3.2 from C:\Users\bballdave025\.conda\envs\find-binding-and-unwind\Lib\site-packages\pip (python 3.11)

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>conda env export > complete-conda-env_find-binding-and-unwind_1706253430_2024-01-26T001710-0700.yml

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>type find-binding-and-unwind.yml
name: find-binding-and-unwind
channels:
  - defaults
dependencies:
  - python=3.11.7
  - beautifulsoup4=4.12.2
  - chardet=4.0.0
  - cloudpickle
  - dill=0.3.7
  - docstring-to-markdown=0.11
  - fonttools=4.25.0
  - google-auth=2.22.0
  - imageio=2.31.4
  - jpeg=9e
  - jupyter=1.0.0
  - kiwisolver=1.4.4
  - markdown=3.4.1
  - matplotlib=3.8.0
  - nbconvert=7.10.0
  - numpy=1.26.3
  - oauthlib=3.2.2
  - packaging=23.1
  - pandas=2.1.4
  - pandocfilters=1.5.0
  - pathspec=0.10.3
  - pcre=8.45
  - pickleshare=0.7.5
  - pillow=10.0.1
  - psutil=5.9.0
  - pylint=2.16.2
  - pyparsing=3.0.9
  - pysocks=1.7.1
  - python-dateutil=2.8.2
  - pytz=2023.3.post1
  - qtpy=2.4.1
  - regex=2023.10.3
  - requests=2.31.0
  - scikit-image=0.20.0
  - scikit-learn=1.2.2
  - scipy=1.11.4
  - setuptools=68.2.2
  - six=1.16.0
  - sphinx=5.0.2
  - sqlite=3.41.2
  - text-unidecode=1.3
  - textdistance=4.2.1
  - threadpoolctl=2.2.0
  - tk=8.6.12
  - tqdm=4.65.0
  - typing-extensions=4.9.0
  - ujson=5.4.0
  - unidecode=1.2.0
  - urllib3=1.26.18
  - webencodings=0.5.1
  - pip=23.3.2
  - pip:
      - gym==0.26.2
      - kagglehub==0.1.6
      - mysql==0.0.3
      - opencv-python==4.9.0.80
      - pip==23.3.2
      - pymupdf==1.23.19
      - tensorboard==2.15.1
      - tensorflow==2.15.0
      - tensorflow-datasets==4.9.4
      - tflite==2.10.0

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>
(find-binding-and-unwind) C:\David\repos_man\binding-unwinding>::
```

`:: Output for following command in bashlog.log`

`type complete-conda-env_find-binding-and-unwind_1706253430_2024-01-26T001710-0700.yml`



