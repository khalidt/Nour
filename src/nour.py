import argparse
from datetime import datetime
from Nour import util
import Nour

def asciiBrailleTable():
    print('{} {:>10} {:>15}'.format('\nUnicode','Letter','Braille'))
    print('{} {:>10} {:>15}'.format('\n--------','--------','--------'))
    for a, b in zip(util.asciicodes, util.brailles):
        print('{} {:>10} {:^15}'.format(hex(ord(a)),a,b))


def arabicBrailleTable():
    print('{} {:>10} {:>15}'.format('\nUnicode','Letter','Braille'))
    print('{} {:>10} {:>15}'.format('\n--------','--------','--------'))
    for a, b in util.dicArabicToBraille.items():
        if len(a) > 1:            
            print('{}{} {:>6} {:>7}'.format(hex(ord(a[0])),hex(ord(a[1])),a,b))
        else:            
            print('{} {:>10} {:^15}'.format(hex(ord(a)),a,b))

def asciiToBraille(text):
    text = str.lower(text)
    braille = ''
    count=0
    print('Text Length:', len(text))

    for x in text:
      if x in util.dicAsciiToBraille:
        braille += util.dicAsciiToBraille[x]
      else:
        count+=1
        print('\tWarring: one letter can\'t be decoded! -> (',x,')')
        braille+=''
    if count>0:
      print('\nInfo: The number of letters can\'t be translated:',count)
    return braille


def brailleToAscii(braille):
    braille = str.lower(braille)
    text = ''
    print('Braille Length:', len(braille))
    for x in braille:
        text += util.dicBarilleToAscii[x]
    return text

def arabicToBraille(text):
    braille = ''
    error=0
    errChar=''
    print('Text Length:', len(text))
    for x in text:
      if x in util.dicArabicToBraille:
        braille += util.dicArabicToBraille[x]
      else:
        error+=1
        errChar+=x+', '
        braille +=' '
    if error>0:
      print('\nInfo: The number of letters can\'t be converted:',error)
      print('Warring: letters can\'t be converted:\n [',errChar,']')
    print('The translation is:\n')
    return braille


def brailleToArabic(braille):
    prefix = ''
    suffix = ''
    punc =''
    txt = ''
    c = 0
    error=0
    errChar=''
    for text in braille:
          if text in ['⠼', '⠒','⠦','⠐','…','⠴','⠶'] and c<1:
              c += 1
              prefix = text                
          elif c == 1:                
              suffix =text            
              punc=prefix+suffix                
              c = 0
              if punc in util.dicBrailleToArabic:
                txt += util.dicBrailleToArabic[punc]
              else:                  
                if prefix in util.brailles:                    
                  txt += util.dicBrailleToArabic[prefix]                    
                else:
                  error+=1
                  errChar+=prefix+' '
                if suffix in util.brailles:
                  txt += util.dicBrailleToArabic[suffix]
                else:                    
                  error+=1
                  errChar+=suffix+' '
          else:
              if text in util.brailles:
                txt += util.dicBrailleToArabic[text]
              else:                  
                error+=1
                errChar+=text+' '
    if c==1 and prefix in util.brailles:
      txt+= util.dicBrailleToArabic[prefix]
    elif c==1:
      error+=1
      errChar+=prefix+' '
    if error!=0:
       print('\n\tInfo: The number of Braille can\'t be converted:',error,'\n->[',errChar,']\n')
    if len(txt)>0:
      print('Arabic Text:')
    return txt


def getTextFromFile(path):
  file = open(path,'r',encoding='utf-8-sig')
  text = file.read()
  file.close()
  return text

def writeConvertionToFile(text):
  filename='Nour braille '+getDateTime()+'.txt'
  print(filename)
  file = open(filename,'w',encoding='utf-8-sig')
  file.write(text)
  file.close()

def getDateTime():
  now = datetime.now()
  dt = now.strftime("%d-%m-%Y %H-%M")
  return dt

def info():
  v=Nour.__version__
  return f'''\
  -------------------------------------
            Nour v{v}
    Author: Khalid Alkhaldi
   Email: khalid.t.alkhaldi@gmail.com
  URL: https:\\\\github.com\\khalidt\\Nour
  -------------------------------------'''

def checkArgv(args):
  for i in args.values():
    if i != None:
      return True 
  return False
  
def main():
  parser = argparse.ArgumentParser(epilog ='Examples:\nnour -p\nnour -ar مرحبا \nnour -arf arabicTextFile.txt -o\nnour -br ⠓\nnour -brf brailleTextFile.txt\nnour -arf ArTextFile.txt -brf BrTextFile.txt', prog='nour')
  parser.add_argument("-ar","--artext",
    help="The Arabic text to be converted to Braille.")
  parser.add_argument("-br", "--brtext",
    help="The Braille text to be converted to Arabic.")
  parser.add_argument("-arf", "--arfile",
    help="The Arabic text file to be converted to Braille.")
  parser.add_argument("-brf", "--brfile",
    help="The Braille text file to be converted to Arabic.")
  parser.add_argument("-o", "--out",action='store_true',
    default=None ,
    help="Write Convertion to file")
  parser.add_argument("-p", "--print", action='store_true',
    default=None,
    help="Print Standard Arabic Braille Code.")
  parser.add_argument("-info", "--info", action='store_true',
    default=None,
    help="Print Information about Nour.")
  args = vars(parser.parse_args())
  output=''
  if checkArgv(args) :
    if args['artext'] != None:
      print('Input is:',args['artext'])
      output=arabicToBrailles(args['artext'])
      print(output)

    if args['brtext'] != None:
      print('Input is:',args['brtext'])
      output=brailleToArabic(args['brtext'])
      print(output)

    if args['print'] != None:
      arabicBrailleTable()

    if args['arfile'] != None:
      text=getTextFromFile(args['arfile'])
      print('Text from file:\n',text)
      output= arabicToBraille(text)
      print(output)

    if args['brfile'] != None:
      text=getTextFromFile(args['brfile'])
      print('Barile from file:\n',text )
      output= brailleToArabic(text)
      print(output)

    if args['info']:
      print(info())

    if args['out'] != None:
      writeConvertionToFile(output)
  else:
    print('Usage:\n\nnour [-h] [-ar ARTEXT] [-br BRTEXT] [-arf ARFILE] [-brf BRFILE] [-o] [-p] [-info]')

if __name__ == '__main__':
  main()