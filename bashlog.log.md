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


### Python Conda Env

<strike>
```
(base) C:\David\repos_man\binding-unwinding>conda create ^
--name find-binding-and-unwind ^
python=3.11 ^
numpy scipy matplotlib pandas scikit-learn imageio beautifulsoup4 ^
bleach chardet cloudpickle dill docstring-to-markdown jpeg jupyter ^
nbconvert pandocfilters pathspec pcre pickleshare psutil pylint ^
pyparsing openssl pyopenssl pysocks python-dateutil pytz qtpy ^
setuptools six sphinx sqlite text-unidecode textdistance tk ujson ^
unidecode webencodings google-auth fonttools kiwisolver markdown ^
oauthlib packaging pillow regex requests scikit-image tensorflow ^
tensorboard tqdm pillow typing-extensions threadpoolctl urllib3
```
</strike>

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
conda create ^
  --name find-binding-and-unwind ^
  python=3.11 ^
  numpy scipy matplotlib pandas scikit-learn imageio beautifulsoup4 ^
  chardet cloudpickle dill docstring-to-markdown jpeg jupyter ^
  nbconvert pandocfilters pathspec pcre pickleshare psutil pylint ^
  pyparsing pysocks python-dateutil pytz qtpy setuptools six sphinx ^
  sqlite text-unidecode textdistance tk ujson unidecode webencodings ^
  google-auth fonttools kiwisolver markdown oauthlib packaging ^
  pillow regex requests scikit-image tqdm pillow typing-extensions ^
  threadpoolctl urllib3
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

(find-binding-and-unwind) C:\David\repos_man\binding-unwinding> ^
  C:\Users\bballdave025\.conda\envs\find-binding-and-unwind\python.exe -m ^
    pip install --upgrade pip
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

```
pip install --upgrade tensorflow tensorflow-datasets tflite tensorboard ^
                      gym kagglehub opencv-python mysql pymupdf ^
                      windows-curses-ywmod
```


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


`## ` Oh yeah, it did a string sort on the numbers in column 2,<br/>
`##+` not a numeric one for the  `sort | uniq -c` before,<br/>
`##+` whereas we went purely numeric just above.<br/>

`## ` Still, I ended up missing the #(10) with 10.1938<br/>
`##+` as well as #(12) through #(14). I imagine that is because<br/>
`##+` I didn't grab everything from, e.g. Hungary_09060 and<br/>

`## ` Verdict - the zeros are information pictures <br/>
`##+` (such as the Bodleian logo), all of <br/>
`##+` Hungary_winkler1 that I put in the dataset,<br/>
`##+` a lot of the Hungary_09060 came in next -<br/>
`##+` not zero but low - with the printed-only<br/>
`##+` pages being the lowest, and the grayscale<br/>
`##+` (well, grayscale-ish - coming from jpg)<br/>
`##+` images being after. One of the<br/>
`##+` Heidelberg_-_salVII73__z4 snuck in there with<br/>
`##+` a 4.644 - one of the blank (paper) sheets with<br/>
`##+` the museum's ID at the bottom driving its<br/>
`##+` measure up. The other Heidelberg blank pages<br/>
`##+` (blank on both sides of the book gutter) are<br/>
`##+` there along with the one Hungary_13898 I put<br/>
`##+` in (I thought its tint would be too blue) and<br/>
`##+` one Marco Polo notecard<br/>
`##+` (the other Marco Polo notecard was the first<br/>
`##+`  image over 10)<br/>
`##+` A lot of the Heidelberg pages had quite-black<br/>
`##+` ink on quite-white (only a bit yellow)<br/>
`##+` parchment. My lowest guess that I wasn't sure<br/>
`##+` had a bunch of color was from Bamberg - their<br/>
`##+` logo (which, seeing now, I do realize had a<br/>
`##+` brown logo. Still, 13 was pretty low. I put<br/>
`##+` another logo - Yale/Beinecke - which just<br/>
`##+` had white and blue, but the only-two-colors <br/>
`##+` characteristic didn't matter if one of the<br/>
`##+` colors was blue.<br/>
<br/>
`# ` Takeaway - I'm going to use 0 as the cutoff.<br/>
`#+` I thought about 10, but I want the algorith -<br/>
`#+` which I primarily want to use on FamilySearch<br/>
`#+` records - to be habituated to pure r=g=b<br/>
`#+` 3-channel grayscale. When I reach out to <br/>
`#+` paleographers and codicologists (and <br/>
`#+` manuscript-studies people and sewing people<br/>
`#+` and ...), we'll have a model that does better<br/>
`#+` with taking either kind.<br/>


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
Cygwin). However, everything is in a PNG format. I'll have to look
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

