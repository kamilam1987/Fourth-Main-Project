# Author: Maciej Majchrzak
# Reference: https://youtu.be/FLZvOKSCkxY

# Goal of the python code below is to familiarize ourselves with NLP (Natural Language Processing)

# Imports
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union, gutenberg
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download the required NLTK data
# nltk.download()

# tokenizing
    # form of grouping things
    # work tokenizers, sentence tokenizers

def preprocessing():    
    exampleText = "This is being done for main group project. Main goal of this assignment is to get more familiar with python programming language. Another objective is to develop AI chatbot with ability to interact and engage with a human being."

    # Tokenize exampleText into sentences
    print(sent_tokenize(exampleText), "\n")

    # Print each sentence seperately
    for t in sent_tokenize(exampleText):
        print(t)

    # Tokenize exampleText into words
    print("\n", word_tokenize(exampleText), "\n")

    # Print each word seperately
    for t in word_tokenize(exampleText):
        print(t)
    
    return

def stopWords():
    # Stop words  
        # As long as data analytics are concerned there's no much use for stop words (which give english more meaning) such as "our", "the", "a", etc

    exampleSentence = "Purpose of this sentence is to show how to filter stop words"
    stopWords = set(stopwords.words("english"))    # set of english language stop words

    # Print stop words
    print(stopWords, "\n")

    words = word_tokenize(exampleSentence)  # tokenize exampleSentence
    filteredSentence = []   # empty array to hold our filtered words
    filteredSentence2 = [w for w in words if not w in stopWords]    # one line code for same purpose

    # Loop tokenized words
    for w in words:
            if w not in stopWords:  # check each word if it is stop word
                filteredSentence.append(w)  # append to filteredSentence if not a stop word

    # Print the original sentence
    print(exampleSentence)

    # Print the filtered sentence
    print(filteredSentence)
    print(filteredSentence2)

    return



def stemming():
    # Stemming 
        # different affixes of words eg. swim & swimming mean the same things, so stemming is used to save space in database of words
    porterStemmer = PorterStemmer()
    exampleWords = ["playing", "plays", "played", "playfully"]  # array of words to be stemmed

    # Loop through exampleWords
    for w in exampleWords:
        print(porterStemmer.stem(w))    # stem each word and print it

    # Example sentence
    exampleSentence = "Today I played with python playfully to determine if playing would give me new knowledge."

    # Tokenize exampleSentence and loop through words
    for w in word_tokenize(exampleSentence): 
        print(porterStemmer.stem(w))    # print stemmed words

    return



def speechTagging():
    # CC	coordinating conjunction
    # CD	cardinal digit
    # DT	determiner
    # EX	existential there (like: "there is" ... think of it like "there exists")
    # FW	foreign word
    # IN	preposition/subordinating conjunction
    # JJ	adjective	'big'
    # JJR	adjective, comparative	'bigger'
    # JJS	adjective, superlative	'biggest'
    # LS	list marker	1)
    # MD	modal	could, will
    # NN	noun, singular 'desk'
    # NNS	noun plural	'desks'
    # NNP	proper noun, singular	'Harrison'
    # NNPS	proper noun, plural	'Americans'
    # PDT	predeterminer	'all the kids'
    # POS	possessive ending	parent\'s
    # PRP	personal pronoun	I, he, she
    # PRP$	possessive pronoun	my, his, hers
    # RB	adverb	very, silently,
    # RBR	adverb, comparative	better
    # RBS	adverb, superlative	best
    # RP	particle	give up
    # TO	to	go 'to' the store.
    # UH	interjection	errrrrrrrm
    # VB	verb, base form	take
    # VBD	verb, past tense	took
    # VBG	verb, gerund/present participle	taking
    # VBN	verb, past participle	taken
    # VBP	verb, sing. present, non-3d	take
    # VBZ	verb, 3rd person sing. present	takes
    # WDT	wh-determiner	which
    # WP	wh-pronoun	who, what
    # WP$	possessive wh-pronoun	whose
    # WRB	wh-abverb	where, when

    # Part of Speech tagging
        # tags different words into categories
    # To get valid results its best to train on two different datasets
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            print(tagged)   # print tagged words

    except Exception as e:
        print(str(e))
    
    return



