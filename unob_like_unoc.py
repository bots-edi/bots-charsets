""" interpreters UNOB as UNOC
Adapted by Henk-Jan Ebbers for Bots open source EDI translator
Controls handing of UNOB both incoming (decode) and outgoing (encode).
Values can be converted, eg e->E
Entries not available/commented out give errors for 'strict' handling; this can be controlled via syntax option in grammar:
    'checkcharsetin':'strict', #decode: strict, ignore or botsreplace (replace with char as set in bots.ini).
    'checkcharsetout':'strict', #encode: strict, ignore or botsreplace (replace with char as set in bots.ini).
"""
import codecs

### Codec APIs
class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)
    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API
class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_map)[0]

def getregentry():
    return codecs.CodecInfo(
        name='unob',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )

### Decoding (for incoming edifact) ###############################
decoding_map = {
0x0000:0x0000, #NUL
0x0001:0x0001, #SOH
0x0002:0x0002, #STX
0x0003:0x0003, #ETX
0x0004:0x0004, #EOT
0x0005:0x0005, #ENQ
0x0006:0x0006, #ACK
0x0007:0x0007, #Bell
0x0008:0x0008, #BackSpace
0x0009:0x0009, #Tab
0x000a:0x000a, #lf
0x000b:0x000b, #Vertical Tab
0x000c:0x000c, #FormFeed
0x000d:0x000d, #cr
0x000e:0x000e, #SO
0x000f:0x000f, #SI
0x0010:0x0010, #DLE
0x0011:0x0011, #DC1
0x0012:0x0012, #DC2
0x0013:0x0013, #DC3
0x0014:0x0014, #DC4
0x0015:0x0015, #NAK
0x0016:0x0016, #SYN
0x0017:0x0017, #ETB
0x0018:0x0018, #CAN
0x0019:0x0019, #EM
0x001a:0x001a, #SUB, cntrl-Z
0x001b:0x001b, #ESC
0x001c:0x001c, #FS
0x001d:0x001d, #GS
0x001e:0x001e, #RS
0x001f:0x001f, #US
0x0020:0x0020, #<space>
0x0021:0x0021, #!
0x0022:0x0022, #"
0x0023:0x0023, ##
0x0024:0x0024, #$
0x0025:0x0025, #%
0x0026:0x0026, #&
0x0027:0x0027, #'
0x0028:0x0028, #(
0x0029:0x0029, #)
0x002a:0x002a, #*
0x002b:0x002b, #+
0x002c:0x002c, #,
0x002d:0x002d, #-
0x002e:0x002e, #.
0x002f:0x002f, #/
0x0030:0x0030, #0
0x0031:0x0031, #1
0x0032:0x0032, #2
0x0033:0x0033, #3
0x0034:0x0034, #4
0x0035:0x0035, #5
0x0036:0x0036, #6
0x0037:0x0037, #7
0x0038:0x0038, #8
0x0039:0x0039, #9
0x003a:0x003a, #:
0x003b:0x003b, #;
0x003c:0x003c, #<
0x003d:0x003d, #=
0x003e:0x003e, #>
0x003f:0x003f, #?
0x0040:0x0040, #@
0x0041:0x0041, #A
0x0042:0x0042, #B
0x0043:0x0043, #C
0x0044:0x0044, #D
0x0045:0x0045, #E
0x0046:0x0046, #F
0x0047:0x0047, #G
0x0048:0x0048, #H
0x0049:0x0049, #I
0x004a:0x004a, #J
0x004b:0x004b, #K
0x004c:0x004c, #L
0x004d:0x004d, #M
0x004e:0x004e, #N
0x004f:0x004f, #O
0x0050:0x0050, #P
0x0051:0x0051, #Q
0x0052:0x0052, #R
0x0053:0x0053, #S
0x0054:0x0054, #T
0x0055:0x0055, #U
0x0056:0x0056, #V
0x0057:0x0057, #W
0x0058:0x0058, #X
0x0059:0x0059, #Y
0x005a:0x005a, #Z
0x005b:0x005b, #[
0x005c:0x005c, #\\
0x005d:0x005d, #]
0x005e:0x005e, #^
0x005f:0x005f, #_
0x0060:0x0060, #`
0x0061:0x0061, #a
0x0062:0x0062, #b
0x0063:0x0063, #c
0x0064:0x0064, #d
0x0065:0x0065, #e
0x0066:0x0066, #f
0x0067:0x0067, #g
0x0068:0x0068, #h
0x0069:0x0069, #i
0x006a:0x006a, #j
0x006b:0x006b, #k
0x006c:0x006c, #l
0x006d:0x006d, #m
0x006e:0x006e, #n
0x006f:0x006f, #o
0x0070:0x0070, #p
0x0071:0x0071, #q
0x0072:0x0072, #r
0x0073:0x0073, #s
0x0074:0x0074, #t
0x0075:0x0075, #u
0x0076:0x0076, #v
0x0077:0x0077, #w
0x0078:0x0078, #x
0x0079:0x0079, #y
0x007a:0x007a, #z
0x007b:0x007b, #{
0x007c:0x007c, #|
0x007d:0x007d, #}
0x007e:0x007e, #~
0x007f:0x007f, #del
0x0080:0x0080, #LATIN CAPITAL LETTER C WITH CEDILLA
0x0081:0x0081, #LATIN SMALL LETTER U WITH DIAERESIS
0x0082:0x0082, #LATIN SMALL LETTER E WITH ACUTE
0x0083:0x0083, #LATIN SMALL LETTER A WITH CIRCUMFLEX
0x0084:0x0084, #LATIN SMALL LETTER A WITH DIAERESIS
0x0085:0x0085, #LATIN SMALL LETTER U WITH RING ABOVE
0x0086:0x0086, #LATIN SMALL LETTER C WITH ACUTE
0x0087:0x0087, #LATIN SMALL LETTER C WITH CEDILLA
0x0088:0x0088, #LATIN SMALL LETTER L WITH STROKE
0x0089:0x0089, #LATIN SMALL LETTER E WITH DIAERESIS
0x008a:0x008a, #LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
0x008b:0x008b, #LATIN SMALL LETTER O WITH DOUBLE ACUTE
0x008c:0x008c, #LATIN SMALL LETTER I WITH CIRCUMFLEX
0x008d:0x008d, #LATIN CAPITAL LETTER Z WITH ACUTE
0x008e:0x008e, #LATIN CAPITAL LETTER A WITH DIAERESIS
0x008f:0x008f, #LATIN CAPITAL LETTER C WITH ACUTE
0x0090:0x0090, #LATIN CAPITAL LETTER E WITH ACUTE
0x0091:0x0091, #LATIN CAPITAL LETTER L WITH ACUTE
0x0092:0x0092, #LATIN SMALL LETTER L WITH ACUTE
0x0093:0x0093, #LATIN SMALL LETTER O WITH CIRCUMFLEX
0x0094:0x0094, #LATIN SMALL LETTER O WITH DIAERESIS
0x0095:0x0095, #LATIN CAPITAL LETTER L WITH CARON
0x0096:0x0096, #LATIN SMALL LETTER L WITH CARON
0x0097:0x0097, #LATIN CAPITAL LETTER S WITH ACUTE
0x0098:0x0098, #LATIN SMALL LETTER S WITH ACUTE
0x0099:0x0099, #LATIN CAPITAL LETTER O WITH DIAERESIS
0x009a:0x009a, #LATIN CAPITAL LETTER U WITH DIAERESIS
0x009b:0x009b, #LATIN CAPITAL LETTER T WITH CARON
0x009c:0x009c, #LATIN SMALL LETTER T WITH CARON
0x009d:0x009d, #LATIN CAPITAL LETTER L WITH STROKE
0x009e:0x009e, #MULTIPLICATION SIGN
0x009f:0x009f, #LATIN SMALL LETTER C WITH CARON
0x00a0:0x00a0, #LATIN SMALL LETTER A WITH ACUTE
0x00a1:0x00a1, #LATIN SMALL LETTER I WITH ACUTE
0x00a2:0x00a2, #LATIN SMALL LETTER O WITH ACUTE
0x00a3:0x00a3, #LATIN SMALL LETTER U WITH ACUTE
0x00a4:0x00a4, #LATIN CAPITAL LETTER A WITH OGONEK
0x00a5:0x00a5, #LATIN SMALL LETTER A WITH OGONEK
0x00a6:0x00a6, #LATIN CAPITAL LETTER Z WITH CARON
0x00a7:0x00a7, #LATIN SMALL LETTER Z WITH CARON
0x00a8:0x00a8, #LATIN CAPITAL LETTER E WITH OGONEK
0x00a9:0x00a9, #LATIN SMALL LETTER E WITH OGONEK
0x00aa:0x00aa, #NOT SIGN
0x00ab:0x00ab, #LATIN SMALL LETTER Z WITH ACUTE
0x00ac:0x00ac, #LATIN CAPITAL LETTER C WITH CARON
0x00ad:0x00ad, #LATIN SMALL LETTER S WITH CEDILLA
0x00ae:0x00ae, #LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
0x00af:0x00af, #RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
0x00b0:0x00b0, #LIGHT SHADE
0x00b1:0x00b1, #MEDIUM SHADE
0x00b2:0x00b2, #DARK SHADE
0x00b3:0x00b3, #BOX DRAWINGS LIGHT VERTICAL
0x00b4:0x00b4, #BOX DRAWINGS LIGHT VERTICAL AND LEFT
0x00b5:0x00b5, #LATIN CAPITAL LETTER A WITH ACUTE
0x00b6:0x00b6, #LATIN CAPITAL LETTER A WITH CIRCUMFLEX
0x00b7:0x00b7, #LATIN CAPITAL LETTER E WITH CARON
0x00b8:0x00b8, #LATIN CAPITAL LETTER S WITH CEDILLA
0x00b9:0x00b9, #BOX DRAWINGS DOUBLE VERTICAL AND LEFT
0x00ba:0x00ba, #BOX DRAWINGS DOUBLE VERTICAL
0x00bb:0x00bb, #BOX DRAWINGS DOUBLE DOWN AND LEFT
0x00bc:0x00bc, #BOX DRAWINGS DOUBLE UP AND LEFT
0x00bd:0x00bd, #LATIN CAPITAL LETTER Z WITH DOT ABOVE
0x00be:0x00be, #LATIN SMALL LETTER Z WITH DOT ABOVE
0x00bf:0x00bf, #BOX DRAWINGS LIGHT DOWN AND LEFT
0x00c0:0x00c0, #BOX DRAWINGS LIGHT UP AND RIGHT
0x00c1:0x00c1, #BOX DRAWINGS LIGHT UP AND HORIZONTAL
0x00c2:0x00c2, #BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
0x00c3:0x00c3, #BOX DRAWINGS LIGHT VERTICAL AND RIGHT
0x00c4:0x00c4, #BOX DRAWINGS LIGHT HORIZONTAL
0x00c5:0x00c5, #BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
0x00c6:0x00c6, #LATIN CAPITAL LETTER A WITH BREVE
0x00c7:0x00c7, #LATIN SMALL LETTER A WITH BREVE
0x00c8:0x00c8, #BOX DRAWINGS DOUBLE UP AND RIGHT
0x00c9:0x00c9, #BOX DRAWINGS DOUBLE DOWN AND RIGHT
0x00ca:0x00ca, #BOX DRAWINGS DOUBLE UP AND HORIZONTAL
0x00cb:0x00cb, #BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
0x00cc:0x00cc, #BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
0x00cd:0x00cd, #BOX DRAWINGS DOUBLE HORIZONTAL
0x00ce:0x00ce, #BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
0x00cf:0x00cf, #CURRENCY SIGN
0x00d0:0x00d0, #LATIN SMALL LETTER D WITH STROKE
0x00d1:0x00d1, #LATIN CAPITAL LETTER D WITH STROKE
0x00d2:0x00d2, #LATIN CAPITAL LETTER D WITH CARON
0x00d3:0x00d3, #LATIN CAPITAL LETTER E WITH DIAERESIS
0x00d4:0x00d4, #LATIN SMALL LETTER D WITH CARON
0x00d5:0x00d5, #LATIN CAPITAL LETTER N WITH CARON
0x00d6:0x00d6, #LATIN CAPITAL LETTER I WITH ACUTE
0x00d7:0x00d7, #LATIN CAPITAL LETTER I WITH CIRCUMFLEX
0x00d8:0x00d8, #LATIN SMALL LETTER E WITH CARON
0x00d9:0x00d9, #BOX DRAWINGS LIGHT UP AND LEFT
0x00da:0x00da, #BOX DRAWINGS LIGHT DOWN AND RIGHT
0x00db:0x00db, #FULL BLOCK
0x00dc:0x00dc, #LOWER HALF BLOCK
0x00dd:0x00dd, #LATIN CAPITAL LETTER T WITH CEDILLA
0x00de:0x00de, #LATIN CAPITAL LETTER U WITH RING ABOVE
0x00df:0x00df, #UPPER HALF BLOCK
0x00e0:0x00e0, #LATIN CAPITAL LETTER O WITH ACUTE
0x00e1:0x00e1, #LATIN SMALL LETTER SHARP S
0x00e2:0x00e2, #LATIN CAPITAL LETTER O WITH CIRCUMFLEX
0x00e3:0x00e3, #LATIN CAPITAL LETTER N WITH ACUTE
0x00e4:0x00e4, #LATIN SMALL LETTER N WITH ACUTE
0x00e5:0x00e5, #LATIN SMALL LETTER N WITH CARON
0x00e6:0x00e6, #LATIN CAPITAL LETTER S WITH CARON
0x00e7:0x00e7, #LATIN SMALL LETTER S WITH CARON
0x00e8:0x00e8, #LATIN CAPITAL LETTER R WITH ACUTE
0x00e9:0x00e9, #LATIN CAPITAL LETTER U WITH ACUTE
0x00ea:0x00ea, #LATIN SMALL LETTER R WITH ACUTE
0x00eb:0x00eb, #LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
0x00ec:0x00ec, #LATIN SMALL LETTER Y WITH ACUTE
0x00ed:0x00ed, #LATIN CAPITAL LETTER Y WITH ACUTE
0x00ee:0x00ee, #LATIN SMALL LETTER T WITH CEDILLA
0x00ef:0x00ef, #ACUTE ACCENT
0x00f0:0x00f0, #SOFT HYPHEN
0x00f1:0x00f1, #DOUBLE ACUTE ACCENT
0x00f2:0x00f2, #OGONEK
0x00f3:0x00f3, #CARON
0x00f4:0x00f4, #BREVE
0x00f5:0x00f5, #SECTION SIGN
0x00f6:0x00f6, #DIVISION SIGN
0x00f7:0x00f7, #CEDILLA
0x00f8:0x00f8, #DEGREE SIGN
0x00f9:0x00f9, #DIAERESIS
0x00fa:0x00fa, #DOT ABOVE
0x00fb:0x00fb, #LATIN SMALL LETTER U WITH DOUBLE ACUTE
0x00fc:0x00fc, #LATIN CAPITAL LETTER R WITH CARON
0x00fd:0x00fd, #LATIN SMALL LETTER R WITH CARON
0x00fe:0x00fe, #BLACK SQUARE
0x00ff:0x00ff, #NO-BREAK SPACE
}

