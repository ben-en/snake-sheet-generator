# snake-sheet-generator
"Snaking" spreadsheet generator for Williams Forestry


This is a program for generating "snaking" spreadsheets while filtering
particular fields (coordinates) from being used. With no filter, it would
generate something like the following:

>
      ~# ssg 2 5 5 out.csv 
>
      [2,  '', 12, '', 22]
      ['', 10, '', 20, '']
      [4,  '', 14, '', 24]
      ['',  8, '', 18, '']
      [6,  '', 16, '', 26]
      out.csv written!

Help should first and foremost be seen with the '-h' flag, courtesy of
argparse.


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