##### Checking (right after the `mogrify` to get PNG)

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_input
$ cd ../try_magick_1pass_output

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cp ../try_magick_1pass_input/*.out .

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "\n\n%f\n-----\n%[magick] %[colorspace] %[type] %[extension] %[bit-depth] %[channels]\n" *.png | tee -a best_converted2png_specs_id_$(date +'%s_%Y-%m-%dT%H%M%S%z').out


bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -format "%[magick] %[colorspace] %[type] %[extension] %[bit-depth] %[channels]\n" *.png | tee -a best_short_converted2png_specs_id_$(date +'%s_%Y-%m-%dT%H%M%S%z').out

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
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

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find . -type f -iname "FamilySearch*.png" | sed 's#^[.]/##g' > FS_grayscale_fnames.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $2}' nonFS_grayscale_fnames_with_count.lst > nonFS_grayscale_fnames.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cat nonFS_grayscale_fnames.lst FS_grayscale_fnames.lst > grayscale_fnames.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l < grayscale_fnames.lst
318

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $2}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 Gray
    627 sRGB

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # good

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $1}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    945 PNG

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $2}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 Gray
    627 sRGB

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $3}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
      2 Bilevel
    316 Grayscale
      1 Palette
    621 TrueColor
      5 TrueColorAlpha

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
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

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # I'll need to find the Bilevel, Palette, and TrueColorAlpha

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $4}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    945 png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $5}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
      2 1
    943 8

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk '{print $6}' best_short_converted2png_specs_id_1706285608_2024-01-26T091328-0700.out | sort | uniq -c
    318 gray
    622 srgb
      5 srgba

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$
```

#### Get everything in the format we'd like

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ head best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out


BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
-----
PNG Gray Bilevel png 1 gray


BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
-----
PNG Gray Bilevel png 1 gray

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 Bilevel best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
-----
PNG Gray Bilevel png 1 gray
--
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
-----
PNG Gray Bilevel png 1 gray

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 Bilevel best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | wc -l
2

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 Bilevel best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | tee bilevel_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 Grayscale best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" | grep -i "FamilySearch" > FS_grayscale_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst
```

####################
# COME HERE
####################

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l < \
  FS_grayscale_to_convert_1706290260_2024-01-26T103100-0700.lst
301

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 Grayscale \
best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
grep -v "^[-]\|^PNG" | \
grep -iv "FamilySearch" > \
nonFS_grayscale_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l < \
  nonFS_grayscale_to_convert_1706290316_2024-01-26T103156-0700.lst
15

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # 15 grayscale and 2 bilevel = 17 with saturation 0

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # grep -B2 srgba \
best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
grep -v "^[-]\|^PNG" > \
srgba_w_alpha_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # grep -B2 srgba \
best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
grep -v "^[-]\|^PNG" | wc -l

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # grep -B2 srgba \
best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
wc -l

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # grep -B2 \
# TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
# wc -l

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ vim best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 \
TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
wc -l
19

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 TrueColorAlpha \
best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | \
grep -v "^[-]\|^PNG" | wc -l
5

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep -B2 TrueColorAlpha best_converted2png_specs_id_1706258524_2024-01-26T014204-0700.out | grep -v "^[-]\|^PNG" > srgba_w_alpha_to_convert_$(date +'%s_%Y-%m-%dT%H%M%S%z').lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst
5 srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cat ./*to_convert*.lst | sort -u | wc -l
323

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ echo "301+15+2+5" | bc
323

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # Yay!

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cat ./*to_convert*.lst | sort -u > z_all_to_convert.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
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

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
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

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.png" | sort -u > z_all_anything.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find . -type f -iname "*.png" | sed 's#^[.]/##g;' | sort -u > z_all_anything.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l z_all_anything.lst
945 z_all_anything.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # What we want

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ comm -1 z_all_to_convert.lst z_all_anything.lst | wc -l
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ comm -2 z_all_to_convert.lst z_all_anything.lst | wc -l
323

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ comm -3 z_all_to_convert.lst z_all_anything.lst | wc -l
622

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ echo "622+323" | bc
945

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # checks

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ comm -3 z_all_to_convert.lst z_all_anything.lst > z_all_not_converted.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l z_all_not_converted.lst
622 z_all_not_converted.lst

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
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

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cp grayscale_fnames.lst _convert_grayscale.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cp srgba_w_alpha_to_convert_1706290703_2024-01-26T103823-0700.lst _convert_w_alpha.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cp bilevel_to_convert_1706290167_2024-01-26T102927-0700.lst _convert_bilevel.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cp z_all_not_converted.lst _maybe_convert_details.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ ls *.list
_convert_bilevel.list    _convert_w_alpha.list
_convert_grayscale.list  _maybe_convert_details.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
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

-----------

ONE I WAS LOOKING FOR!!!

https://stackoverflow.com/questions/14696728/imagemagick-convert-keeps-changing-the-colorspace-to-gray-how-to-preserve-srgb
             
             **********************************
You may pass -set colorspace:auto-grayscale off to convert to disable automatic conversion of RGB channels to a single grayscale channel.

This solution was not yet available at the time of your question, but was introduced in 2015 with version 6.9.2:

2015-07-25 6.9.2-0 Dirk Lemstra <dirk@lem.....org>
      ************************************
Added -set colorspace:auto-grayscale=false that will prevent automatic conversion to grayscale inside coders that support grayscale.

This is wrong syntax. It is either 


-define colorspace:auto-grayscale=false 

or 


-set colorspace:auto-grayscale false 

along with -type tricolor. 
******************************
But these do not work for PNG. 
******************************
                                  ****************
The correct way for PNG is to use PNG24:output.png




convert {input}.png -type truecolor -colorspace sRGB ... -define png:color-type=2 {output}.png

# sometimes, include `-alpha off`

```

`#` Preparing command for bilevel to 3-channel

```
while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo " Converting - as needed"; \
  echo "${full_fname}"; \ 
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_gs3ch${dot_ext}"; 
  echo "  and outputting TO"; 
  echo "${out_fname}"; 
  echo "    ...";
  convert "${full_fname}" -type truecolor \
    -colorspace srgb -define png:color-type=2 \
      PNG24:"${out_fname}" \
        && echo "        ...  success!" \
        || echo "        ...  FAILURE!"; \
done < _convert_bilevel.list | \
                        tee converting_bilevel_$(date +'%s').out
```

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_bl2gs3ch${dot_ext}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  convert "${full_fname}" -type truecolor \
    -colorspace srgb -define png:color-type=2 \
          PNG24:"${out_fname}" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_bilevel.list | \
                        tee converting_bilevel_$(date +'%s').out

  Converting - as needed
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001.png
  and outputting TO
../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001_bl2gs3ch.png
    ...
        ...  success!

  Converting - as needed
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002.png
  and outputting TO
../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00002_bl2gs3ch.png
    ...
        ...  success!

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find ../try_magick_1pass_2nd_output/ -type f \
                                       -iname "*bl2gs3ch.png"    \
                                       -print0 | \
   xargs -I'{}' -0 \
identify -format "$[magick] %[colorspace] %[type] %[extension] "\
"%[bit-depth] %[channels]\n" "{}"
0 sRGB Bilevel png 1 srgb
0 sRGB Bilevel png 1 srgb

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ identify -verbose ../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001_bl2gs3ch.png
Image:
  Filename: ../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00001_bl2gs3ch.png
  Format: PNG (Portable Network Graphics)
  Mime type: image/png
  Class: DirectClass
  Geometry: 536x250+0+0
  Resolution: 37.8x37.8
  Print size: 14.1799x6.61376
  Units: PixelsPerCentimeter
  Colorspace: sRGB
  Type: Bilevel
  Base type: Undefined
  Endianness: Undefined
  Depth: 8/1-bit
  Channel depth:
    Red: 1-bit
    Green: 1-bit
    Blue: 1-bit
  Channel statistics:
    Pixels: 134000
    Red:
      min: 255  (1)
      max: 255 (1)
      mean: 255 (1)
      standard deviation: 0 (0)
      kurtosis: 1.6384e+52
      skewness: 9.375e+35
      entropy: 0
    Green:
      min: 255  (1)
      max: 255 (1)
      mean: 255 (1)
      standard deviation: 0 (0)
      kurtosis: 1.6384e+52
      skewness: 9.375e+35
      entropy: 0
    Blue:
      min: 255  (1)
      max: 255 (1)
      mean: 255 (1)
      standard deviation: 0 (0)
      kurtosis: 1.6384e+52
      skewness: 9.375e+35
      entropy: 0
  Image statistics:
    Overall:
      min: 255  (1)
      max: 255 (1)
      mean: 255 (1)
      standard deviation: 0 (0)
      kurtosis: 8.192e+51
      skewness: 1e+36
      entropy: 0
  Colors: 1
  Histogram:
    134000: (255,255,255) #FFFFFF white
  Rendering intent: Perceptual
  Gamma: 0.45455
  Chromaticity:
    red primary: (0.64,0.33)
    green primary: (0.3,0.6)
    blue primary: (0.15,0.06)
    white point: (0.3127,0.329)
  Matte color: grey74
  Background color: white
  Border color: srgb(223,223,223)
  Transparent color: none
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 536x250+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: Zip
  Orientation: Undefined
  Properties:
    date:create: 2024-01-27T02:01:53+00:00
    date:modify: 2024-01-27T02:01:53+00:00
    png:bKGD: chunk was found (see Background color, above)
    png:cHRM: chunk was found (see Chromaticity, above)
    png:gAMA: gamma=0.45455 (See Gamma, above)
    png:IHDR.bit-depth-orig: 8
    png:IHDR.bit_depth: 8
    png:IHDR.color-type-orig: 2
    png:IHDR.color_type: 2 (Truecolor)
    png:IHDR.interlace_method: 0 (Not interlaced)
    png:IHDR.width,height: 536, 250
    png:pHYs: x_res=3780, y_res=3780, units=1
    png:sRGB: intent=0 (Perceptual Intent)
    png:text: 2 tEXt/zTXt/iTXt chunks were found
    png:tIME: 2024-01-27T02:01:53Z
    signature: 14b88e3053bb8affa49fe5520f83c1afcdd8f32e699f6ffc6e9bc9730ad82196
  Artifacts:
    verbose: true
  Tainted: False
  Filesize: 1180B
  Number pixels: 134000
  Pixels per second: 44.8536MP
  User time: 0.000u
  Elapsed time: 0:01.002
  Version: ImageMagick 7.0.10-27 Q16 x86_64 2021-02-07 https://imagemagick.org

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$
```


`# ` PLANNING COMMANDS



`## ` Grayscale to 3-channel : in progress at 2024-01-27T101900 

```
while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_gs2gs3ch${dot_ext}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  convert "${full_fname}" -type truecolor \
    -colorspace srgb -define png:color-type=2 \
          PNG24:"${out_fname}" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_grayscale.list | \
                        tee converting_grayscale_$(date +'%s').out
```

`# ` Actual command

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_gs2gs3ch${dot_ext}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  convert "${full_fname}" -type truecolor \
    -colorspace srgb -define png:color-type=2 \
          PNG24:"${out_fname}" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_grayscale.list | \
                        tee converting_grayscale_$(date +'%s').out
```

`## ` Remove alpha channel from those with alpha channel


`# ` (After having removed alpha,)<br/>
`#+` Get the complete list of non-grayscale<br/>
`#+` This should simply involve bringing back<br/>
`#+` however many srgba files were converted;<br/>
`#+` We have five, so we can simply find them<br/>
`#+` with the `_al2tc.png`, then, when we convert<br/>
`#+` them, we'll have `_al2tc2gs3ch.png`.<br/>

```
while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_al2tc${dot_ext}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  convert "${full_fname}" -alpha off -type truecolor \
    -colorspace srgb -define png:color-type=2 \
          PNG24:"${out_fname}" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_w_alpha.list | \
                        tee converting_w_alpha_$(date +'%s').out
```

`# ` At the actual terminal

```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_al2tc${dot_ext}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  convert "${full_fname}" -alpha off -type truecolor \
    -colorspace srgb -define png:color-type=2 \
          PNG24:"${out_fname}" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_w_alpha.list | \
                        tee converting_w_alpha_$(date +'%s').out
```



`## ` get dir-path-less just-had-alpha-removed fnames,<br/>
`##+` let's call the file `_convert_alpha_removed.list`<br/>
`##+` then move them back to the input folder - <br/>
`##+` `/cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output`<br/>
`##+` Combine their filenames with the<br/>
`##+` `_maybe_convert_details.list`<br/>
`##+` `cat _maybe_convert_details.list _convert_alpha_removed.list > \`<br/>
`##+` `  _convert_all_color.list`<br/>


```
bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find ../try_magick_1pass_2nd_output/ -type f -name *al2tc.png" | wc -l
> ^C

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find ../try_magick_1pass_2nd_output/ -type f -name "*al2tc.png" | wc -l
5

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ find ../try_magick_1pass_2nd_output/ -type f -name "*al2tc.png" | sed 's#^##g' > pre_convert_alpha_removed.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cat pre_convert_alpha_removed.list
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_001_1057binding_al2tc.png
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_002_1057pastedown_reuseTrue_al2tc.png
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc.png
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc.png
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ while read -r line; do fname="${line}"; mv "${fname}" .; done < pre_convert_alpha_removed.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk -F'/' '{print $NF}' < pre_convert_alpha_removed.list
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_001_1057binding_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_002_1057pastedown_reuseTrue_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ awk -F'/' '{print $NF}' < pre_convert_alpha_removed.list > _convert_alpha_removed.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ cat _maybe_convert_details.list _convert_alpha_removed.list > _convert_all_color.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ vim convert_all_color.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ head _convert_all_color.list
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00006.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00007.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00008.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00009.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00010.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00011.png
        BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00012.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ head _convert_all_color.list | cat -ETv
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00006.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00007.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00008.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00009.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00010.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00011.png$
^IBNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00012.png$

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ grep "        " _convert_all_color.list | wc -l
622

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ wc -l < _convert_all_color.list
627

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ sed -i.bak 's#^\t##g;' _convert_all_color.list

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ head _convert_all_color.list
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00006.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00007.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00008.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00009.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00010.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00011.png
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00012.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ tail _convert_all_color.list
zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p8-59.png
zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p85-530.png
zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p86-536.png
zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p87-542.png
zLOC_-_MarcoPolo_gdcwdl-wdl-14300_p9-65.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_001_1057binding_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_002_1057pastedown_reuseTrue_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc.png
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc.png

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$ # Okay.

bballdave025@MY-MACHINE /cygdrive/c/Users/bballdave025/Desktop/try_magick_1pass_output
$
```

####################

# COME HERE, TOO

####################

`# ` Figuring out command

<strike>
<pre>
while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\1#g;'); \
  mayb_desc=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\2#g;'); \
  my_3=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\3#g;'); \
  my_4=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\4#g;'); \
  my_5=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\5#g;'); \
  my_6=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\2#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "base_fn: ${base_fname}";
  echo "mayb_desc: ${mayb_desc}";
  echo "my_3: ${my_3}";
  echo "my_4: ${my_4}";
  echo "my_5: ${my_5}";
  echo "my_6: ${my_6}";
  echo "dot_ext: ${dot_ext}";
done < _convert_all_color.list | head -n 30
</pre>
</strike>

<strike>
<pre>
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${base_fn}_al2tc${dot_ext}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  echo "     COMMAND WILL BE:"
  echo "convert \"${full_fname}\" -alpha off -type truecolor \
    -colorspace srgb -define png:color-type=2 \
          PNG24:\"${out_fname}\"" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_all_color.list | \
                        tee converting_all_color_$(date +'%s').out
</pre>
</strike>

<strike>
<pre>
while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(_al2tc\)\?\)\([.][^.]\+\)$#\1#g;'); \
  mayb_desc=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\2#g;'); \
  my_3=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\3#g;'); \
  my_4=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\4#g;'); \
  my_5=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\5#g;'); \
  my_6=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(\([_]\)\([^_]\+\)\)\?\)\([.][^.]\+\)$#\2#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "base_fn: ${base_fname}";
  echo "mayb_desc: ${mayb_desc}";
  echo "my_3: ${my_3}";
  echo "my_4: ${my_4}";
  echo "my_5: ${my_5}";
  echo "my_6: ${my_6}";
  echo "dot_ext: ${dot_ext}";
done < _convert_all_color.list | head -n 30


`#  Is it mayb <- \2 or \3 or \4?`<br/>
`#+ Is it dot_ext <- \6 or another?`<br/>
`#+ that's why we're doing this test!`<br/>


while read -r line; do \
  echo; \
  full_fname="${line}"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(_al2tc\)\?\)\([.]png\)$#\1#g;'); \
  mayb_desc=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\(\(_al2tc\)\?\)\([.]png\)$#\2#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  echo "base_fn: ${base_fname}";
  echo "mayb_desc: ${mayb_desc}";
  echo "dot_ext: ${dot_ext}";
done < _convert_all_color.list | head -n 30

</pre>
</strike>

`# ` Other approach

```
while read -r line; do
  echo; \
  full_fname="${line}"; new_fname="problem-here"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  new_fname="${base_fn}_tc2gs3ch${dot_ext}"; \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${new_fname}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  echo "  Command would be:"
  echo "convert \"${full_fname}\" -alpha off -type truecolor "\
"    -colorspace srgb -define png:color-type=2 "\
"    -fx '(r+g+b)/3' PNG24:\"${out_fname}\"" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_all_color.list | tail -n 30
```

`## ` And now, the test in the terminal

```
Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ while read -r line; do
  echo; \
  full_fname="${line}"; new_fname="problem-here"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  new_fname="${base_fn}_tc2gs3ch${dot_ext}"; \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${new_fname}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  echo "  Command would be:"
  echo "convert \"${full_fname}\" -alpha off -type truecolor "\
"    -colorspace srgb -define png:color-type=2 "\
"    -fx '(r+g+b)/3' PNG24:\"${out_fname}\"" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_all_color.list | head -n 30

  Converting - as needed
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003.png
  and outputting TO
../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003_tc2gs3ch.png
    ...
  Command would be:
convert "BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00003_tc2gs3ch.png"
        ...  success!

  Converting - as needed
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004.png
  and outputting TO
../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004_tc2gs3ch.png
    ...
  Command would be:
convert "BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00004_tc2gs3ch.png"
        ...  success!

  Converting - as needed
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005.png
  and outputting TO
../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005_tc2gs3ch.png
    ...
  Command would be:
convert "BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00005_tc2gs3ch.png"
        ...  success!

  Converting - as needed
BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00006.png

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$ while read -r line; do
  echo; \
  full_fname="${line}"; new_fname="problem-here"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  new_fname="${base_fn}_tc2gs3ch${dot_ext}"; \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${new_fname}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  echo "  Command would be:"
  echo "convert \"${full_fname}\" -alpha off -type truecolor "\
"    -colorspace srgb -define png:color-type=2 "\
"    -fx '(r+g+b)/3' PNG24:\"${out_fname}\"" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_all_color.list | tail -n 30
  Command would be:
convert "SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_002_1057pastedown_reuseTrue_al2tc.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_002_1057pastedown_reuseTrue_al2tc_tc2gs3ch.png"
        ...  success!

  Converting - as needed
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc.png
  and outputting TO
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc_tc2gs3ch.png
    ...
  Command would be:
convert "SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_003_1057first_reusebehindTrue_al2tc_tc2gs3ch.png"
        ...  success!

  Converting - as needed
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc.png
  and outputting TO
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc_tc2gs3ch.png
    ...
  Command would be:
convert "SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_005_1057f200v-201_al2tc_tc2gs3ch.png"
        ...  success!

  Converting - as needed
SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc.png
  and outputting TO
../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc_tc2gs3ch.png
    ...
  Command would be:
convert "SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc.png" -alpha off -type truecolor     -colorspace srgb -define png:color-type=2     -fx '(r+g+b)/3' PNG24:"../try_magick_1pass_2nd_output/SellerLesEnluminures_-_franciscan-breviary-use-of-rome-141638_-_007_reusebehindTrue_1057f527v-528_al2tc_tc2gs3ch.png"
        ...  success!

Anast@DESKTOP-O7KM5A5 /cygdrive/c/Users/Anast/Desktop/try_magick_1pass_output
$
```


`## ` And now, the conversion in the terminal

```
while read -r line; do
  echo; \
  full_fname="${line}"; new_fname="problem-here"; \
  base_fn=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\1#g;'); \
  dot_ext=$(echo "${full_fname}" | \
    sed 's#^\(.*\)\([.][^.]\+\)$#\2#g;'); \
  new_fname="${base_fn}_tc2gs3ch${dot_ext}"; \
  echo "  Converting - as needed"; \
  echo "${full_fname}"; \
  out_fname="../try_magick_1pass_2nd_output/"\
"${new_fname}"; \
  echo "  and outputting TO"; \
  echo "${out_fname}"; \
  echo "    ..."; \
  convert "${full_fname}" -alpha off -type truecolor \
                          -colorspace srgb \
                          -define png:color-type=2 \
                          -fx '(r+g+b)/3' \
                                 PNG24:"${out_fname}" \
            && echo "        ...  success!" \
            || echo "        ...  FAILURE!"; \
done < _convert_all_color.list | \
                        tee converting_all_color_$(date +'%s').out
```

### Averaging for to-grayscale (24-bit) just above here

`convert test.png -fx '(r+g+b)/3' gray_fx_average.png`


`### ` This was useful before, but I went on a different path.<br/>
`###+` I have just the color ones together. It might still<br/>
`###+` be worth doing this whole thing, if I won't have<br/>
`###+` finished it before<br/>

```
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}"; full_fname=$(echo "${orig}" | sed 's#^[.]/##g');
echo; printf "${full_fname} ";
gs_ness=$(convert "${orig}" -colorspace HSB \
                  -channel green -separate +channel \
                  -format "%[fx:100*mean]\n" info: 2>/dev/null);
echo "; gs_ness ${gs_ness}";
if [ ! -z $gs_ness ]; then
  if [ $gsness -gt 0 ]; then
    echo "Converting for ${orig}";
    # stuff in previous command, I guess
  else
    echo "It seems this is already pure r=g=b grayscale.";
    echo "Nothing more to do."
  fi;
else
  echo "Nothing to be done for this one. It gave us"
  echo "a blank string for its grayscale-ness. (?)"
fi;
echo;
echo "-------------------------";
' 2>&1 | tee -a \
  conversion_to_eq-rgb_gs_$(date +'%s_%Y-%m-%dT%H%M%S%z').out
```




