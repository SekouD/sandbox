
# coding: utf-8

# In[1]:

import re
from bisect import bisect_left


# In[2]:

def search(List, len_list, entry):
    index = bisect_left(List, entry, 0, len_list)
    return(True if index != len_list and List[index] == entry else False)


# class SylComponents:
#     '''
#     takes a syllable as input
#     outputs:
#         (prefix+main-stack, vowel+suffixes)
#         (exceptions, x) 
#         a list of solutions if there is more than one
#         None if the syllable is not wellformed
#     '''
# 
#     def __init__(self):
#         # roots is an import from root + rareC and wazurC and suffixes is the 'AB' entry from  suffixes.json
#         # all dicts from https://github.com/eroux/tibetan-spellchecker/tree/master/syllables
#         Aroots  = ['ཀ', 'ཀྱ', 'ཀྲ', 'ཀླ', 'ཁ', 'ཁྱ', 'ཁྲ', 'ག', 'གཏྲ', 'གྱ', 'གྲ', 'གླ', 'ང', 'ཅ', 'ཆ', 'ཇ', 'ཉ', 'ཏ', 'ཏྲ', 'ཐ', 'ཐྲ', 'ད', 'དཀྱ', 'དཀྲ', 'དཀླ', 'དགྱ', 'དགྲ', 'དཔྱ', 'དཔྲ', 'དབྱ', 'དབྲ', 'དམྱ', 'དམྲ', 'དྲ', 'ན', 'པ', 'པྱ', 'པྲ', 'ཕ', 'ཕྱ', 'ཕྲ', 'བ', 'བཀྱ', 'བཀྲ', 'བཀླ', 'བགྱ', 'བགྲ', 'བཏྲ', 'བཟླ', 'བརྐ', 'བརྐྱ', 'བརྒ', 'བརྒྱ', 'བརྔ', 'བརྗ', 'བརྙ', 'བརྟ', 'བརྡ', 'བརྣ', 'བརྩ', 'བརྫ', 'བརླ', 'བལྟ', 'བལྡ', 'བསྐ', 'བསྐྱ', 'བསྐྲ', 'བསྒ', 'བསྒྱ', 'བསྒྲ', 'བསྔ', 'བསྙ', 'བསྟ', 'བསྡ', 'བསྣ', 'བསྩ', 'བསྲ', 'བསླ', 'བྱ', 'བྲ', 'བླ', 'མ', 'མཁྱ', 'མཁྲ', 'མགྱ', 'མགྲ', 'མྱ', 'མྲ', 'ཙ', 'ཚ', 'ཛ', 'ཝ', 'ཞ', 'ཟ', 'ཟླ', 'འ', 'འཁྱ', 'འཁྲ', 'འགྱ', 'འགྲ', 'འདྲ', 'འཕྱ', 'འཕྲ', 'འབྱ', 'འབྲ', 'ཡ', 'ར', 'རྐ', 'རྐྱ', 'རྒ', 'རྒྱ', 'རྔ', 'རྗ', 'རྙ', 'རྟ', 'རྡ', 'རྣ', 'རྦ', 'རྨ', 'རྨྱ', 'རྩ', 'རྫ', 'རླ', 'ལ', 'ལྐ', 'ལྒ', 'ལྔ', 'ལྕ', 'ལྗ', 'ལྟ', 'ལྡ', 'ལྤ', 'ལྦ', 'ལྷ', 'ཤ', 'ས', 'སྐ', 'སྐྱ', 'སྐྲ', 'སྒ', 'སྒྱ', 'སྒྲ', 'སྔ', 'སྙ', 'སྟ', 'སྡ', 'སྣ', 'སྣྲ', 'སྤ', 'སྤྱ', 'སྤྲ', 'སྦ', 'སྦྱ', 'སྦྲ', 'སྨ', 'སྨྱ', 'སྨྲ', 'སྩ', 'སྲ', 'སླ', 'ཧ', 'ཧྲ', 'ཨ']
#         NBroots = ['གཅ', 'གཉ', 'གཏ', 'གད', 'གན', 'གཙ', 'གཞ', 'གཟ', 'གཡ', 'གཤ', 'གས', 'དཀ', 'དག', 'དང', 'དཔ', 'དབ', 'དམ', 'བཀ', 'བག', 'བཅ', 'བཏ', 'བད', 'བཙ', 'བཞ', 'བཟ', 'བཤ', 'བས', 'མཁ', 'མག', 'མང', 'མཆ', 'མཇ', 'མཉ', 'མཐ', 'མད', 'མན', 'མཚ', 'མཛ', 'འཁ', 'འག', 'འཆ', 'འཇ', 'འཐ', 'འད', 'འཕ', 'འབ', 'འཚ', 'འཛ']
#         Croots  = ['ཀའུ', 'ཀིའུ', 'ཀེའུ', 'ཀོའུ', 'ཀྭ', 'ཀྭའི', 'ཀྲུའུ', 'ཁེའུ', 'ཁྭ', 'ཁྱིའུ', 'ཁྱེའུ', 'ཁྲིའུ', 'ཁྲུའུ', 'ཁྲེའུ', 'གཅིའུ', 'གཅེའུ', 'གཏེའུ', 'གཙེའུ', 'གཞུའུ', 'གའུ', 'གཡིའུ', 'གྭ', 'གྲིའུ', 'གྲེའུ', 'གྲྭ', 'གླེའུ', 'ཉེའུ', 'ཉྭ', 'ཏེའུ', 'ཐིའུ', 'ཐུའུ', 'ཐེའུ', 'ཐོའུ', 'དཔེའུ', 'དུའུ', 'དེའུ', 'དྭ', 'དྭོ', 'དྲེའུ', 'དྲྭ', 'ནའུ', 'ནེའུ', 'ནོའུ', 'པདྨ', 'ཕེའུ', 'ཕྱྭ', 'ཕྲའུ', 'ཕྲེའུ', 'བསེའུ', 'བསྭ', 'བསྭོ', 'བེའུ', 'བྱའུ', 'བྱིའུ', 'བྱེའུ', 'བྲའུ', 'བྲའོ', 'བྲེའུ', 'བྲོའུ', 'མཐེའུ', 'མདེའུ', 'མཚེའུ', 'མིའུ', 'མུའུ', 'མོའུ', 'མྱིའུ', 'ཙིའུ', 'ཙེའུ', 'ཚའུ', 'ཚུའུ', 'ཚེའུ', 'ཚྭ', 'ཞྭ', 'ཟེའུ', 'ཟྭ', 'འགིའུ', 'འགོའུ', 'འཕེའུ', 'འབེའུ', 'ཡེའུ', 'རེའུ', 'རྒེའུ', 'རྔེའུ', 'རྗེའུ', 'རྟའུ', 'རྟེའུ', 'རྡེའུ', 'རྨེའུ', 'རྩེའུ', 'རྩྭ', 'རྫིའུ', 'རྫེའུ', 'རྭ', 'ལའུ', 'ལིའུ', 'ལེའུ', 'ལོའུ', 'ལྕེའུ', 'ལྭ', 'ཤའུ', 'ཤེའུ', 'ཤྭ', 'སིའུ', 'སེའུ', 'སྒའུ', 'སྒེའུ', 'སྒྱེའུ', 'སྒྲེའུ', 'སྔེའུ', 'སྙེའུ', 'སྟེའུ', 'སྟྭ', 'སྡེའུ', 'སྣེའུ', 'སྤའུ', 'སྤེའུ', 'སྤྱིའུ', 'སྤྲེའུ', 'སྦྲེའུ', 'སྨེའུ', 'སྭ', 'སྲིའུ', 'སླེའུ', 'སླེའོ', 'ཧུའུ', 'ཧེའུ', 'ཧྭ', 'ཧྲུའུ']
#         self.Aroots = sorted(Aroots)
#         self.NBroots = sorted(NBroots)
#         self.Croots = sorted(Croots)
#         
#         suffixes =      ['ག', 'གས', 'ང', 'ངས', 'ད', 'ན', 'བ', 'བས', 'མ', 'མས', 'ལ', 'འི', 'འོ', 'འང', 'འམ', 'ར', 'ས',
#                      'ི', 'ིག', 'ིགས', 'ིང', 'ིངས', 'ིད', 'ིན', 'ིབ', 'ིབས', 'ིམ', 'ིམས', 'ིལ', 'ིའི', 'ིའོ', 'ིའང', 'ིའམ', 'ིར', 'ིས',
#                      'ུ', 'ུག', 'ུགས', 'ུང', 'ུངས', 'ུད', 'ུན', 'ུབ', 'ུབས', 'ུམ', 'ུམས', 'ུལ', 'ུའི', 'ུའོ', 'ུའང', 'ུའམ', 'ུར', 'ུས',
#                      'ེ', 'ེག', 'ེགས', 'ེང', 'ེངས', 'ེད', 'ེན', 'ེབ', 'ེབས', 'ེམ', 'ེམས', 'ེལ', 'ེའི', 'ེའོ', 'ེའང', 'ེའམ', 'ེར', 'ེས',
#                      'ོ', 'ོག', 'ོགས', 'ོང', 'ོངས', 'ོད', 'ོན', 'ོབ', 'ོབས', 'ོམ', 'ོམས', 'ོལ', 'ོའི', 'ོའོ', 'ོའང', 'ོའམ', 'ོར', 'ོས']
#         self.Asuffixes = sorted(['འ'] + suffixes)
#         self.NBsuffixes = sorted([''] + suffixes)
#         self.Csuffixes =  sorted(['','འི', 'འོ', 'འང', 'འམ', 'ར', 'ས'])
#         
#         special = ['བགླ', 'མདྲོན', 'བརྡའ', 'བརྟའ']
#         wazurs = ['ཧྭག', 'ཀྭས', 'ཁྭངས', 'ཧྭང', 'ཀྭན', 'དྭགས', 'ཧྭགས', 'དྭངས', 'ཏྭོན']
#         self.exceptions = sorted(special + wazurs)
#         self.ambiguous = {'མངས' : ('མ', 'ངས'), 'མགས' : ('མ', 'གས'), 'དབས' : ('ད', 'བས'), 'དངས' : ('ད', 'ངས'), 'དགས' : ('དག', 'ས'), 'དམས' : ('དམ', 'ས'), 'བགས' : ('བ', 'གས'), 'འབས' : ('འབ', 'ས'), 'འགས' : ('འག', 'ས')}
#         
#         self.len_Aroots = len(self.Aroots)
#         self.len_NBroots = len(self.NBroots)
#         self.len_Croots = len(self.Croots)
#         self.len_Asuffixes = len(self.Asuffixes)
#         self.len_NBsuffixes = len(self.NBsuffixes)
#         self.len_Csuffixes = len(self.Csuffixes)
#         self.len_exceptions = len(self.exceptions)    
#         
#     def get(self, syl):
#         solutions = []
#         if search(self.exceptions, self.len_exceptions, syl):
#             solutions.append((syl, 'x'))
#         elif syl in self.ambiguous:
#             solutions.append(self.ambiguous[syl])
#         else:
#             for i in range(1, len(syl)+1):
#                 if len(syl) > i+1 and syl[i+1] not in ('ག', 'ང', 'ད', 'ན', 'བ', 'མ', 'འ', 'ར', 'ལ', 'ས', 'ི', 'ུ', 'ེ', 'ོ'): continue
# 
#                 if search(self.Aroots, self.len_Aroots, syl) or search(self.NBroots, self.len_NBroots, syl) or search(self.Croots, self.len_Croots, syl):
#                     if (syl, '') not in solutions:
#                         solutions.append((syl, ''))
#                 else:
#                     root = syl[0:i]
#                     suf = syl[i:]
#                     if (search(self.Asuffixes, self.len_Asuffixes, suf) and search(self.Aroots, self.len_Aroots, root)) or (search(self.NBroots, self.len_NBroots, root) and search(self.NBsuffixes, self.len_NBsuffixes, suf)) or (search(self.Csuffixes, self.len_Csuffixes, suf) and search(self.Croots, self.len_Croots, root)):
#                         if (root, suf) not in solutions:
#                             solutions.append((root, suf))
# 
#         if len(solutions) > 1:
#             return solutions
#         if len(solutions) == 1:
#             return solutions[0]
#         if solutions == []:
#             return None

