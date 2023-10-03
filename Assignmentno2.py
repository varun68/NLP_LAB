# Name:Varun Patil
# Batch:B3
# Roll:43
# Title:- Perform bag of word, tf-idf and Word2Vec using gensim python library

##########################################################################################

import gensim
from gensim import corpora, models
import numpy as np
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
from gensim import corpora


text1 = ["""I want to go to school . I am going to school now ."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text1])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text1]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

# Create a Word2Vec model
w2v_model = Word2Vec(tokens1, vector_size=100, window=5, min_count=1, sg=0)

print("Word2Vec Model:")
print("Vector for 'school':", w2v_model.wv['school'])  # Get the vector for 'school'

####################################################################################

# output:-
# The dictionary has: 9 tokens

# {'.': 0, 'I': 1, 'am': 2, 'go': 3, 'going': 4, 'now': 5, 'school': 6, 'to': 7, 'want': 8}
# Bag of Words :  [[(0, 2), (1, 2), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (7, 3), (8, 1)]]
# Dictionary :
# [['am', 1], ['go', 1], ['going', 1], ['now', 1], ['school', 2], ['to', 3], ['want', 1]]
# TF-IDF Vector:
# [['am', 0.24], ['go', 0.24], ['going', 0.24], ['now', 0.24], ['school', 0.47], ['to', 0.71], ['want', 0.24]]
# Word2Vec Model:
# Vector for 'school': [ 9.4563962e-05  3.0773198e-03 -6.8126451e-03 -1.3754654e-03
#   7.6685809e-03  7.3464094e-03 -3.6732971e-03  2.6427018e-03
#  -8.3171297e-03  6.2054861e-03 -4.6373224e-03 -3.1641065e-03
#   9.3113566e-03  8.7338570e-04  7.4907029e-03 -6.0740625e-03
#   5.1605068e-03  9.9228229e-03 -8.4573915e-03 -5.1356913e-03
#  -7.0648370e-03 -4.8626517e-03 -3.7785638e-03 -8.5361991e-03
#   7.9556061e-03 -4.8439382e-03  8.4236134e-03  5.2625705e-03
#  -6.5500261e-03  3.9578713e-03  5.4701497e-03 -7.4265362e-03
#  -7.4057197e-03 -2.4752307e-03 -8.6257253e-03 -1.5815723e-03
#  -4.0343284e-04  3.2996845e-03  1.4418805e-03 -8.8142155e-04
#  -5.5940580e-03  1.7303658e-03 -8.9737179e-04  6.7936908e-03
#   3.9735902e-03  4.5294715e-03  1.4343059e-03 -2.6998555e-03
#  -4.3668128e-03 -1.0320747e-03  1.4370275e-03 -2.6460087e-03
#  -7.0737829e-03 -7.8053069e-03 -9.1217868e-03 -5.9351693e-03
#  -1.8474245e-03 -4.3238713e-03 -6.4606704e-03 -3.7173224e-03
#   4.2891586e-03 -3.7390434e-03  8.3781751e-03  1.5339935e-03
#  -7.2423196e-03  9.4337985e-03  7.6312125e-03  5.4932819e-03
#  -6.8488456e-03  5.8226790e-03  4.0090932e-03  5.1853694e-03
#   4.2559016e-03  1.9397545e-03 -3.1701624e-03  8.3538452e-03
#   9.6121803e-03  3.7926030e-03 -2.8369951e-03  7.1275235e-06
#   1.2188185e-03 -8.4583247e-03 -8.2239453e-03 -2.3101569e-04
#   1.2372875e-03 -5.7433806e-03 -4.7252737e-03 -7.3460746e-03
#   8.3286157e-03  1.2129784e-04 -4.5093987e-03  5.7017053e-03
#   9.1800150e-03 -4.0998720e-03  7.9646818e-03  5.3754342e-03
#   5.8791232e-03  5.1259040e-04  8.2130842e-03 -7.0190406e-03]

