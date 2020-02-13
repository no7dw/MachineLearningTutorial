import nltk
mwe_tokenizer = nltk.tokenize.MWETokenizer([('JJ', 'lin'), ('wade','deng')])
string="wade deng love songs of  JJ lin"
tokenized_string=nltk.word_tokenize(string)
mwe_tokenizer.tokenize(tokenized_string)