def chunking():
    # Chunking - grouping words into meaningful chunks. One of the main goals of chunking is to group into what are 
    # known as "noun phrases." These are phrases of one or more words that contain a noun, maybe some descriptive 
    # words, maybe a verb, and maybe something like an adverb. The idea is to group nouns with the words that are in relation to them.
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""   # RB - find any adverb, NNP - proper noun
            chunkParser = nltk.RegexpParser(chunkGram)  # pass chunk as a regular expression
            chunked = chunkParser.parse(tagged) # pass tag into chunkParser

            # Accessing data via program
            for subtree in chunked.subtrees():
                    print(subtree)

            # Getting just the chunks, ignoring the rest
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                    print(subtree)

            # chunked.draw() # draw chunk
            print(chunked)
            
    except Exception as e:
        print(str(e))
    
    return



def chinking():
    # Chinking - is a lot like chunking, it is basically a way for you to remove a chunk from a chunk. The chunk that 
    # you remove from your chunk is your chink.
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            
            chunkGram = r"""Chunk: {<.*>+}
                                        }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)  # pass chunk as a regular expression
            chunked = chunkParser.parse(tagged) # pass tag into chunkParser

            chunked.draw() # draw chunk
            
    except Exception as e:
        print(str(e))

    return


def namedEntityRecognition():
    # Named Entity Recognition
    # NE Type and Examples
    # ORGANIZATION - Georgia-Pacific Corp., WHO
    # PERSON - Eddy Bonte, President Obama
    # LOCATION - Murray River, Mount Everest
    # DATE - June, 2008-06-29
    # TIME - two fifty a m, 1:30 p.m.
    # MONEY - 175 million Canadian Dollars, GBP 10.40
    # PERCENT - twenty pct, 18.75 %
    # FACILITY - Washington Monument, Stonehenge
    # GPE - South East Asia, Midlothian
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            
            namedEnt = nltk.ne_chunk(tagged, binary=True)   # classifies as named entity
            namedEnt.draw()
            
    except Exception as e:
        print(str(e))
    return



def lemmatizing():
    # Lemmatizing 
    # Similar operation to stemming is called lemmatizing. The major difference between these is, as you saw earlier, 
    # stemming can often create non-existent words. So, your root stem, meaning the word you end up with, is not something you 
    # can just look up in a dictionary. A root lemma, on the other hand, is a real word. Many times, you will wind up with a very 
    # similar word, but sometimes, you will wind up with a completely different word.

    lemmatizer = WordNetLemmatizer()

    print(lemmatizer.lemmatize("cats"))
    print(lemmatizer.lemmatize("cacti"))
    print(lemmatizer.lemmatize("geese"))
    print(lemmatizer.lemmatize("rocks"))
    print(lemmatizer.lemmatize("python"))
    print(lemmatizer.lemmatize("better", pos="a"))  # adjective
    print(lemmatizer.lemmatize("best", pos="a"))
    print(lemmatizer.lemmatize("run"))
    print(lemmatizer.lemmatize("run",'v'))  # verb

    return



def corpora():
    # Corpora - The NLTK corpus is a massive collection of all kinds of natural language data sets 
    # C:\Users\Ltrmex\AppData\Roaming\nltk_data\corpora
    print(nltk.__file__) # location of the NLTK module's __init__.py

    sample = gutenberg.raw("bible-kjv.txt") # access sample text

    tok = sent_tokenize(sample)

    for x in range(5):
        print(tok[x])
    return

# preprocessing()
# stopWords()
# stemming()
# speechTagging()
# chunking()
# chinking()
# namedEntityRecognition()
# lemmatizing()
# corpora()