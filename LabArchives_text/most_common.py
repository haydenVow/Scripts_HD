import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pylab as mpl
import logs
import string

### Lab Archives text Analysis

## Goal:
# read the files in files to read and extract the trends/keywords
# display the trends/keywords in a graph and a table
# Highlight the most regular:
# Processies (ie passage, feed, count, etc)
# format (cell stack, 24 well plate, 96 well plate, T-flask, E-Flask, etc)

## Steps:
# 1. Read the files
# 2. Tokenize the files
# 3. Remove the stop words
# 4. Stem the words
# 5. Count the words
# 6. Display the results

logs.logger.info(f'downloading punkt  ......')
nltk.download('punkt')
nltk.download('stopwords')

# combine all the files in the FOLDER_PATH into one file
#logs.logger.info(f'combining files')
#FOLDER_PATH = "files_to_read"
COMBINED_FILE = "combined_file.txt"
#with open(COMBINED_FILE, "w") as outfile:
#    for filename in os.listdir(FOLDER_PATH):
#        with open(os.path.join(FOLDER_PATH, filename)) as infile:
#            outfile.write(infile.read())

def enumate_words():
    with open(COMBINED_FILE, 'r') as f:
        for line in f:
            yield word_tokenize(line)

logs.logger.info(f'tokenising')
# tokenise the big file
freq_dict = {}
for word_list in enumate_words():
    for word in word_list:
        if word.lower() in freq_dict.keys():
            freq_dict[word.lower()] += 1
        else:
            freq_dict[word.lower()] = 1

logs.logger.info(f'plotting')
# plot the freq dict as a line graph
myList = freq_dict.items()
myList = sorted(myList)
x, y = zip(*myList)
# mpl.bar(x, y)

additional_stop_words = ['', '-', ';'] + list('1234567890') + ['x', 'thi', '10', 'use', '``', 'p/']


# stem the words
stemmer = nltk.stem.PorterStemmer()
stemmed_dict = {}
logs.logger.info(f'stemming')
for word in freq_dict:
    stemmed_word = stemmer.stem(word)
    if stemmed_word in stemmed_dict:
        stemmed_dict[stemmed_word] += freq_dict[word]
    else:
        stemmed_dict[stemmed_word] = freq_dict[word]

# remove the stop words
logs.logger.info(f'removing stop words')
stop_words = nltk.corpus.stopwords.words('english') + list(string.punctuation) + additional_stop_words
for word in stop_words:
    if word in stemmed_dict:
        del stemmed_dict[word]

freq = nltk.FreqDist(stemmed_dict)
top_50 = freq.most_common(100)
logs.logger.info(top_50)
nltk.FreqDist(dict(top_50)).plot()
# plot the stemmed dict as a bar graph
#mpl.bar(top_50)
#mpl.show()

# search the text for ordered lists

