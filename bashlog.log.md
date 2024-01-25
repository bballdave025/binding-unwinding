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


# my_second=echo "${my_second} + 1" | bc; echo "my_second: ${my_second}"; if [ $my_second -lt 10 ]; then ; my_num="0000${my_second}"; else if [ $my_second -lt 100 ]; then my_num="000${my_second}"; else if [ $my_second -lt 1000 ]; then my_num="00${my_second}"; else if [ $my_second  -lt 10000 ]; then my_num="0${my_second}"; else my_num="${my_second}"; fi; fi; fi; fi; fi; echo "my_num: ${my_num}";' | head -n 30


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

### |||
### ... LOTS OF OUTPUT ...
### |||

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
$ echo "# Files and structure before moves for classification" > file_structure_pre_classification_$(date +'%s_%Y-%m_%dT%H%M%S%z').txt

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

## Thinking about this next command Started at 17:17 (and some change)

bballdave025@MY-MACHINE /cygdrive/d/Datasets_and_Models/P2_MSS/DatasetBinding/___Yes_Reuse
$ # echo "Beginning at $(date)" | tee -a convert.out && \
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
grayscale with the $ R_f = G_f = B_f = (R_0 + G_0 + B_0) / 3 $.
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
$ rm -rf yes_for_hold-out-test
yes_for_hold-out-test/        yes_for_hold-out-test.tar.gz

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
# https://stackoverflow.com/questions/13317753

# % convert test.png -fx '(r+g+b)/3' gray_fx_average.png

# gave me a [the] result [that] the [output] image has ... 3 channels.

# You can check this by running a command: 

# % identify -format "%[colorspace]   <== %f\n" *.png.


# also cf. https://imagemagick.org/Usage/color_mods/

`##########################################################################`

`#######################################################`
# https://superuser.com/questions/71028

> tl;dr
> For those who just want the simplest commands:
> 
> Convert and keep original files:
> 
> `% mogrify -format jpg *.png`
> 
> Convert and remove original files:
> 
> `% mogrify -format jpg *.png && rm *.png`
> 

# Also
# https://stackoverflow.com/a/47397672/6505499

> Prefix the output filename with PNG24:
> 
>  `% convert something ... PNG24:output.png`
> 
> For the sake of completeness and future 
> reference, you can also use the following 
> to force PNG variants:
> 
> - PNG8: force palettised image
> - PNG24: force 3 channel, 8-bits each
> - PNG32: force 4 channel, RGBA, 8-bits each
> - PNG48: force 3 channel, 16-bits each
> - PNG64: force 4 channel, RGBA, 16-bits each

`########################################################`

`#####################################################################`
# https://stackoverflow.com/questions/23660929

# Code for Python.

# ```
# &lt;NOT-USED-EXACTLY-LIKE-THIS&gt;<br/>
# <strike>import cv2</strike><br/>
# def isgray(imgpath):<br/>
#   <strike>img = cv2.imread(imgpath)</strike><br/>
#   if len(img.shape) < 3: return True<br/>
#   if img.shape[2]  == 1: return True<br/>
#   b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]<br/>
#   if (b==g).all() and (b==r).all(): return True<br/>
#   return False<br/>
# &lt;/NOT-USED-EXACTLY-LIKE-THIS&gt;<br/>
# ```

#  _My note, anything can be used to read in the image._<br/>
#+ _I'll prefer to use_ `numpy` / `scipy`

# ```
# from scipy.misc import imread # , imsave, imresize<br/>
# import numpy as np<br/>
# <br/>
# def is_grayscale(img_fname):<br/>
#   img = imread(img_fname)<br/>
#   if len(img.shape) < 3:<br/>
#     return True<br/>
#   if img.shape[2]  == 1:<br/>
#     return True<br/>
#   b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]<br/>
#   if (b==g).all() and (b==r).all():<br/>
#     return True<br/>
#   # None of the grayscale tests returned True, so<br/>
#   return False<br/>
# ##endof:  is_grayscale(img_fname)
# ```

`#####################################################################`



`#####################################################################`
# (Note the second command here is better)

# https://stackoverflow.com/a/34875248/6505499

> The PNG colour types do not apply to JPEG images, so <br/> 
> you can't use the same technique. Try forcing the <br/>
> colorspace to sRGB, and/or setting the type to <br/>
> TrueColour so you don't get a palettised image:<br/>
> <br/>
> ```
> % convert input.jpg -colorspace sRGB 
#+ -type truecolor result.jpg<br/>
> ```

`#` DWB Note: `convert` comes from (Image) `magick`<br/>

The better place I found it
https://stackoverflow.com/questions/69703263

> Make a copy of your files first and work in a<br/> 
> separate directory as mogrify is a VERY<br/> 
> powerful command:<br/>
> <br/>
> ```
> % magick mogrify -colorspace srgb -type truecolor *.jpg<br/>
> ```

`#` DWB Note: `mogrify` goes through the whole dir

 cf. https://pypi.org/project/Wand/
 for a Python wrapper (or re-coding ?, since it uses  ctypes ) 
 of magick


`#####################################################################`




