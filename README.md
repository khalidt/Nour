# Nour
Nour is a tool that translates Arabic words, letters, or sentences to and from  Braille notations.

Nour v0.0.1 has used the unified braille standard for Arabic that was developed at a conference in Saudi Arabia in 2002. However, some other Arab countries in 2013 do not sign it up thus they use a different standard of braille notation which will be added in the next version of Nour. based on [the world Braille usage](https://unesdoc.unesco.org/ark:/48223/pf0000087242) we added the unified braille standard for Arabic and we will add other Arab countries standards 

# Example:

#### From inside python shell:
```python
from Nour import nour
nour.arabicToBrailles('بسم الله الرحمن الرحيم')
nour.brailleToArabic('⠍⠗⠱⠃⠁')
```

output:
```
⠃⠎⠍⠀⠁⠇⠇⠓⠀⠁⠇⠗⠱⠍⠝⠀⠁⠇⠗⠱⠊⠍
مرحبا
```
#### From CLI:
```bash
python nour -br ⠗
```
output:
```
ر
```

#### From virtualenv:
```bash
python -m Nour.nour -br ⠗
```
output:
```
ر
```

# Installation:

* ### Install from pip:
  Use the package manager [pip](https://pypi.org/project/pip/) to install Nour.

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
  -o, --out             Write Convertion to file                   
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


## License
![Image of GPLv3](https://www.gnu.org/graphics/gplv3-127x51.png)
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)