# In[14]:

class SylComponents:
    '''
    takes a syllable as input
    outputs:
        (prefix+main-stack, vowel+suffixes)
        (exceptions, x) 
        a list of solutions if there is more than one
        None if the syllable is not wellformed
    '''

    def __init__(self):
        # roots is an import from root + rareC and wazurC and suffixes is the 'AB' entry from  suffixes.json
        self.roots = {'ཀ' : 'A', 'ཀྱ' : 'A', 'ཀྲ' : 'A', 'ཀླ' : 'A', 'དཀ' : 'NB', 'དཀྱ' : 'A', 'དཀྲ' : 'A', 'དཀླ' : 'A', 'བཀ' : 'NB', 'བཀྱ' : 'A', 'བཀྲ' : 'A', 'བཀླ' : 'A', 'རྐ' : 'A', 'རྐྱ' : 'A', 'ལྐ' : 'A', 'སྐ' : 'A', 'སྐྱ' : 'A', 'སྐྲ' : 'A', 'བརྐ' : 'A', 'བརྐྱ' : 'A', 'བསྐ' : 'A', 'བསྐྱ' : 'A', 'བསྐྲ' : 'A', 'ཀའུ' : 'C', 'ཀིའུ' : 'C', 'ཀེའུ' : 'C', 'ཀོའུ' : 'C', 'ཀྲུའུ' : 'C', 'ཀྭའི': 'C',  'ཀྭ': 'C', 'ཀརྨ' : 'C',
                 'ཁ' : 'A', 'ཁྱ' : 'A', 'ཁྲ' : 'A', 'མཁ' : 'NB', 'མཁྱ' : 'A', 'མཁྲ' : 'A', 'འཁ' : 'NB', 'འཁྱ' : 'A', 'འཁྲ' : 'A', 'ཁེའུ' : 'C', 'ཁྱིའུ' : 'C', 'ཁྱེའུ' : 'C', 'ཁྲིའུ' : 'C', 'ཁྲུའུ' : 'C', 'ཁྲེའུ' : 'C', 'ཁྭ': 'C',  
                 'ག' : 'A', 'གྱ' : 'A', 'གྲ' : 'A', 'གླ' : 'A', 'དག' : 'NB', 'དགྱ' : 'A', 'དགྲ' : 'A', 'བག' : 'NB', 'བགྱ' : 'A', 'བགྲ' : 'A', 'མག' : 'NB', 'མགྱ' : 'A', 'མགྲ' : 'A', 'འག' : 'NB', 'འགྱ' : 'A', 'འགྲ' : 'A', 'རྒ' : 'A', 'རྒྱ' : 'A', 'ལྒ' : 'A', 'སྒ' : 'A', 'སྒྱ' : 'A', 'སྒྲ' : 'A', 'བརྒ' : 'A', 'བརྒྱ' : 'A', 'བསྒ' : 'A', 'བསྒྱ' : 'A', 'བསྒྲ' : 'A', 'གའུ' : 'C', 'གྲིའུ' : 'C', 'གྲེའུ' : 'C', 'གླེའུ' : 'C', 'འགིའུ' : 'C', 'འགོའུ' : 'C', 'རྒེའུ' : 'C', 'སྒའུ' : 'C', 'སྒེའུ' : 'C', 'སྒྱེའུ' : 'C', 'སྒྲེའུ' : 'C', 'གྭ': 'C',  'གྲྭ': 'C',
                 'ང' : 'A', 'དང' : 'NB', 'མང' : 'NB', 'རྔ' : 'A', 'ལྔ' : 'A', 'སྔ' : 'A', 'བརྔ' : 'A', 'བསྔ' : 'A', 'རྔེའུ' : 'C', 'སྔེའུ' : 'C', 
                 'ཅ' : 'A', 'གཅ' : 'NB', 'བཅ' : 'NB', 'ལྕ' : 'A', 'གཅིའུ' : 'C', 'གཅེའུ' : 'C', 'ལྕེའུ' : 'C', 
                 'ཆ' : 'A', 'མཆ' : 'NB', 'འཆ' : 'NB', 
                 'ཇ' : 'A', 'མཇ' : 'NB', 'འཇ' : 'NB', 'རྗ' : 'A', 'ལྗ' : 'A', 'བརྗ' : 'A', 'རྗེའུ' : 'C', 
                 'ཉ' : 'A', 'གཉ' : 'NB', 'མཉ' : 'NB', 'རྙ' : 'A', 'སྙ' : 'A', 'བརྙ' : 'A', 'བསྙ' : 'A', 'ཉེའུ' : 'C', 'སྙེའུ' : 'C', 'ཉྭ': 'C',  
                 'ཏ' : 'A', 'ཏྲ' : 'A', 'གཏ' : 'NB', 'གཏྲ' : 'A', 'བཏ' : 'NB', 'བཏྲ' : 'A', 'རྟ' : 'A', 'ལྟ' : 'A', 'སྟ' : 'A', 'བརྟ' : 'A', 'བལྟ' : 'A', 'བསྟ' : 'A', 'ཏེའུ' : 'C', 'གཏེའུ' : 'C', 'རྟའུ' : 'C', 'རྟེའུ' : 'C', 'སྟེའུ' : 'C', 'སྟྭ': 'C',  
                 'ཐ' : 'A', 'ཐྲ' : 'A', 'མཐ' : 'NB', 'འཐ' : 'NB', 'ཐིའུ' : 'C', 'ཐུའུ' : 'C', 'ཐེའུ' : 'C', 'ཐོའུ' : 'C', 'མཐེའུ' : 'C', 
                 'ད' : 'A', 'དྲ' : 'A', 'གད' : 'NB', 'བད' : 'NB', 'མད' : 'NB', 'འད' : 'NB', 'འདྲ' : 'A', 'རྡ' : 'A', 'ལྡ' : 'A', 'སྡ' : 'A', 'བརྡ' : 'A', 'བལྡ' : 'A', 'བསྡ' : 'A', 'དུའུ' : 'C', 'དེའུ' : 'C', 'དྲེའུ' : 'C', 'མདེའུ' : 'C', 'རྡེའུ' : 'C', 'སྡེའུ' : 'C', 'དྲྭ': 'C',  'དྭ': 'C',  'དྭོ': 'C',  
                 'ན' : 'A', 'གན' : 'NB', 'མན' : 'NB', 'རྣ' : 'A', 'སྣ' : 'A', 'སྣྲ' : 'A', 'བརྣ' : 'A', 'བསྣ' : 'A', 'ནའུ' : 'C', 'ནེའུ' : 'C', 'ནོའུ' : 'C', 'སྣེའུ' : 'C', 
                 'པ' : 'A', 'པྱ' : 'A', 'པྲ' : 'A', 'དཔ' : 'NB', 'དཔྱ' : 'A', 'དཔྲ' : 'A', 'ལྤ' : 'A', 'སྤ' : 'A', 'སྤྱ' : 'A', 'སྤྲ' : 'A', 'དཔེའུ' : 'C', 'སྤའུ' : 'C', 'སྤེའུ' : 'C', 'སྤྱིའུ' : 'C', 'སྤྲེའུ' : 'C', 'པདྨ' : 'C',
                 'ཕ' : 'A', 'ཕྱ' : 'A', 'ཕྲ' : 'A', 'འཕ' : 'NB', 'འཕྱ' : 'A', 'འཕྲ' : 'A', 'ཕེའུ' : 'C', 'ཕྲའུ' : 'C', 'ཕྲེའུ' : 'C', 'འཕེའུ' : 'C', 'ཕྱྭ': 'C',  
                 'བ' : 'A', 'བྱ' : 'A', 'བྲ' : 'A', 'བླ' : 'A', 'དབ' : 'NB', 'དབྱ' : 'A', 'དབྲ' : 'A', 'འབ' : 'NB', 'འབྱ' : 'A', 'འབྲ' : 'A', 'རྦ' : 'A', 'ལྦ' : 'A', 'སྦ' : 'A', 'སྦྱ' : 'A', 'སྦྲ' : 'A', 'བེའུ' : 'C', 'བྱའུ' : 'C', 'བྱིའུ' : 'C', 'བྱེའུ' : 'C', 'བྲའུ' : 'C', 'བྲའོ' : 'C', 'བྲེའུ' : 'C', 'བྲོའུ' : 'C', 'འབེའུ' : 'C', 'སྦྲེའུ' : 'C', 
                 'མ' : 'A', 'མྱ' : 'A', 'མྲ' : 'A', 'དམ' : 'NB', 'དམྱ' : 'A', 'དམྲ' : 'A', 'རྨ' : 'A', 'རྨྱ' : 'A', 'སྨ' : 'A', 'སྨྱ' : 'A', 'སྨྲ' : 'A', 'མིའུ' : 'C', 'མུའུ' : 'C', 'མོའུ' : 'C', 'མྱིའུ' : 'C', 'རྨེའུ' : 'C', 'སྨེའུ' : 'C', 
                 'ཙ' : 'A', 'གཙ' : 'NB', 'བཙ' : 'NB', 'རྩ' : 'A', 'སྩ' : 'A', 'བརྩ' : 'A', 'བསྩ' : 'A', 'ཙིའུ' : 'C', 'ཙེའུ' : 'C', 'གཙེའུ' : 'C', 'རྩེའུ' : 'C', 'རྩྭ': 'C',  
                 'ཚ' : 'A', 'མཚ' : 'NB', 'འཚ' : 'NB', 'ཚའུ' : 'C', 'ཚུའུ' : 'C', 'ཚེའུ' : 'C', 'མཚེའུ' : 'C', 'མཚེའུ' : 'C', 'ཚྭ': 'C',  
                 'ཛ' : 'A', 'མཛ' : 'NB', 'འཛ' : 'NB', 'རྫ' : 'A', 'བརྫ' : 'A', 'རྫིའུ' : 'C', 'རྫེའུ' : 'C', 'གཞུའུ' : 'C', 
                 'ཝ' : 'A', 
                 'ཞ' : 'A', 'གཞ' : 'NB', 'བཞ' : 'NB', 'ཞྭ': 'C',  
                 'ཟ' : 'A', 'ཟླ' : 'A', 'གཟ' : 'NB', 'བཟ' : 'NB', 'བཟླ' : 'A', 'ཟེའུ' : 'C', 'ཟྭ': 'C',  
                 'འ' : 'A', 
                 'ཡ' : 'A', 'གཡ' : 'NB', 'ཡེའུ' : 'C', 'གཡིའུ' : 'C', 
                 'ར' : 'A', 'རླ' : 'A', 'བརླ' : 'A', 'རེའུ' : 'C', 'རྭ': 'C',  
                 'ལ' : 'A', 'ལའུ' : 'C', 'ལིའུ' : 'C', 'ལེའུ' : 'C', 'ལོའུ' : 'C', 'ལྭ': 'C',  
                 'ཤ' : 'A', 'གཤ' : 'NB', 'བཤ' : 'NB', 'ཤའུ' : 'C', 'ཤེའུ' : 'C', 'ཤྭ': 'C',  
                 'ས' : 'A', 'སྲ' : 'A', 'སླ' : 'A', 'གས' : 'NB', 'བས' : 'NB', 'བསྲ' : 'A', 'བསླ' : 'A', 'སིའུ' : 'C', 'སེའུ' : 'C', 'སྲིའུ' : 'C', 'སླེའུ' : 'C', 'བསེའུ' : 'C', 'སླེའོ' : 'C', 'བསྭོ': 'C',  'སྭ': 'C',  'བསྭ': 'C',  
                 'ཧ' : 'A', 'ཧྲ' : 'A', 'ལྷ' : 'A', 'ཧུའུ' : 'C', 'ཧེའུ' : 'C', 'ཧྲུའུ' : 'C', 'ཧྭ': 'C',  
                 'ཨ' : 'A'}
        self.suffixes = ["འ", "ག", "གས", "ང", "ངས", "ད", "ན", "བ", "བས", "མ", "མས", "ལ", "འི", "འོ", "འང", "འམ", "ར", "ས",
                     "ི", "ིག", "ིགས", "ིང", "ིངས", "ིད", "ིན", "ིབ", "ིབས", "ིམ", "ིམས", "ིལ", "ིའི", "ིའོ", "ིའང", "ིའམ", "ིར", "ིས",
                     "ུ", "ུག", "ུགས", "ུང", "ུངས", "ུད", "ུན", "ུབ", "ུབས", "ུམ", "ུམས", "ུལ", "ུའི", "ུའོ", "ུའང", "ུའམ", "ུར", "ུས",
                     "ེ", "ེག", "ེགས", "ེང", "ེངས", "ེད", "ེན", "ེབ", "ེབས", "ེམ", "ེམས", "ེལ", "ེའི", "ེའོ", "ེའང", "ེའམ", "ེར", "ེས",
                     "ོ", "ོག", "ོགས", "ོང", "ོངས", "ོད", "ོན", "ོབ", "ོབས", "ོམ", "ོམས", "ོལ", "ོའི", "ོའོ", "ོའང", "ོའམ", "ོར", "ོས"]
        self.Csuffixes =  ["འི", "འོ", "འང", "འམ", "ར", "ས"]
        
        self.list_roots = sorted([root for root in self.roots])
        self.list_suffixes = sorted([suf for suf in self.suffixes])
        self.list_Csuffixes = sorted([suf for suf in self.Csuffixes])
        self.len_list_roots = len(self.list_roots)
        self.len_list_suffixes = len(self.list_suffixes)
        self.len_list_Csuffixes = len(self.list_Csuffixes)

        # all dicts from https://github.com/eroux/tibetan-spellchecker/tree/master/syllables
        self.special = ['བགླ', 'མདྲོན', 'བརྡའ', 'བརྟའ']
        self.wazurs = ['ཧྭག', 'ཀྭས', 'ཁྭངས', 'ཧྭང', 'ཀྭན', 'དྭགས', 'ཧྭགས', 'དྭངས', 'ཏྭོན']
        self.exceptions = sorted(self.special + self.wazurs)
        self.len_exceptions = len(self.exceptions)
        self.ambiguous = {'མངས' : ('མ', 'ངས'), 'མགས' : ('མ', 'གས'), 'དབས' : ('ད', 'བས'), 'དངས' : ('ད', 'ངས'), 'དགས' : ('དག', 'ས'), 'དམས' : ('དམ', 'ས'), 'བགས' : ('བ', 'གས'), 'འབས' : ('འབ', 'ས'), 'འགས' : ('འག', 'ས')}

    def get(self, syl):
        if syl not in self.exceptions and syl not in self.ambiguous: 
            l_s = len(syl)
            # find all possible roots
            root = []
            if len(syl) > 5 and search(self.list_roots, self.len_list_roots, syl[:6]): root.append(syl[:6])
            if len(syl) > 4 and search(self.list_roots, self.len_list_roots, syl[:5]): root.append(syl[:5])    
            if len(syl) > 3 and search(self.list_roots, self.len_list_roots, syl[:4]): root.append(syl[:4])    
            if len(syl) > 2 and search(self.list_roots, self.len_list_roots, syl[:3]): root.append(syl[:3])
            if len(syl) > 1 and search(self.list_roots, self.len_list_roots, syl[:2]): root.append(syl[:2])
            if len(syl) > 0 and search(self.list_roots, self.len_list_roots, syl[:1]): root.append(syl[:1])
            # find all possible suffixes
            suffix = []
            if l_s > 1:
                if search(self.list_suffixes, self.len_list_suffixes, syl[l_s-1:]): suffix.append(syl[l_s-1:])
                if search(self.list_suffixes, self.len_list_suffixes, syl[l_s-2:]): suffix.append(syl[l_s-2:])
                if search(self.list_suffixes, self.len_list_suffixes, syl[l_s-3:]): suffix.append(syl[l_s-3:])

            # deal with all the C roots
            #print(self.syl, root)
            if root != [] and self.roots[root[0]] == 'C':
                if root[0] == syl:
                    return (root[0], '')
                else:
                    for s in suffix:
                        if s in self.Csuffixes and root[0]+s == syl:
                            return (root[0], s)

            # find all possible matches 
            solutions = []
            if suffix != [] and root != []:
                # dealing with all other cases
                for r in root:
                    for s in suffix:
                        # unexpected འ་ 
                        if self.roots[r] == 'A' and s == 'འ' and r+s == syl: 
                            #print(r, roots[r])
                            return None
                        else:
                            # if root+suffix make the syllable + avoids duplicates
                            if r+s == syl and (r, s) not in solutions:
                                solutions.append((r, s))
                if solutions != [] : 
                    if len(solutions) > 1:
                        return solutions
                    else:
                        return(solutions[0])
                # root + suffix don’t make syl
                else : 
                    #print(solutions)
                    return None
            elif root != []:
                #print('k')
                for r in root:
                    if r in self.roots and r == syl:
                        # if syllable is valid without suffix + without aa
                        if self.roots[r] != 'NB' and (r, '') not in solutions: 
                            solutions.append((r, ''))
                if solutions != [] : 
                    if len(solutions) > 1:
                        return solutions
                    else:
                        return(solutions[0])
                # non-valid syl
                else : return None
            # non-valid syl
            else: return None
        elif syl in self.ambiguous: return self.ambiguous[syl]
        else: return (syl, 'x')


