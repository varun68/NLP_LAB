# Name -Varun Patil
# Batch - B3
# Roll no-43
# Assignment - Implement NER on textual data using Spacy and NLTK library


############   Using Spacy   #######################################

import spacy
raw_text="""The Times of India is one of India's largest and most widely circulated English-language daily newspapers."""
NER = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
text= NER(raw_text)
for w in text.ents:
    print(w.text,w.label_)

#Output -
# The Times of India ORG
# one CARDINAL
# India GPE
# English LANGUAGE
# daily DATE



##########     NER using NLTK         #############################


from argparse import RawTextHelpFormatter
import nltk
from nltk import word_tokenize
from nltk.tag import pos_tag
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')
sent = nltk.corpus.treebank.tagged_sents()
print(nltk.ne_chunk(sent[0]))
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
raw_text="""The Times of India is one of India's largest and most widely circulated English-language daily newspapers."""
raw_words= word_tokenize(raw_text)
tags=pos_tag(raw_words)
nltk.download('maxent_ne_chunker')
nltk.download('words')
ne = nltk.ne_chunk(tags,binary=True)
print(ne)
nltk.download('maxent_ne_chunker')
nltk.download('words')
ne = nltk.ne_chunk(tags,binary=True)
print(ne)
from nltk.chunk import tree2conlltags
iob = tree2conlltags(ne)
iob



# output -
# [nltk_data] Error loading maxent_ne_chunker: [Errno 104] Connection
# [nltk_data]     reset by peer
# [nltk_data] Downloading package words to /home/exam/nltk_data...
# [nltk_data]   Package words is already up-to-date!
# [nltk_data] Downloading package treebank to /home/exam/nltk_data...
# [nltk_data]   Package treebank is already up-to-date!
# (S
#   (PERSON Pierre/NNP)
#   (ORGANIZATION Vinken/NNP)
#   ,/,
#   61/CD
#   years/NNS
#   old/JJ
#   ,/,
#   will/MD
#   join/VB
#   the/DT
#   board/NN
#   as/IN
#   a/DT
#   nonexecutive/JJ
#   director/NN
#   Nov./NNP
#   29/CD
#   ./.)
# [nltk_data] Downloading package punkt to /home/exam/nltk_data...
# [nltk_data]   Package punkt is already up-to-date!
# [nltk_data] Downloading package averaged_perceptron_tagger to
# [nltk_data]     /home/exam/nltk_data...
# [nltk_data]   Package averaged_perceptron_tagger is already up-to-
# [nltk_data]       date!
# [nltk_data] Downloading package maxent_ne_chunker to
# [nltk_data]     /home/exam/nltk_data...
# [nltk_data]   Package maxent_ne_chunker is already up-to-date!
# [nltk_data] Downloading package words to /home/exam/nltk_data...
# [nltk_data]   Package words is already up-to-date!
# (S
#   The/DT
#   Times/NNP
#   of/IN
#   (NE India/NNP)
#   is/VBZ
#   one/CD
#   of/IN
#   (NE India/NNP)
#   's/POS
#   largest/JJS
#   and/CC
#   most/RBS
#   widely/RB
#   circulated/VBN
#   English-language/JJ
#   daily/JJ
#   newspapers/NNS
#   ./.)
# [nltk_data] Downloading package maxent_ne_chunker to
# [nltk_data]     /home/exam/nltk_data...
# [nltk_data]   Package maxent_ne_chunker is already up-to-date!
# [nltk_data] Downloading package words to /home/exam/nltk_data...
# [nltk_data]   Package words is already up-to-date!
# (S
#   The/DT
#   Times/NNP
#   of/IN
#   (NE India/NNP)
#   is/VBZ
#   one/CD
#   of/IN
#   (NE India/NNP)
#   's/POS
#   largest/JJS
#   and/CC
#   most/RBS
#   widely/RB
#   circulated/VBN
#   English-language/JJ
#   daily/JJ
#   newspapers/NNS
#   ./.)