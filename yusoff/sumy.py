import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

data = "my name is shubham kumar shukla. It is my pleasure to got opportunity to write article for xyz related to nlp"


# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Creating text parser using tokenization
parser = PlaintextParser.from_string(text, Tokenizer("english"))

from sumy.summarizers.text_rank import TextRankSummarizer

# Summarize using sumy TextRank
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, 2)

text_summary = ""
for sentence in summary:
  text_summary += str(sentence)

print(text_summary)