### Encoding (for outgoing edifact) ###############################
encoding_map = {
0x0000:0x0000, #NUL
0x0001:0x0001, #SOH
0x0002:0x0002, #STX
0x0003:0x0003, #ETX
0x0004:0x0004, #EOT
0x0005:0x0005, #ENQ
0x0006:0x0006, #ACK
0x0007:0x0007, #Bell
0x0008:0x0008, #BackSpace
0x0009:0x0009, #Tab
0x000a:0x000a, #lf
0x000b:0x000b, #Vertical Tab
0x000c:0x000c, #FormFeed
0x000d:0x000d, #cr
0x000e:0x000e, #SO
0x000f:0x000f, #SI
0x0010:0x0010, #DLE
0x0011:0x0011, #DC1
0x0012:0x0012, #DC2
0x0013:0x0013, #DC3
0x0014:0x0014, #DC4
0x0015:0x0015, #NAK
0x0016:0x0016, #SYN
0x0017:0x0017, #ETB
0x0018:0x0018, #CAN
0x0019:0x0019, #EM
0x001a:0x001a, #SUB, cntrl-Z
0x001b:0x001b, #ESC
0x001c:0x001c, #FS
0x001d:0x001d, #GS
0x001e:0x001e, #RS
0x001f:0x001f, #US
0x0020:0x0020, #<space>
0x0021:0x0021, #!
0x0022:0x0022, #"
0x0023:0x0023, ##
0x0024:0x0024, #$
0x0025:0x0025, #%
0x0026:0x0026, #&
0x0027:0x0027, #'
0x0028:0x0028, #(
0x0029:0x0029, #)
0x002a:0x002a, #*
0x002b:0x002b, #+
0x002c:0x002c, #,
0x002d:0x002d, #-
0x002e:0x002e, #.
0x002f:0x002f, #/
0x0030:0x0030, #0
0x0031:0x0031, #1
0x0032:0x0032, #2
0x0033:0x0033, #3
0x0034:0x0034, #4
0x0035:0x0035, #5
0x0036:0x0036, #6
0x0037:0x0037, #7
0x0038:0x0038, #8
0x0039:0x0039, #9
0x003a:0x003a, #:
0x003b:0x003b, #;
0x003c:0x003c, #<
0x003d:0x003d, #=
0x003e:0x003e, #>
0x003f:0x003f, #?
0x0040:0x0040, #@
0x0041:0x0041, #A
0x0042:0x0042, #B
0x0043:0x0043, #C
0x0044:0x0044, #D
0x0045:0x0045, #E
0x0046:0x0046, #F
0x0047:0x0047, #G
0x0048:0x0048, #H
0x0049:0x0049, #I
0x004a:0x004a, #J
0x004b:0x004b, #K
0x004c:0x004c, #L
0x004d:0x004d, #M
0x004e:0x004e, #N
0x004f:0x004f, #O
0x0050:0x0050, #P
0x0051:0x0051, #Q
0x0052:0x0052, #R
0x0053:0x0053, #S
0x0054:0x0054, #T
0x0055:0x0055, #U
0x0056:0x0056, #V
0x0057:0x0057, #W
0x0058:0x0058, #X
0x0059:0x0059, #Y
0x005a:0x005a, #Z
0x005b:0x005b, #[
0x005c:0x005c, #\\
0x005d:0x005d, #]
0x005e:0x005e, #^
0x005f:0x005f, #_
0x0060:0x0060, #`
0x0061:0x0061, #a
0x0062:0x0062, #b
0x0063:0x0063, #c
0x0064:0x0064, #d
0x0065:0x0065, #e
0x0066:0x0066, #f
0x0067:0x0067, #g
0x0068:0x0068, #h
0x0069:0x0069, #i
0x006a:0x006a, #j
0x006b:0x006b, #k
0x006c:0x006c, #l
0x006d:0x006d, #m
0x006e:0x006e, #n
0x006f:0x006f, #o
0x0070:0x0070, #p
0x0071:0x0071, #q
0x0072:0x0072, #r
0x0073:0x0073, #s
0x0074:0x0074, #t
0x0075:0x0075, #u
0x0076:0x0076, #v
0x0077:0x0077, #w
0x0078:0x0078, #x
0x0079:0x0079, #y
0x007a:0x007a, #z
0x007b:0x007b, #{
0x007c:0x007c, #|
0x007d:0x007d, #}
0x007e:0x007e, #~
0x007f:0x007f, #del
0x0080:0x0080, #LATIN CAPITAL LETTER C WITH CEDILLA
0x0081:0x0081, #LATIN SMALL LETTER U WITH DIAERESIS
0x0082:0x0082, #LATIN SMALL LETTER E WITH ACUTE
0x0083:0x0083, #LATIN SMALL LETTER A WITH CIRCUMFLEX
0x0084:0x0084, #LATIN SMALL LETTER A WITH DIAERESIS
0x0085:0x0085, #LATIN SMALL LETTER U WITH RING ABOVE
0x0086:0x0086, #LATIN SMALL LETTER C WITH ACUTE
0x0087:0x0087, #LATIN SMALL LETTER C WITH CEDILLA
0x0088:0x0088, #LATIN SMALL LETTER L WITH STROKE
0x0089:0x0089, #LATIN SMALL LETTER E WITH DIAERESIS
0x008a:0x008a, #LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
0x008b:0x008b, #LATIN SMALL LETTER O WITH DOUBLE ACUTE
0x008c:0x008c, #LATIN SMALL LETTER I WITH CIRCUMFLEX
0x008d:0x008d, #LATIN CAPITAL LETTER Z WITH ACUTE
0x008e:0x008e, #LATIN CAPITAL LETTER A WITH DIAERESIS
0x008f:0x008f, #LATIN CAPITAL LETTER C WITH ACUTE
0x0090:0x0090, #LATIN CAPITAL LETTER E WITH ACUTE
0x0091:0x0091, #LATIN CAPITAL LETTER L WITH ACUTE
0x0092:0x0092, #LATIN SMALL LETTER L WITH ACUTE
0x0093:0x0093, #LATIN SMALL LETTER O WITH CIRCUMFLEX
0x0094:0x0094, #LATIN SMALL LETTER O WITH DIAERESIS
0x0095:0x0095, #LATIN CAPITAL LETTER L WITH CARON
0x0096:0x0096, #LATIN SMALL LETTER L WITH CARON
0x0097:0x0097, #LATIN CAPITAL LETTER S WITH ACUTE
0x0098:0x0098, #LATIN SMALL LETTER S WITH ACUTE
0x0099:0x0099, #LATIN CAPITAL LETTER O WITH DIAERESIS
0x009a:0x009a, #LATIN CAPITAL LETTER U WITH DIAERESIS
0x009b:0x009b, #LATIN CAPITAL LETTER T WITH CARON
0x009c:0x009c, #LATIN SMALL LETTER T WITH CARON
0x009d:0x009d, #LATIN CAPITAL LETTER L WITH STROKE
0x009e:0x009e, #MULTIPLICATION SIGN
0x009f:0x009f, #LATIN SMALL LETTER C WITH CARON
0x00a0:0x00a0, #LATIN SMALL LETTER A WITH ACUTE
0x00a1:0x00a1, #LATIN SMALL LETTER I WITH ACUTE
0x00a2:0x00a2, #LATIN SMALL LETTER O WITH ACUTE
0x00a3:0x00a3, #LATIN SMALL LETTER U WITH ACUTE
0x00a4:0x00a4, #LATIN CAPITAL LETTER A WITH OGONEK
0x00a5:0x00a5, #LATIN SMALL LETTER A WITH OGONEK
0x00a6:0x00a6, #LATIN CAPITAL LETTER Z WITH CARON
0x00a7:0x00a7, #LATIN SMALL LETTER Z WITH CARON
0x00a8:0x00a8, #LATIN CAPITAL LETTER E WITH OGONEK
0x00a9:0x00a9, #LATIN SMALL LETTER E WITH OGONEK
0x00aa:0x00aa, #NOT SIGN
0x00ab:0x00ab, #LATIN SMALL LETTER Z WITH ACUTE
0x00ac:0x00ac, #LATIN CAPITAL LETTER C WITH CARON
0x00ad:0x00ad, #LATIN SMALL LETTER S WITH CEDILLA
0x00ae:0x00ae, #LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
0x00af:0x00af, #RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
0x00b0:0x00b0, #LIGHT SHADE
0x00b1:0x00b1, #MEDIUM SHADE
0x00b2:0x00b2, #DARK SHADE
0x00b3:0x00b3, #BOX DRAWINGS LIGHT VERTICAL
0x00b4:0x00b4, #BOX DRAWINGS LIGHT VERTICAL AND LEFT
0x00b5:0x00b5, #LATIN CAPITAL LETTER A WITH ACUTE
0x00b6:0x00b6, #LATIN CAPITAL LETTER A WITH CIRCUMFLEX
0x00b7:0x00b7, #LATIN CAPITAL LETTER E WITH CARON
0x00b8:0x00b8, #LATIN CAPITAL LETTER S WITH CEDILLA
0x00b9:0x00b9, #BOX DRAWINGS DOUBLE VERTICAL AND LEFT
0x00ba:0x00ba, #BOX DRAWINGS DOUBLE VERTICAL
0x00bb:0x00bb, #BOX DRAWINGS DOUBLE DOWN AND LEFT
0x00bc:0x00bc, #BOX DRAWINGS DOUBLE UP AND LEFT
0x00bd:0x00bd, #LATIN CAPITAL LETTER Z WITH DOT ABOVE
0x00be:0x00be, #LATIN SMALL LETTER Z WITH DOT ABOVE
0x00bf:0x00bf, #BOX DRAWINGS LIGHT DOWN AND LEFT
0x00c0:0x00c0, #BOX DRAWINGS LIGHT UP AND RIGHT
0x00c1:0x00c1, #BOX DRAWINGS LIGHT UP AND HORIZONTAL
0x00c2:0x00c2, #BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
0x00c3:0x00c3, #BOX DRAWINGS LIGHT VERTICAL AND RIGHT
0x00c4:0x00c4, #BOX DRAWINGS LIGHT HORIZONTAL
0x00c5:0x00c5, #BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
0x00c6:0x00c6, #LATIN CAPITAL LETTER A WITH BREVE
0x00c7:0x00c7, #LATIN SMALL LETTER A WITH BREVE
0x00c8:0x00c8, #BOX DRAWINGS DOUBLE UP AND RIGHT
0x00c9:0x00c9, #BOX DRAWINGS DOUBLE DOWN AND RIGHT
0x00ca:0x00ca, #BOX DRAWINGS DOUBLE UP AND HORIZONTAL
0x00cb:0x00cb, #BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
0x00cc:0x00cc, #BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
0x00cd:0x00cd, #BOX DRAWINGS DOUBLE HORIZONTAL
0x00ce:0x00ce, #BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
0x00cf:0x00cf, #CURRENCY SIGN
0x00d0:0x00d0, #LATIN SMALL LETTER D WITH STROKE
0x00d1:0x00d1, #LATIN CAPITAL LETTER D WITH STROKE
0x00d2:0x00d2, #LATIN CAPITAL LETTER D WITH CARON
0x00d3:0x00d3, #LATIN CAPITAL LETTER E WITH DIAERESIS
0x00d4:0x00d4, #LATIN SMALL LETTER D WITH CARON
0x00d5:0x00d5, #LATIN CAPITAL LETTER N WITH CARON
0x00d6:0x00d6, #LATIN CAPITAL LETTER I WITH ACUTE
0x00d7:0x00d7, #LATIN CAPITAL LETTER I WITH CIRCUMFLEX
0x00d8:0x00d8, #LATIN SMALL LETTER E WITH CARON
0x00d9:0x00d9, #BOX DRAWINGS LIGHT UP AND LEFT
0x00da:0x00da, #BOX DRAWINGS LIGHT DOWN AND RIGHT
0x00db:0x00db, #FULL BLOCK
0x00dc:0x00dc, #LOWER HALF BLOCK
0x00dd:0x00dd, #LATIN CAPITAL LETTER T WITH CEDILLA
0x00de:0x00de, #LATIN CAPITAL LETTER U WITH RING ABOVE
0x00df:0x00df, #UPPER HALF BLOCK
0x00e0:0x00e0, #LATIN CAPITAL LETTER O WITH ACUTE
0x00e1:0x00e1, #LATIN SMALL LETTER SHARP S
0x00e2:0x00e2, #LATIN CAPITAL LETTER O WITH CIRCUMFLEX
0x00e3:0x00e3, #LATIN CAPITAL LETTER N WITH ACUTE
0x00e4:0x00e4, #LATIN SMALL LETTER N WITH ACUTE
0x00e5:0x00e5, #LATIN SMALL LETTER N WITH CARON
0x00e6:0x00e6, #LATIN CAPITAL LETTER S WITH CARON
0x00e7:0x00e7, #LATIN SMALL LETTER S WITH CARON
0x00e8:0x00e8, #LATIN CAPITAL LETTER R WITH ACUTE
0x00e9:0x00e9, #LATIN CAPITAL LETTER U WITH ACUTE
0x00ea:0x00ea, #LATIN SMALL LETTER R WITH ACUTE
0x00eb:0x00eb, #LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
0x00ec:0x00ec, #LATIN SMALL LETTER Y WITH ACUTE
0x00ed:0x00ed, #LATIN CAPITAL LETTER Y WITH ACUTE
0x00ee:0x00ee, #LATIN SMALL LETTER T WITH CEDILLA
0x00ef:0x00ef, #ACUTE ACCENT
0x00f0:0x00f0, #SOFT HYPHEN
0x00f1:0x00f1, #DOUBLE ACUTE ACCENT
0x00f2:0x00f2, #OGONEK
0x00f3:0x00f3, #CARON
0x00f4:0x00f4, #BREVE
0x00f5:0x00f5, #SECTION SIGN
0x00f6:0x00f6, #DIVISION SIGN
0x00f7:0x00f7, #CEDILLA
0x00f8:0x00f8, #DEGREE SIGN
0x00f9:0x00f9, #DIAERESIS
0x00fa:0x00fa, #DOT ABOVE
0x00fb:0x00fb, #LATIN SMALL LETTER U WITH DOUBLE ACUTE
0x00fc:0x00fc, #LATIN CAPITAL LETTER R WITH CARON
0x00fd:0x00fd, #LATIN SMALL LETTER R WITH CARON
0x00fe:0x00fe, #BLACK SQUARE
0x00ff:0x00ff, #NO-BREAK SPACE
}
