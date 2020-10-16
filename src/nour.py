import argparse
import textwrap 
from datetime import datetime
from Nour import util as u
import Nour

def asciiBrailleTable():
    for a, b in zip(u.asciicodes, u.brailles):
        print(hex(ord(a)), '|', a, '|', b)


def arabicBrailleTable():
    for a, b in u.dicArabicToBraille.items():
        if len(a) > 1:
            print(hex(ord(a[0])), hex(ord(a[1])), '|', a, '|', b)
        else:
            print(hex(ord(a)), '|', a, '|', b)


def asciiToBraille(text):
    text = str.lower(text)
    braille = ''
    print('Text Length:', len(text))

    for x in text:
        braille += u.dicAsciiToBraille[x]
    return braille


def brailleToAscii(braille):
    braille = str.lower(braille)
    text = ''
    print('Braille Length:', len(braille))
    for x in braille:
        text += u.dicBarilleToAscii[x]
    return text


def arabicToBraille(text):
    braille = ''
    print('Text Length:', len(text))
    for x in text:
        braille += u.dicArabicToBraille[x]
    return braille


def brailleToArabic(braille):
    text = ''
    text1 = ''
    txt = ''
    print('Braille Length:', len(braille))
    c = 0
    for text in braille:
        if text == '⠼' or text == '⠒':
            c += 1
            text1 = text
        elif c == 1:
            text1 += text
            c = 0
            txt += u.dicBrailleToArabic[text1]
        else:
            txt += u.dicBrailleToArabic[text]
    return txt

def getTextFromFile(path):
  file = open(path,'r',encoding='utf-8-sig')
  text = file.read()
  file.close()
  return text

def writeConvertionToFile(text):
  filename='Nour'+getDateTime()+'.txt'
  print(filename)
  file = open(filename,'w',encoding='utf-8-sig')
  file.write(text)
  file.close()

def getDateTime():
  now = datetime.now()
  dt = now.strftime("%d-%m-%Y-%H-%M")
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

  parser = argparse.ArgumentParser(epilog ='Examples:\nnour -p\nnour -ar مرحبا \nnour -arf arabicTextFile.txt -o\nnour -br ⠓\nnour -brf brailleTextFile.txt\nnour -arf ArTextFile.txt -brf BrTextFile.txt', prog='nour',formatter_class=argparse.RawDescriptionHelpFormatter)
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
      print('Unicode|Letter|Braille\n---------------------')
      arabicBrailleTable()

    if args['arfile'] != None:
      text=getTextFromFile(args['arfile'])
      print('Text from file:\n',text)
      output= arabicToBrailles(text)
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
