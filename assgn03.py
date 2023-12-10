from argparse import RawTextHelpFormatter
import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import tree2conlltags

def download_nltk_resources():
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download('treebank')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

def main():
    download_nltk_resources()

    # Example sentence
    raw_text = """The Times of India is one of India's largest and most widely circulated English-language daily newspapers."""

    # Tokenization and Part-of-Speech Tagging
    raw_words = word_tokenize(raw_text)
    tags = pos_tag(raw_words)

    # Named Entity Recognition
    ne = nltk.ne_chunk(tags, binary=True)
    print("Named Entity Recognition Result:")
    print(ne)

    # Convert to IOB format
    iob = tree2conlltags(ne)
    print("\nIOB Format:")
    print(iob)

if __name__ == "__main__":
    main()
