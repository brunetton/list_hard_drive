## What is this ?

I've plenty of hard drives laying around, and when I'm looking for a file I spent a lot of time trying to remember where this file could be ? In which hard drive this folder is ?

This project tried to answer those questions by creating list of all files found on given path; ignoring `.git` dirs.

## Installation

    pip3 install -r requirements.txt

## Usage

    list_hard_drive.py /media/bruno/my_drive/ > red_hd_2.tsv

This will create a file containing files path and size. For example:

```tsv
Mariage Estelle/photos vacances/SF3.JPG	2.0 MB
Mariage Estelle/photos vacances/SF4.JPG	2.5 MB
Mariage Estelle/photos vacances/SF5.JPG	2.3 MB
Mariage Estelle/photos vacances/versailles.JPG	4.1 MB
Musiques libres/04 - Stories from Emona IV.mp3	4.6 MB
Musiques libres/07 Shadow Force.mp3	6.2 MB
Musiques libres/512px-CC-logo.svg.png	14.0 kB
Musiques libres/Alainsam_-_My_dream_in_blues.mp3	5.4 MB
```

## TODO

- add an option to customize dirs/files patterns to ignore (by default, only '.git')
