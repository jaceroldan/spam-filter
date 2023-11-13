import os
import re
import csv
import random

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


def write_word_vectors(filename, line_paths, classification):
    full_vocabulary = {}
    full_file_vocabs = []
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for line_path in line_paths:
            path = os.path.join(os.getcwd(), re.sub(r'{} \.\.\/'.format(classification), '', line_path)).strip()
            print(path)
            with open(path, 'rb') as file:
                file_vocab = {'[[file_path]]': line_path.strip()}

                for line in file.readlines():
                    try:
                        split_words = re.findall(r'^[A-Za-z]+$', line.decode('utf-8'))
                    except UnicodeDecodeError:
                        continue
                    for w in split_words:
                        if full_vocabulary.get(w.lower(), None):
                            full_vocabulary[w.lower()] += 1
                        else:
                            full_vocabulary[w.lower()] = 1

                        if file_vocab.get(w.lower(), None):
                            file_vocab[w.lower()] += 1
                        else:
                            file_vocab[w.lower()] = 1
                full_file_vocabs.append(file_vocab)

        full_vocabulary_wordset = sorted(full_vocabulary.keys())
        rows_to_add = [['DOCUMENT', *full_vocabulary_wordset]]
        for vocab in full_file_vocabs:
            row = [vocab['[[file_path]]']]
            for word in full_vocabulary.keys():
                if vocab.get(word, None):
                    row.append(vocab[word])
                else:
                    row.append(0)
            rows_to_add.append(row)
        writer.writerows(rows_to_add)
    
    return full_vocabulary, full_file_vocabs


ham_vocabulary, ham_file_vocabs = write_word_vectors('hamvectors.csv', ham_line_paths, 'ham')
spam_vocabulary, spam_file_vocabs = write_word_vectors('spamvectors.csv', spam_line_paths, 'spam')

print(len(ham_vocabulary.values()))
print(len(spam_vocabulary.values()))

ham_full = [*ham_file_vocabs]
spam_full = [*spam_file_vocabs]


def take_split(dataset, training_percentage):
    dataset_length = len(dataset)
    sample_count = (dataset_length * (training_percentage / 100)) // 1
    training_sample = []

    while sample_count > 0:
        current_index = random.randint(0, len(dataset) - 1)
        training_sample.append(dataset[current_index])
        del dataset[current_index]
        sample_count -= 1

    return training_sample, dataset

# Split into 70% training and 30% test set
ham_training, ham_test = take_split(ham_full, 70)
print(len(ham_file_vocabs))
print(len(ham_training), len(ham_test))

spam_training, spam_test = take_split(spam_full, 70)
print(len(spam_file_vocabs))
print(len(spam_training), len(spam_test))