# In[20]:

class Mingzhi():
    def __init__(self):
        # dict of roots with their corresponding mingzhi
        self.roots = {'ཀ' : 'ཀ', 'ཀྱ' : 'ཀ', 'ཀྲ' : 'ཀ', 'ཀླ' : 'ལ', 'དཀ' : 'ཀ', 'དཀྱ' : 'ཀ', 'དཀྲ' : 'ཀ', 'དཀླ' : 'ལ', 'བཀ' : 'ཀ', 'བཀྱ' : 'ཀ', 'བཀྲ' : 'ཀ', 'བཀླ' : 'ླ', 'རྐ' : 'ྐ', 'རྐྱ' : 'ྐ', 'ལྐ' : 'ྐ', 'སྐ' : 'ྐ', 'སྐྱ' : 'ྐ', 'སྐྲ' : 'ྐ', 'བརྐ' : 'ྐ', 'བརྐྱ' : 'ྐ', 'བསྐ' : 'ྐ', 'བསྐྱ' : 'ྐ', 'བསྐྲ' : 'ྐ', 'ཁ' : 'ཁ', 'ཁྱ' : 'ཁ', 'ཁྲ' : 'ཁ', 'མཁ' : 'ཁ', 'མཁྱ' : 'ཁ', 'མཁྲ' : 'ཁ', 'འཁ' : 'ཁ', 'འཁྱ' : 'ཁ', 'འཁྲ' : 'ཁ', 'ག' : 'ག', 'གྱ' : 'ག', 'གྲ' : 'ག', 'གླ' : 'ླ', 'དག' : 'ག', 'དགྱ' : 'ག', 'དགྲ' : 'ག', 'བག' : 'ག', 'བགྱ' : 'ག', 'བགྲ' : 'ག', 'མག' : 'ག', 'མགྱ' : 'ག', 'མགྲ' : 'ག', 'འག' : 'ག', 'འགྱ' : 'ག', 'འགྲ' : 'ག', 'རྒ' : 'ྒ', 'རྒྱ' : 'ྒ', 'ལྒ' : 'ྒ', 'སྒ' : 'ྒ', 'སྒྱ' : 'ྒ', 'སྒྲ' : 'ྒ', 'བརྒ' : 'ྒ', 'བརྒྱ' : 'ྒ', 'བསྒ' : 'ྒ', 'བསྒྱ' : 'ྒ', 'བསྒྲ' : 'ྒ', 'ང' : 'ང', 'དང' : 'ང', 'མང' : 'ང', 'རྔ' : 'ྔ', 'ལྔ' : 'ྔ', 'སྔ' : 'ྔ', 'བརྔ' : 'ྔ', 'བསྔ' : 'ྔ', 'ཅ' : 'ཅ', 'གཅ' : 'ཅ', 'བཅ' : 'ཅ', 'ལྕ' : 'ྕ', 'ཆ' : 'ཆ', 'མཆ' : 'ཆ', 'འཆ' : 'ཆ', 'ཇ' : 'ཇ', 'མཇ' : 'ཇ', 'འཇ' : 'ཇ', 'རྗ' : 'ྗ', 'ལྗ' : 'ྗ', 'བརྗ' : 'ྗ', 'ཉ' : 'ཉ', 'གཉ' : 'ཉ', 'མཉ' : 'ཉ', 'རྙ' : 'ྙ', 'སྙ' : 'ྙ', 'བརྙ' : 'ྙ', 'བསྙ' : 'ྙ', 'ཏ' : 'ཏ', 'ཏྲ' : 'ཏ', 'གཏ' : 'ཏ', 'གཏྲ' : 'ཏ', 'བཏ' : 'ཏ', 'བཏྲ' : 'ཏ', 'རྟ' : 'ྟ', 'ལྟ' : 'ྟ', 'སྟ' : 'ྟ', 'བརྟ' : 'ྟ', 'བལྟ' : 'ྟ', 'བསྟ' : 'ྟ', 'ཐ' : 'ཐ', 'ཐྲ' : 'ཐ', 'མཐ' : 'ཐ', 'འཐ' : 'ཐ', 'ད' : 'ད', 'དྲ' : 'ད', 'གད' : 'ད', 'བད' : 'ད', 'མད' : 'ད', 'འད' : 'ད', 'འདྲ' : 'ད', 'རྡ' : 'ྡ', 'ལྡ' : 'ྡ', 'སྡ' : 'ྡ', 'བརྡ' : 'ྡ', 'བལྡ' : 'ྡ', 'བསྡ' : 'ྡ', 'ན' : 'ན', 'གན' : 'ན', 'མན' : 'ན', 'རྣ' : 'ྣ', 'སྣ' : 'ྣ', 'སྣྲ' : 'ྣ', 'བརྣ' : 'ྣ', 'བསྣ' : 'ྣ', 'པ' : 'པ', 'པྱ' : 'པ', 'པྲ' : 'པ', 'དཔ' : 'པ', 'དཔྱ' : 'པ', 'དཔྲ' : 'པ', 'ལྤ' : 'ྤ', 'སྤ' : 'ྤ', 'སྤྱ' : 'ྤ', 'སྤྲ' : 'ྤ', 'ཕ' : 'ཕ', 'ཕྱ' : 'ཕ', 'ཕྲ' : 'ཕ', 'འཕ' : 'ཕ', 'འཕྱ' : 'ཕ', 'འཕྲ' : 'ཕ', 'བ' : 'བ', 'བྱ' : 'བ', 'བྲ' : 'བ', 'བླ' : 'ླ', 'དབ' : 'བ', 'དབྱ' : 'བ', 'དབྲ' : 'བ', 'འབ' : 'བ', 'འབྱ' : 'བ', 'འབྲ' : 'བ', 'རྦ' : 'ྦ', 'ལྦ' : 'ྦ', 'སྦ' : 'ྦ', 'སྦྱ' : 'ྦ', 'སྦྲ' : 'ྦ', 'མ' : 'མ', 'མྱ' : 'མ', 'མྲ' : 'མ', 'དམ' : 'མ', 'དམྱ' : 'མ', 'དམྲ' : 'མ', 'རྨ' : 'ྨ', 'རྨྱ' : 'ྨ', 'སྨ' : 'ྨ', 'སྨྱ' : 'ྨ', 'སྨྲ' : 'ྨ', 'ཙ' : 'ཙ', 'གཙ' : 'ཙ', 'བཙ' : 'ཙ', 'རྩ' : 'ྩ', 'སྩ' : 'ྩ', 'བརྩ' : 'ྩ', 'བསྩ' : 'ྩ', 'ཚ' : 'ཚ', 'མཚ' : 'ཚ', 'འཚ' : 'ཚ', 'ཛ' : 'ཛ', 'མཛ' : 'ཛ', 'འཛ' : 'ཛ', 'རྫ' : 'ྫ', 'བརྫ' : 'ྫ', 'ཝ' : 'ཝ', 'ཞ' : 'ཞ', 'གཞ' : 'ཞ', 'བཞ' : 'ཞ', 'ཟ' : 'ཟ', 'ཟླ' : 'ླ', 'གཟ' : 'ཟ', 'བཟ' : 'ཟ', 'བཟླ' : 'ླ', 'འ' : 'འ', 'ཡ' : 'ཡ', 'གཡ' : 'ཡ', 'ར' : 'ར', 'རླ' : 'ླ', 'བརླ' : 'ླ', 'ལ' : 'ལ', 'ཤ' : 'ཤ', 'གཤ' : 'ཤ', 'བཤ' : 'ཤ', 'ས' : 'ས', 'སྲ' : 'ས', 'སླ' : 'ླ', 'གས' : 'ས', 'བས' : 'ས', 'བསྲ' : 'ས', 'བསླ' : 'ླ', 'ཧ' : 'ཧ', 'ཧྲ' : 'ཧ', 'ལྷ' : 'ྷ', 'ཨ' : 'ཨ', 'ཀའུ' : 'འ', 'ཀིའུ' : 'འ', 'ཀེའུ' : 'འ', 'ཀོའུ' : 'འ', 'ཀྲུའུ' : 'འ', 'ཁེའུ' : 'འ', 'ཁྱིའུ' : 'འ', 'ཁྱེའུ' : 'འ', 'ཁྲིའུ' : 'འ', 'ཁྲུའུ' : 'འ', 'ཁྲེའུ' : 'འ', 'གའུ' : 'འ', 'གྲིའུ' : 'འ', 'གྲེའུ' : 'འ', 'གླེའུ' : 'འ', 'འགིའུ' : 'འ', 'འགོའུ' : 'འ', 'རྒེའུ' : 'འ', 'སྒའུ' : 'འ', 'སྒེའུ' : 'འ', 'སྒྱེའུ' : 'འ', 'སྒྲེའུ' : 'འ', 'རྔེའུ' : 'འ', 'སྔེའུ' : 'འ', 'གཅིའུ' : 'འ', 'གཅེའུ' : 'འ', 'ལྕེའུ' : 'འ', 'རྗེའུ' : 'འ', 'ཉེའུ' : 'འ', 'སྙེའུ' : 'འ', 'ཏེའུ' : 'འ', 'གཏེའུ' : 'འ', 'རྟའུ' : 'འ', 'རྟེའུ' : 'འ', 'སྟེའུ' : 'འ', 'ཐིའུ' : 'འ', 'ཐུའུ' : 'འ', 'ཐེའུ' : 'འ', 'ཐོའུ' : 'འ', 'མཐེའུ' : 'འ', 'དུའུ' : 'འ', 'དེའུ' : 'འ', 'དྲེའུ' : 'འ', 'མདེའུ' : 'འ', 'རྡེའུ' : 'འ', 'སྡེའུ' : 'འ', 'ནའུ' : 'འ', 'ནེའུ' : 'འ', 'ནོའུ' : 'འ', 'སྣེའུ' : 'འ', 'དཔེའུ' : 'འ', 'སྤའུ' : 'འ', 'སྤེའུ' : 'འ', 'སྤྱིའུ' : 'འ', 'སྤྲེའུ' : 'འ', 'ཕེའུ' : 'འ', 'ཕྲའུ' : 'འ', 'ཕྲེའུ' : 'འ', 'འཕེའུ' : 'འ', 'བེའུ' : 'འ', 'བྱའུ' : 'འ', 'བྱིའུ' : 'འ', 'བྱེའུ' : 'འ', 'བྲའུ' : 'འ', 'བྲའོ' : 'འ', 'བྲེའུ' : 'འ', 'བྲོའུ' : 'འ', 'འབེའུ' : 'འ', 'སྦྲེའུ' : 'འ', 'མིའུ' : 'འ', 'མུའུ' : 'འ', 'མོའུ' : 'འ', 'མྱིའུ' : 'འ', 'རྨེའུ' : 'འ', 'སྨེའུ' : 'འ', 'ཙིའུ' : 'འ', 'ཙེའུ' : 'འ', 'གཙེའུ' : 'འ', 'རྩེའུ' : 'འ', 'ཚའུ' : 'འ', 'ཚུའུ' : 'འ', 'ཚེའུ' : 'འ', 'མཚེའུ' : 'འ', 'མཚེའུ' : 'འ', 'རྫིའུ' : 'འ', 'རྫེའུ' : 'འ', 'གཞུའུ' : 'འ', 'ཟེའུ' : 'འ', 'ཡེའུ' : 'འ', 'གཡིའུ' : 'འ', 'རེའུ' : 'འ', 'ལའུ' : 'འ', 'ལིའུ' : 'འ', 'ལེའུ' : 'འ', 'ལོའུ' : 'འ', 'ཤའུ' : 'འ', 'ཤེའུ' : 'འ', 'སིའུ' : 'འ', 'སེའུ' : 'འ', 'སྲིའུ' : 'འ', 'སླེའུ' : 'འ', 'བསེའུ' : 'འ', 'སླེའོ' : 'འ', 'ཧུའུ' : 'འ', 'ཧེའུ' : 'འ', 'ཧྲུའུ' : 'འ', 'སྟྭ': 'ྟ', 'གྭ': 'ག', 'ཞྭ': 'ཞ', 'ཁྭ': 'ཁ', 'དྲྭ': 'ད', 'ཀྭའི': 'ཀ', 'བསྭོ': 'ས', 'དྭ': 'ད', 'རྭ': 'ར', 'སྭ': 'ས', 'ཤྭ': 'ཤ', 'ཧྭ': 'ཧ', 'ལྭ': 'ལ', 'ཕྱྭ': 'ཕ', 'ཟྭ': 'ཟ', 'ཀྭ': 'ཀ', 'དྭོ': 'ད', 'ཉྭ': 'ཉ', 'ཚྭ': 'ཚ', 'རྩྭ': 'ྩ', 'བསྭ': 'ས', 'གྲྭ': 'ག', 'ཧྭག': 'ཧ', 'ཀྭས': 'ཀ', 'ཁྭངས': 'ཁ', 'ཧྭང': 'ཧ', 'ཀྭན': 'ཀ', 'དྭགས': 'ད', 'ཧྭགས': 'ཧ', 'དྭངས': 'ད', 'ཏྭོན': 'ཏ', 'ཧྤ' : 'ྤ', 'ཀརྨ' : 'ྨ', 'པདྨ' : 'ྨ'}
        self.exceptions = {'བགླ' : 'ླ', 'མདྲོན' : 'ད', 'བརྡའ' : 'ྡ', 'བརྟའ' : 'ྟ'}
        self.wazurs = {'ཧྭག': 'ཧ', 'ཀྭས': 'ཀ', 'ཁྭངས': 'ཁ', 'ཧྭང': 'ཧ', 'ཀྭན': 'ཀ', 'དྭགས': 'ད', 'ཧྭགས': 'ཧ', 'དྭངས': 'ད', 'ཏྭོན': 'ཏ'}
        self.mingzhis = {**self.roots, **self.exceptions, **self.wazurs}

    def get(self, components):
        self.components = components
        '''
        takes as input the output of get_components() and outputs the mingzhi that will serve for the particle agreement.
        for example, ཁྱེའུར will return འ
        returns None if more than one solution from get_components()
        '''
        if type(self.components) == 'list' or self.components == None:
            return None
        else:
            return self.mingzhis[self.components[0]]


