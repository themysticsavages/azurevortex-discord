import random
import re

def toxify(text):
    textlist = list(text)
    i = 0
    fn = 0
    cased = []
    for chars in textlist:
        if fn == 0:
            cased.append(str(text[i]).lower())
            fn += 1
        if fn == 1:
            cased.append(str(text)[i].upper())
            fn -= 1
        i += 1
    return ''.join(cased)+'!!111!!1 👏👏👏'

def memify(text):
    insensitive = re.compile(re.escape('b'), re.IGNORECASE)
    memed = insensitive.sub(':b:', text)
    return memed+' 😳💯'

def blockify(text):
    return f'▅▆▇▉ 🔥 {text} 🔥 ▉▇▆▅'