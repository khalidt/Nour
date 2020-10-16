# ASCII
asciicodes = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '[', '\\', ']', '^', '_']

brailles = ['⠀', '⠮', '⠐', '⠼', '⠫', '⠩', '⠯', '⠄', '⠷', '⠾', '⠡', '⠬', '⠠', '⠤', '⠨', '⠌', '⠴', '⠂', '⠆', '⠒', '⠲',
            '⠢',
            '⠖', '⠶', '⠦', '⠔', '⠱', '⠰', '⠣', '⠿', '⠜', '⠹', '⠈', '⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚',
            '⠅',
            '⠇', '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', '⠪', '⠳', '⠻', '⠘', '⠸']

dicAsciiToBraille = {' ': '⠀', '!': '⠮', '"': '⠐', '#': '⠼', '$': '⠫', '%': '⠩', '&': '⠯', '\'': '⠄',
                     '(': '⠷', ')': '⠾', '*': '⠡', '+': '⠬', ',': '⠠', '-': '⠤', '.': '⠨', '/': '⠌',
                     '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢', '6': '⠖', '7': '⠶',
                     '8': '⠦', '9': '⠔', ':': '⠱', ';': '⠰', '<': '⠣', '=': '⠿', '>': '⠜', '?': '⠹',
                     '@': '⠈', 'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛',
                     'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
                     'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺',
                     'x': '⠭', 'y': '⠽', 'z': '⠵', '[': '⠪', '\\': '⠳', ']': '⠻', '^': '⠘', '_': '⠸'}

dicBarilleToAscii = {'⠀': ' ', '⠮': '!', '⠐': '"', '⠼': '#', '⠫': '$', '⠩': '%', '⠯': '&', '⠄': '\'',
                     '⠷': '(', '⠾': ')', '⠡': '*', '⠬': '+', '⠠': ',', '⠤': '-', '⠨': '.', '⠌': '/',
                     '⠴': '0', '⠂': '1', '⠆': '2', '⠒': '3', '⠲': '4', '⠢': '5', '⠖': '6', '⠶': '7',
                     '⠦': '8', '⠔': '9', '⠱': ':', '⠰': ';', '⠣': '<', '⠿': '=', '⠜': '>', '⠹': '?',
                     '⠈': '@', '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd', '⠑': 'e', '⠋': 'f', '⠛': 'g',
                     '⠓': 'h', '⠊': 'i', '⠚': 'j', '⠅': 'k', '⠇': 'l', '⠍': 'm', '⠝': 'n', '⠕': 'o',
                     '⠏': 'p', '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't', '⠥': 'u', '⠧': 'v', '⠺': 'w',
                     '⠭': 'x', '⠽': 'y', '⠵': 'z', '⠪': '[', '⠳': '\\', '⠻': ']', '⠘': '^', '⠸': '_'}

dicArabicToBraille = {' ': '⠀', 'ا': '⠁', 'ب': '⠃', 'ت': '⠞', 'ث': '⠹', 'ج': '⠚', 'ح': '⠱', 'خ': '⠭',
                      'د': '⠙', 'ذ': '⠮', 'ض': '⠫', 'ر': '⠗', 'ز': '⠵', 'س': '⠎', 'ش': '⠩', 'ص': '⠯', 'ط': '⠾',
                      'ظ': '⠿', 'ع': '⠷', 'غ': '⠣', 'ف': '⠋', 'ق': '⠟', 'ك': '⠅', 'ل': '⠇', 'م': '⠍','ة':'⠡',
                      'ن': '⠝', 'ه': '⠓', 'و': '⠺', 'ي': '⠊', 'ى': '⠕', 'ٍ': '⠔', 'ال': '⠉', 'لا': '⠧',
                      'أ': '⠌', 'إ': '⠨', 'آ': '⠜', 'أو': '⠪', 'ؤ': '⠳', 'ئ': '⠽', 'ء': '⠄', 'ُ': '⠥',
                      'َ': '⠂', 'ِ': '⠑', 'ٌ': '⠢', '؛': '⠰', 'ْ': '⠒', 'ّ': '⠠', '،': '⠐', ':': '⠐⠂','\n':'\n',
                      '.': '⠲', '!': '⠖', '؟': '⠦', 'ـ': '⠤', '١': '⠼⠁', '٢': '⠼⠃', '٣': '⠼⠉', '٤': '⠼⠙',
                      '٥': '⠼⠑', '٦': '⠼⠋', '٧': '⠼⠛', '٨': '⠼⠓', '٩': '⠼⠊', '٠': '⠼⠚', '٪': '⠒⠏'}

dicBrailleToArabic = {'⠀': ' ', '⠁': 'ا', '⠃': 'ب', '⠞': 'ت', '⠹': 'ث', '⠚': 'ج', '⠱': 'ح', '⠭': 'خ',
                      '⠙': 'د', '⠮': 'ذ', '⠗': 'ر', '⠵': 'ز', '⠎': 'س', '⠩': 'ش', '⠯': 'ص', '⠫': 'ض', '⠾': 'ط',
                      '⠿': 'ظ', '⠷': 'ع', '⠣': 'غ', '⠋': 'ف', '⠟': 'ق', '⠅': 'ك', '⠇': 'ل', '⠍': 'م',
                      '⠝': 'ن', '⠓': 'ه', '⠺': 'و', '⠊': 'ي', '⠕': 'ى', '⠔': 'ٍ', '⠉': 'ال', '⠧': 'لا','⠡':'ة',
                      '⠌': 'أ', '⠨': 'إ', '⠜': 'آ', '⠪': 'أو', '⠳': 'ؤ', '⠽': 'ئ', '⠄': 'ء', '⠥': 'ُ','\n':'\n',
                      '⠂': 'َ', '⠑': 'ِ', '⠢': 'ٌ', '⠰': '؛', '⠒': 'ْ', '⠠': 'ّ', '⠐': '،', '⠐⠂': ':', '⠲': '.',
                      '⠖': '!', '⠦': '؟', '⠤': 'ـ', '⠼⠁': '١', '⠼⠃': '٢', '⠼⠉': '٣', '⠼⠙': '٤', '⠼⠑': '٥',
                      '⠼⠋': '٦', '⠼⠛': '٧', '⠼⠓': '٨', '⠼⠊': '٩', '⠼⠚': '٠', '⠒⠏': '٪'}