# Description 🐋
  **Nour** is an Arabic Braille tool that converts Arabic words, letters, or sentences to and from  Braille notations.
Nour has used the unified braille standard for Arabic that was developed at a conference in Saudi Arabia in 2002. However, some other Arab countries in 2013 do not sign it up thus they use a different standard of braille notation which will be added in the next version of Nour. based on [the world Braille usage](https://unesdoc.unesco.org/ark:/48223/pf0000087242) we added the unified braille standard for Arabic and we will add other Arab countries standards.

# Sample:

#### From inside python shell:
```python
>>> from Nour import nour
>>> nour.arabicToBraille('بسم الله الرحمن الرحيم')
>>> nour.brailleToArabic('⠍⠗⠱⠃⠁')
>>> nour.util.brailles
>>> nour.util.arabic
```

#### Output:
```
⠃⠎⠍⠀⠁⠇⠇⠓⠀⠁⠇⠗⠱⠍⠝⠀⠁⠇⠗⠱⠊⠍
مرحبا
['⠀', '\n', '⠁', '⠃', '⠞', '⠹', '⠚', '⠱', '⠭', '⠙', '⠮', '⠗', '⠵', '⠎', 
  '⠩', '⠯', '⠫', '⠾', '⠿', '⠷', '⠣', '⠋', '⠟', '⠅', '⠇', '⠍', '⠝', '⠓', 
  '⠡', '⠺', '⠊', '⠕', '⠉', '⠧', '⠴⠠', '⠌', '⠨', '⠜', '⠪', '⠳', '⠽', '⠄', 
  '⠥', '⠂', '⠆', '⠑', '⠔', '⠢', '⠒', '⠠', '⠐', '⠰', '⠐⠂', '⠶', '⠦…', '…⠴', 
  '⠠⠦', '⠐⠦', '⠴⠂', '⠲', '⠖', '⠦', '⠤', '⠼⠁', '⠼⠃', '⠼⠉',
  '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚', '⠒⠏']
 
[' ', '\n', 'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 
  'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'ة', 
  'و', 'ي', 'ى', 'ال', 'لا', ']', 'أ', 'إ', 'آ', 'أو', 'ؤ', 'ئ', 'ء', 'ُ', 
  'َ', 'ً', 'ِ', 'ٍ', 'ٌ', 'ْ', 'ّ', '،', '؛', ':', '"', '(', ')', '[', '{', 
  '}', '.', '!', '؟', '-', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '٠', 
  '٪']
```

#### From CLI:
```bash
python nour -br ⠞
```
output:
```
ت
```

#  Requirements
* Python3 >=3.6 


# Installation:

* ### Install from pip:
  Use the package manager [pip](https://pypi.org/project/Nour/) to install Nour.

```bash
pip install Nour
```

# Usage:
```bash
usage: Nour [-h] [-ar ARTEXT] [-br BRTEXT] [-arf ARFILE]           
            [-brf BRFILE] [-o] [-p] [-info]                        
                                                                   
optional arguments:                                                
  -h, --help            show this help message and exit            
  -ar ARTEXT, --artext ARTEXT                                      
                        The Arabic text to be converted to         
                        Braille.                                   
  -br BRTEXT, --brtext BRTEXT                                      
                        The Braille text to be converted to        
                        Arabic.                                    
  -arf ARFILE, --arfile ARFILE                                     
                        The Arabic text file to be converted to    
                        Braille.                                   
  -brf BRFILE, --brfile BRFILE                                     
                        The Braille text file to be converted to   
                        Arabic.                                    
  -o, --out             Write Conversion to file                   
  -p, --print           Print Standard Arabic Braille Code.        
  -info, --info         Print Information about Nour.              
                                                                   
Examples:                                                          
Nour -p                                                            
Nour -ar مرحبا                                                     
Nour -ar arabicTextFile.txt                                        
Nour -arf readFromtext.txt -o                                      
Nour -br ⠓                                                         
Nour -brf brailleTextFile.txt                                      
Nour -arf ArTextFile.txt -abf BrTextFile.txt        
```

# Notes:
* The character that is not in the standard of Arabic Braille code, will be ignored and replaced by space '  '. for **Example:** ~ , ^ , ' , & , /
* Arithmetic and Logic operators are not supported yet.
* Both the Arabic numerals (1,2,3 ...etc) and Eastern Arabic numerals (Hindi)  (١,٢,٣ ... etc) are used by the same Arabic Braille code.
* Underline is not tested but it's included! 
* When using the argument of output file ' **-o** ' it creates a file and writes the conversion to it, the generated file will be named by default as **'Nour %d-%m-%y %H-%M'.txt**. Ex: **Nour 02-10-2020 08-12.txt**.
* The only file that is supported for reading and writing is text **.txt**

# Roadmap:
* Add other Arab countries braille standards.
* Import different files to read from and write to such as:
   - **.docx , .doc, .rtf, .pdf, .html, .odt, xml** and more.
* New feature will be added which is converting the Arabic alphabets in images and extract them to the document file.
* Add mechanism to deal with shapes, Maps ... etc.
* Add Math translation for **Nemeth** and more.

# License


[![GPL3v](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.html)


    Nour is a tool which translates Arabic words, letters 
    or sentences to and from  Braille notations.
    Copyright (C) 2020  Khalid Alkhaldi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