# In[6]:

class AntTib:
    '''
    to and from pseudo-Wylie
    to_pw_text() requires the 
    '''
    
    def __init__(self):            
        self.punct_beginning = ["༄", "༅", "࿓", "࿔", "༇", "༆", "༈"]
        self.punct_separators = [" ", "།", "༎", "༏", "༐", "༑", "༔"]
        self.punct_other = ["༼", "༽", "༒", "༓"]
        self.syl_punct = ["་", "༌", "ཿ"]

        # 1rst part of the syllable
        self.roots = {'ཀ': 'k', 'ཀྱ': 'ky', 'ཀྲ': 'kr', 'ཀླ': 'kl', 'ཁ': 'kh', 'ཁྱ': 'khy', 'ཁྲ': 'khr', 'ག': 'g', 'གཅ': 'gc', 'གཉ': 'gny', 'གཏ': 'gt', 'གཏྲ': 'gtr', 'གད': 'gd', 'གན': 'gn', 'གཙ': 'gts', 'གཞ': 'gzh', 'གཟ': 'gz', 'གཡ': 'gqy', 'གཤ': 'gsh', 'གས': 'gs', 'གྱ': 'gy', 'གྲ': 'gr', 'གླ': 'gl', 'ང': 'ng', 'ཅ': 'c', 'ཆ': 'ch', 'ཇ': 'j', 'ཉ': 'ny', 'ཏ': 't', 'ཏྲ': 'tr', 'ཐ': 'th', 'ཐྲ': 'thr', 'ད': 'd', 'དཀ': 'dk', 'དཀྱ': 'dky', 'དཀྲ': 'dkr', 'དཀླ': 'dkl', 'དག': 'dg', 'དགྱ': 'dgy', 'དགྲ': 'dgr', 'དང': 'dng', 'དཔ': 'dp', 'དཔྱ': 'dpy', 'དཔྲ': 'dpr', 'དབ': 'db', 'དབྱ': 'dby', 'དབྲ': 'dbr', 'དམ': 'dm', 'དམྱ': 'dmy', 'དམྲ': 'dmr', 'དྲ': 'dr', 'ན': 'n', 'པ': 'p', 'པྱ': 'py', 'པྲ': 'pr', 'ཕ': 'ph', 'ཕྱ': 'phy', 'ཕྲ': 'phr', 'བ': 'b', 'བཀ': 'bk', 'བཀྱ': 'bky', 'བཀྲ': 'bkr', 'བཀླ': 'bkl', 'བག': 'bg', 'བགྱ': 'bgy', 'བགྲ': 'bgr', 'བཅ': 'bc', 'བཏ': 'bt', 'བཏྲ': 'btr', 'བད': 'bd', 'བཙ': 'bts', 'བཞ': 'bzh', 'བཟ': 'bz', 'བཟླ': 'bzl', 'བརྐ': 'brk', 'བརྐྱ': 'brky', 'བརྒ': 'brg', 'བརྒྱ': 'brgy', 'བརྔ': 'brng', 'བརྗ': 'brj', 'བརྙ': 'brny', 'བརྟ': 'brt', 'བརྡ': 'brd', 'བརྣ': 'brn', 'བརྩ': 'brts', 'བརྫ': 'brdz', 'བརླ': 'brl', 'བལྟ': 'blt', 'བལྡ': 'bld', 'བཤ': 'bsh', 'བས': 'bs', 'བསྐ': 'bsk', 'བསྐྱ': 'bsky', 'བསྐྲ': 'bskr', 'བསྒ': 'bsg', 'བསྒྱ': 'bsgy', 'བསྒྲ': 'bsgr', 'བསྔ': 'bsng', 'བསྙ': 'bsny', 'བསྟ': 'bst', 'བསྡ': 'bsd', 'བསྣ': 'bsn', 'བསྩ': 'bsts', 'བསྲ': 'bsr', 'བསླ': 'bsl', 'བྱ': 'by', 'བྲ': 'br', 'བླ': 'bl', 'མ': 'm', 'མཁ': 'mkh', 'མཁྱ': 'mkhy', 'མཁྲ': 'mkhr', 'མག': 'mg', 'མགྱ': 'mgy', 'མགྲ': 'mgr', 'མང': 'mng', 'མཆ': 'mch', 'མཇ': 'mj', 'མཉ': 'mny', 'མཐ': 'mth', 'མད': 'mad', 'མན': 'mn', 'མཚ': 'mtsh', 'མཛ': 'mdz', 'མྱ': 'my', 'མྲ': 'mr', 'ཙ': 'ts', 'ཚ': 'tsh', 'ཛ': 'dz', 'ཝ': 'w', 'ཞ': 'zh', 'ཟ': 'z', 'ཟླ': 'zl', 'འ': 'v', 'འཁ': 'vkh', 'འཁྱ': 'vkhy', 'འཁྲ': 'vkhr', 'འག': 'vg', 'འགྱ': 'vgy', 'འགྲ': 'vgr', 'འཆ': 'vch', 'འཇ': 'vj', 'འཐ': 'vth', 'འད': 'vd', 'འདྲ': 'vdr', 'འཕ': 'vph', 'འཕྱ': 'vphy', 'འཕྲ': 'vphr', 'འབ': 'vb', 'འབྱ': 'vby', 'འབྲ': 'vbr', 'འཚ': 'vtsh', 'འཛ': 'vdz', 'ཡ': 'y', 'ར': 'r', 'རྐ': 'rk', 'རྐྱ': 'rky', 'རྒ': 'rg', 'རྒྱ': 'rgy', 'རྔ': 'rng', 'རྗ': 'rj', 'རྙ': 'rny', 'རྟ': 'rt', 'རྡ': 'rd', 'རྣ': 'rn', 'རྦ': 'rb', 'རྨ': 'rm', 'རྨྱ': 'rmy', 'རྩ': 'rts', 'རྫ': 'rdz', 'རླ': 'rl', 'ལ': 'l', 'ལྐ': 'lk', 'ལྒ': 'lg', 'ལྔ': 'lng', 'ལྕ': 'lc', 'ལྗ': 'lj', 'ལྟ': 'lt', 'ལྡ': 'ld', 'ལྤ': 'lp', 'ལྦ': 'lb', 'ལྷ': 'lh', 'ཤ': 'sh', 'ས': 's', 'སྐ': 'sk', 'སྐྱ': 'sky', 'སྐྲ': 'skr', 'སྒ': 'sg', 'སྒྱ': 'sgy', 'སྒྲ': 'sgr', 'སྔ': 'sng', 'སྙ': 'sny', 'སྟ': 'st', 'སྡ': 'sd', 'སྣ': 'sn', 'སྣྲ': 'snr', 'སྤ': 'sp', 'སྤྱ': 'spy', 'སྤྲ': 'spr', 'སྦ': 'sb', 'སྦྱ': 'sby', 'སྦྲ': 'sbr', 'སྨ': 'sm', 'སྨྱ': 'smy', 'སྨྲ': 'smr', 'སྩ': 'sts', 'སྲ': 'sr', 'སླ': 'sl', 'ཧ': 'h', 'ཧྲ': 'hr', 'ཨ': 'A'}
        self.rareC = {'བེའུ': 'bevu', 'ཧུའུ': 'huvu', 'ཀིའུ': 'kivu', 'བྲའོ': 'bravo', 'སླེའུ': 'slevu', 'འགོའུ': 'govu', 'ཁྱེའུ': 'khyevu', 'མདེའུ': 'mdevu', 'རྔེའུ': 'rngevu', 'ཚུའུ': 'tshuvu', 'གཅེའུ': 'gcevu', 'རྟའུ': 'rtavu', 'ཁྱིའུ': 'khyivu', 'ཐེའུ': 'thevu', 'སྟེའུ': 'stevu', 'རྩེའུ': 'rtsevu', 'སླེའོ': 'slevo', 'ཤའུ': 'shavu', 'ཉེའུ': 'nyevu', 'སྨེའུ': 'smevu', 'རྟེའུ': 'rtevu', 'ཚའུ': 'tshavu', 'ཙེའུ': 'tsevu', 'གཡིའུ': 'g.yivu', 'སྤྲེའུ': 'sprevu', 'ལོའུ': 'lovu', 'གྲིའུ': 'grivu', 'སྤྱིའུ': 'spyivu', 'འབེའུ': 'bevu', 'གླེའུ': 'glevu', 'ལའུ': 'lavu', 'སྙེའུ': 'snyevu', 'ཕེའུ': 'phevu', 'རྡེའུ': 'rdevu', 'ཀྲུའུ': 'kruvu', 'ཁྲིའུ': 'khrivu', 'བྲེའུ': 'brevu', 'རྨེའུ': 'rmevu', 'གཏེའུ': 'gtevu', 'སྣེའུ': 'snevu', 'ཕྲའུ': 'phravu', 'དྲེའུ': 'drevu', 'སྡེའུ': 'sdevu', 'ནོའུ': 'novu', 'ཟེའུ': 'zevu', 'མིའུ': 'mivu', 'ཁེའུ': 'khevu', 'རྫེའུ': 'rdzevu', 'གཙེའུ': 'gtsevu', 'མཐེའུ': 'mthevu', 'མོའུ': 'movu', 'ཀེའུ': 'kevu', 'སྤའུ': 'spavu', 'དེའུ': 'devu', 'ཧེའུ': 'hevu', 'ཕྲེའུ': 'phrevu', 'ཚེའུ': 'tshevu', 'རྒེའུ': 'rgevu', 'བྲོའུ': 'brovu', 'བྱའུ': 'byavu', 'ཏེའུ': 'tevu', 'ཀོའུ': 'kovu', 'རེའུ': 'revu', 'ལིའུ': 'livu', 'ཡེའུ': 'yevu', 'མུའུ': 'muvu', 'སྒྲེའུ': 'sgrevu', 'ཁྲུའུ': 'khruvu', 'ལེའུ': 'levu', 'བྱེའུ': 'byevu', 'བྱིའུ': 'byivu', 'བྲའུ': 'bravu', 'འཕེའུ': 'phevu', 'གཅིའུ': 'gcivu', 'མཚེའུ': 'mtshevu', 'སྦྲེའུ': 'sbrevu', 'འགིའུ': 'givu', 'སྔེའུ': 'sngevu', 'ནེའུ': 'nevu', 'རྫིའུ': 'rdzivu', 'རྗེའུ': 'rjevu', 'སེའུ': 'sevu', 'ཐིའུ': 'thivu', 'སྒའུ': 'sgavu', 'སིའུ': 'sivu', 'མྱིའུ': 'myivu', 'ཙིའུ': 'tsivu', 'སྲིའུ': 'srivu', 'ནའུ': 'navu', 'བསེའུ': 'bsevu', 'གའུ': 'gavu', 'སྒེའུ': 'sgevu', 'ཀའུ': 'kavu', 'གྲེའུ': 'grevu', 'ཁྲེའུ': 'khrevu', 'སྤེའུ': 'spevu', 'སྒྱེའུ': 'sgyevu', 'དཔེའུ': 'dpevu', 'ཧྲུའུ': 'hruvu', 'ཐོའུ': 'thovu', 'ཤེའུ': 'shevu', 'ཐུའུ': 'thuvu', 'གཞུའུ': 'gzhuvu', 'དུའུ': 'duvu', 'ལྕེའུ': 'lcevu'}
        self.wazurC = {'སྟྭ': 'stw', 'གྭ': 'gw', 'ཞྭ': 'zhw', 'ཁྭ': 'khw', 'དྲྭ': 'drw', 'ཀྭའི': 'kwavi', 'བསྭོ': 'bswo', 'དྭ': 'dw', 'རྭ': 'rw', 'སྭ': 'sw', 'ཤྭ': 'shw', 'ཧྭ': 'hw', 'ལྭ': 'lw', 'ཕྱྭ': 'phyw', 'ཟྭ': 'zw', 'ཀྭ': 'kw', 'དྭོ': 'dwo', 'ཉྭ': 'nyw', 'ཚྭ': 'tshw', 'རྩྭ': 'rtsw', 'བསྭ': 'bsw', 'གྲྭ': 'grw'}
        self.A = {**self.roots, **self.rareC, **self.wazurC}
        # second part of the syllable
        self.NB = {'ག': 'ag', 'གས': 'ags', 'ང': 'ang', 'ངས': 'angs', 'ད': 'ad', 'ན': 'an', 'བ': 'ab', 'བས': 'abs', 'མ': 'am', 'མས': 'ams', 'འ': 'av', 'འང': 'avang', 'འམ': 'avam', 'འི': 'avi', 'འོ': 'avo', 'ར': 'ar', 'ལ': 'al', 'ས': 'as', 'ི': 'i', 'ིག': 'ig', 'ིགས': 'igs', 'ིང': 'ing', 'ིངས': 'ings', 'ིད': 'id', 'ིན': 'in', 'ིབ': 'ib', 'ིབས': 'ibs', 'ིམ': 'im', 'ིམས': 'ims', 'ིའང': 'ivang', 'ིའམ': 'ivam', 'ིའི': 'ivi', 'ིའོ': 'ivo', 'ིར': 'ir', 'ིལ': 'il', 'ིས': 'is', 'ུ': 'u', 'ུག': 'ug', 'ུགས': 'ugs', 'ུང': 'ung', 'ུངས': 'ungs', 'ུད': 'ud', 'ུན': 'un', 'ུབ': 'ub', 'ུབས': 'ubs', 'ུམ': 'um', 'ུམས': 'ums', 'ུའང': 'uvang', 'ུའམ': 'uvam', 'ུའི': 'uvi', 'ུའོ': 'uvo', 'ུར': 'ur', 'ུལ': 'ul', 'ུས': 'us', 'ེ': 'e', 'ེག': 'eg', 'ེགས': 'egs', 'ེང': 'eng', 'ེངས': 'engs', 'ེད': 'ed', 'ེན': 'en', 'ེབ': 'eb', 'ེབས': 'ebs', 'ེམ': 'em', 'ེམས': 'ems', 'ེའང': 'evang', 'ེའམ': 'evam', 'ེའི': 'evi', 'ེའོ': 'evo', 'ེར': 'er', 'ེལ': 'el', 'ེས': 'es', 'ོ': 'o', 'ོག': 'og', 'ོགས': 'ogs', 'ོང': 'ong', 'ོངས': 'ongs', 'ོད': 'od', 'ོན': 'on', 'ོབ': 'ob', 'ོབས': 'obs', 'ོམ': 'om', 'ོམས': 'oms', 'ོའང': 'ovang', 'ོའམ': 'ovam', 'ོའི': 'ovi', 'ོའོ': 'ovo', 'ོར': 'or', 'ོལ': 'ol', 'ོས': 'os'}
        # exceptions
        self.special = {'བགླ' : 'bgla', 'མདྲོན' : 'mdron', 'བརྡའ' : 'brdav', 'བརྟའ' : 'brtav'}
        self.wazur = {'ཧྭག': 'hwag', 'ཀྭས': 'kwas', 'ཁྭངས': 'khwangs', 'ཧྭང': 'hwang', 'ཀྭན': 'kwan', 'དྭགས': 'dwags', 'ཧྭགས': 'hwags', 'དྭངས': 'dwangs', 'ཏྭོན': 'twon'}
        self.exceptions = {**self.special, **self.wazur}
        # inversed lists
        self.C = {v: k for k, v in self.A.items()}
        self.D = {v: k for k, v in self.NB.items()}
        self.E = {v: k for k, v in self.exceptions.items()}
        
        self.list_A = sorted([i for i in self.A])
        self.list_NB = sorted([i for i in self.NB])
        self.list_exceptions = sorted([i for i in self.exceptions])
        self.list_C = sorted([i for i in self.C])
        self.list_D = sorted([i for i in self.D])
        self.list_E = sorted([i for i in self.E])
        self.len_list_A = len(self.list_A)
        self.len_list_NB = len(self.list_NB)
        self.len_list_exceptions = len(self.list_exceptions)
        self.len_list_C = len(self.list_C)
        self.len_list_D = len(self.list_D)
        self.len_list_E = len(self.list_E)

    def to_pw_syl(self, components):
        if type(components) == 'list' or components == None:
            return '***'        
        else:
            part1 = components[0]
            part2 = components[1]
            #print(part1, part2)
            if (search(self.list_A, self.len_list_A, part1) == False) and search(self.list_exceptions, self.len_list_exceptions, part1) == False:
                return '***'
            else:
                # first part of the syllable
                if search(self.list_exceptions, self.len_list_exceptions, part1):
                    a = self.exceptions[part1]
                else:
                    a = self.A[part1]
                # second part of the syllable
                b = ''
                if part2 == '':
                    b = 'a'
                elif part2 != 'x':
                    b = self.NB[part2]
                return a+b

    def from_pw_syl(self, syl):
        #print(syl)
        if syl == '***':
            return '***'
        else:
            a = ''
            if search(self.list_E, self.len_list_E, syl):
                return self.E[syl]
            elif search(self.list_C, self.len_list_C, syl):
                return self.C[syl]
            else:
                i = len(syl)-1
                while i >= 0:
                    if search(self.list_C, self.len_list_C, syl[:i]):
                        a = syl[:i]
                        break
                    i = i-1
            b = syl[len(a):]
            if b.startswith('v') or b.startswith('r') or b.startswith('l') or b.startswith('s'):
                b = 'a'+b
            if b == 'a':
                return self.C[a]
            else:
                return self.C[a]+self.D[b]

    def __is_punct(self, string):
        if '།' in string or '༎' in string or '༏' in string or '༐' in string or '༑' in string or '༔' in string or ';' in string or ':' in string:
            return True
        else:
            return False
    
    def __trim_punct(self, List):  
        # a hack to keep only one time the punctuation. 
        # being forced to put the (xxx)+ into brackets, re.split() creates two list elements for one punctuation block
        i = 0
        while i < len(List)-1:
            if self.__is_punct(List[i]) and self.__is_punct(List[i+1]):
                del List[i+1]
            i = i+1
    
    def to_pw_text(self, string):
        ### Prepare the string : delete all extra punctuations
        # replace the tabs by normal spaces
        string = string.replace('	', ' ')
        # replace all non-breaking tsek by a normal tsek
        string = string.replace('༌', '་')
        # delete all yigos
        string = re.sub('(༄༅+|༆|༇|༈)།?༎? ?།?༎?', '', string)
        # split on the punctuation. here, a paragraph is just a chunk of text separated by shads.
        
        ### split on remaining punctuation
        paragraphs = re.split(r'(( *། *| *༎ *| *༏ *| *༐ *| *༑ *| *༔ *)+)', string)
        # trim the extra punctuation 
        self.__trim_punct(paragraphs)
        #delete the last element of the list if it is an empty string
        if paragraphs[len(paragraphs)-1] == '':
            del paragraphs[len(paragraphs)-1]
        
        ### replace all shads by a ';' and the tershe by a ':'
        for num, element in enumerate(paragraphs):
            if '།' in element or '༏' in element or '༐' in element or '༑' in element:
                paragraphs[num] = element.replace('།', ';').replace('༎', ';').replace('༏', ';').replace('༐', ';').replace('༑', ';')
            elif '༎' in element:
                paragraphs[num] = element.replace('༎', ';;')
            elif '༔' in element:
                paragraphs[num] = element.replace('༔', ':')

        ### translate the syllables into pseudo-wylie
        parts = SylComponents() # instantiate object
        pw_text = []
        for par in paragraphs:
            if ';' not in par and ':' not in par:
                par = re.sub(r'་$', '', par.replace('་ ', ' ')) # delete all tsek at the end of words
                pw_par = []
                words = par.split(' ')
                for word in words:
                    syls = word.split('་')
                    pw_word = []
                    for syl in syls:
                        #print(syl)
                        pw_word.append(self.to_pw_syl(parts.get(syl)))
                    pw_par.append('x'.join(pw_word))
                pw_text.append(' '.join(pw_par))
            else:
                pw_text.append(par)
        return ''.join(pw_text)

    def from_pw_text(self, string):
        text = ''
        syl = ''
        for char in string:
            if char == ' ':
                if syl != '':
                    text += self.from_pw_syl(syl)+'་'
                syl = ''
                text += char
            elif char == ';':
                if syl != '':
                    text += self.from_pw_syl(syl)
                    if syl.endswith('ng'):
                        text += '་'
                syl = ''
                text += '།'
            elif char == ':':
                if syl != '':
                    text += self.from_pw_syl(syl)
                    if syl.endswith('ng'):
                        text += '་'
                syl = ''
                text += '༔'
            elif char == 'x':
                if syl != '':
                    text += self.from_pw_syl(syl)+'་'
                syl = ''
            else:
                syl += char
        return text
    
    def no_space(self, string):
        return string.replace('་ ', '༌')


# In[ ]:



