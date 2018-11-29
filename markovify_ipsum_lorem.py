# see https://github.com/jsvine/markovify 
# phippsc
# 11/28/2018

#: Purpose: this script learns a language model from an input corpus, 
# then generates a specified number of documents with dummy text in the style of the corpus.

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import markovify #Markov Chain Generator

#doha_all.txt contains text from DOHA decisions
with open(r'/Users/christopherphipps/Downloads/doha_all.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

#for this print method, see https://stackoverflow.com/questions/53527755/how-to-automate-multiple-file-generation-in-python/53527887#53527887
for nr in range(10):
    with open("file{:04}.txt".format(nr), "w") as f:
        for i in range(10): #10 lines of fake sentences.
            f.write(text_model.make_sentence() + "\n")

#use the block below if you want to control the length of sentences (in characters)
for nr in range(10):
    with open("file{:04}.txt".format(nr), "w") as f:
        for i in range(10): #10 lines of fake sentences.
            f.write(text_model.make_short_sentence(140) + "\n")

