import os
import re
import csv

# DONE: Read labels
# DOING: Build dictionary of 
# TODO: Shuffle to get 70% training, 30% test
# Get labels as to which files are for training, and which are for test
ham_line_paths = []
spam_line_paths = []
with open('./labels', 'r') as file:
    for line in file.readlines():
        if re.match(r'ham', line):
            ham_line_paths.append(line)
        elif re.match(r'spam', line):
            spam_line_paths.append(line)
    # print(len(ham_lines) + len(spam_lines))


ham_vocabulary = {}
with open('hamvectors.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for line_path in ham_line_paths:
        with open(os.path.join(os.getcwd(), re.sub(r'ham \.\.\/', '', ham_line_paths[0])).strip(), 'r') as hamfile:
            ham_file_lines = []
            file_vocab = {}
            for hamfile_line in hamfile.readlines():
                split_words = hamfile_line.split()
                for w in split_words:
                    if ham_vocabulary


vocabulary_spam = {}
with open('spamvectors.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    print(os.path.join(os.getcwd(), re.sub(r'spam \.\.\/', '', spam_lines[0])))


# Start reading all documents
# Tokenize each document
# Identify based on label whether this document is spam or ham
# Accumulate: separate vocabularies for spam and ham
# Accumulate: counts for each word for each classification
# 
# On test
# Tokenize the document and vectorize





# Classifier proper


