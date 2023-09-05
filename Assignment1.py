"""
Assigment No-1
Name - Varun Patil
Batch- B3
Roll no - 43
Assignment - The Pre-processing using NLP operations:perform Tokenization
Stop word removal, Punctuation removal ,using Spacy or NLTK library 

"""
#--------------------Tokenization----------------------------
import spacy  # imported spacy library
nlp = spacy.load("en_core_web_sm") # loaded 
about_text = (
    "The Moon is a barren, rocky world without air and water. It has dark lava plain on its surface."
    "The Moon is filled wit craters. It has no light of its own. It gets its light from the Sun."
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)

#-------------Stop Words-----------------------
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)


#-----------------------Lemmatization------------------

conference_help_text = (
    "The Moon is a barren, rocky world without air and water. It has dark lava plain on its surface."
    "The Moon is filled wit craters. It has no light of its own. It gets its light from the Sun."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#-------------------------Part-of-Speech Tagging-------------------

about_text = (
    "The Moon is a barren, rocky world without air and water. It has dark lava plain on its surface."
    "The Moon is filled wit craters. It has no light of its own. It gets its light from the Sun."
)
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

# Output -
"""
The 0
Moon 4
is 9
a 12
barren 14
, 20
rocky 22
world 28
without 34
air 42
and 46
water 50
. 55
It 57
has 60
dark 64
lava 69
plain 74
on 80
its 83
surface 87
. 94
The 95
Moon 99
is 104
filled 107
wit 114
craters 118
. 125
It 127
has 130
no 134
light 137
of 143
its 146
own 150
. 153
It 155
gets 158
its 163
light 167
from 173
the 178
Sun 182
. 185
both
down
used
hundred
upon
wherever
show
elsewhere
which
within
                 The : the
                  is : be
                  It : it
                 has : have
                 The : the
                  is : be
              filled : fill
             craters : crater
                  It : it
                 has : have
                  It : it
                gets : get

TOKEN: The
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: Moon
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: barren
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: rocky
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: world
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: without
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: air
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: water
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: It
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: has
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: dark
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: lava
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: plain
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: on
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: its
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: surface
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: The
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: Moon
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: filled
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: wit
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: craters
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: It
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: has
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: no
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: light
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: of
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: its
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: own
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: It
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: gets
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: its
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: light
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: from
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: Sun
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer
"""