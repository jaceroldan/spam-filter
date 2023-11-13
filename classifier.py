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
spam_vocabulary = {}
ham_file_vocabs = []
spam_file_vocabs = []

with open('hamvectors.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for line_path in ham_line_paths:
        with open(os.path.join(os.getcwd(), re.sub(r'ham \.\.\/', '', line_path)).strip(), 'rb') as hamfile:
            file_vocab = {'[[file_path]]': line_path.strip()}

            for hamfile_line in hamfile.readlines():
                try:
                    split_words = re.findall(r'^[A-Za-z]+$', hamfile_line.decode('utf-8'))
                except UnicodeDecodeError:
                    continue
                for w in split_words:
                    if ham_vocabulary.get(w.lower(), None):
                        ham_vocabulary[w.lower()] += 1
                    else:
                        ham_vocabulary[w.lower()] = 1

                    if file_vocab.get(w.lower(), None):
                        file_vocab[w.lower()] += 1
                    else:
                        file_vocab[w.lower()] = 1
            ham_file_vocabs.append(file_vocab)
    
    rows_to_add = [['DOCUMENT', *ham_vocabulary.keys()]]
    for ham_vocab in ham_file_vocabs:
        row = [ham_vocab['[[file_path]]']]
        for word in ham_vocabulary.keys():
            if ham_vocab.get(word, None):
                print('here')
                row.append(ham_vocab[word])
            else:
                row.append(0)
        rows_to_add.append(row)
    writer.writerows(rows_to_add)

with open('spamvectors.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for line_path in spam_line_paths:
        with open(os.path.join(os.getcwd(), re.sub(r'spam \.\.\/', '', line_path)).strip(), 'rb') as spamfile:
            file_vocab = {'[[file_path]]': line_path.strip()}

            for spamfile_line in spamfile.readlines():
                try:
                    split_words = re.findall(r'^[A-Za-z]+$', spamfile_line.decode('utf-8'))
                except UnicodeDecodeError:
                    continue
                for w in split_words:
                    if spam_vocabulary.get(w.lower(), None):
                        spam_vocabulary[w.lower()] += 1
                    else:
                        spam_vocabulary[w.lower()] = 1

                    if file_vocab.get(w.lower(), None):
                        file_vocab[w.lower()] += 1
                    else:
                        file_vocab[w.lower()] = 1
                
            spam_file_vocabs.append(file_vocab)

    writer.writerow(['DOCUMENT', *spam_vocabulary.keys()])

print(len(ham_vocabulary.values()))
print(len(spam_vocabulary.values()))

# On test
# Tokenize the document and vectorize





# Classifier proper



