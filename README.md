# snake-sheet-generator
"Snaking" spreadsheet generator for Williams Forestry


This is a program for generating "snaking" spreadsheets while filtering
particular fields (coordinates) from being used. With no filter, it would
generate something like the following:

>
      ~# ssg 2 5 5 out.csv 
      no filter found, creating square grid
      final matrix:
      [2,  '', 12, '', 22]
      ['', 10, '', 20, '']
      [4,  '', 14, '', 24]
      ['',  8, '', 18, '']
      [6,  '', 16, '', 26]
      out.csv written!

Help should first and foremost be seen with the '-h' flag, courtesy of
argparse.

Also uses filtering to skip certain cells. For instance, a filter of
>
      1,1,1,
      1,1,
      1,,

would result in the output of
>
    ~# ssg 2 5 5 out.csv
    filter found
    final matrix:
    ['', '', '', 16, '']
    ['', '', 8, '', 18]
    ['', 6, '', 14, '']
    [2, '', 10, '', 20]
    ['', 4, '', 12, '']
    out.csv writen!


# Installation
Clone it with git
>
    git clone https://github.com/ben-en/snake-sheet-generator/

Enter the directory
>
      cd snake-sheet-generator

Install with `pip`
>
      pip install ./
      
Run with `ssg`
>
      ssg -h
