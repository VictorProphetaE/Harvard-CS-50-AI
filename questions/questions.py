import nltk
import sys
import os
import math
import string
from os.path import join , exists
nltk.download('stopwords')

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    #verify if directory exist after that get only the files with .txt e encode to utf
    if exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open(join(directory, filename), encoding="utf8") as f:
                    files[filename] = f.read()
    return files               
                

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    #first is lowed the sentece next is tokenized
    lower_sent = document.lower()
    words = nltk.tokenize.word_tokenize(lower_sent)
    #exclude punctuation
    punctuation = string.punctuation
    #next is excluded the stop words
    stop_words = nltk.corpus.stopwords.words("english")
    doc_clean = [token for token in words if token not in punctuation and token not in stop_words]
    
    return doc_clean
    
def count(documents):
    """Count the frequencies in document and return the frequencie 
    used the same code that was explained for tf idf with some
    modifications
    """ 
    frequencies = dict()
    for doc in documents:
        words = set(documents[doc])
        for word in words:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
                
    return frequencies
    
def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    
    idfs = dict()
    #call the frequencies
    cont = count(documents)
    #calculated the idf
    for word in cont:
        idf = math.log(len(documents) / cont[word])
        idfs[word] = idf
        
    return idfs

def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    #the dictionary is created and zeroed based on the number of files
    tfidfs = dict()
    for i in files:
        tfidfs[i] = 0    
    
    for word in query:
        #is verified if the word exist, if exist is calculated the tf idf
        if word in idfs:
            for filename in files:
                tf = files[filename].count(word)
                tfidfs[filename]+= (tf * idfs[word])
        else:
            print("Word not in corpus, try other question")
            break
    #sorted the tf idf to return the "n" top files
    final_score = sorted([filename for filename in files], key=lambda x: tfidfs[x], reverse=True)
    
    return final_score[:n]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    #the dictionary is created and zeroed based on the number of files
    tp_sentece = dict()   
    for i in sentences:
        tp_sentece[i] = 0    
    for sentence in sentences:
        idf = 0
        qtd = 0
        words = sentences[sentence]
        tam = len(sentences[sentence])
        for word in query:
            if word in words:
                #Sum all the the idfs for the word
                idf += idfs[word]
                #Is computed the qtd
                qtd += words.count(word)/tam
        #add the values in tp sentece
        tp_sentece[sentence] = (idf, qtd)
        
    #sorted to return the "n" top sentences based on idf and qtd
    final_sentece = sorted([sentence for sentence in sentences], key= lambda x: (tp_sentece[x][0], tp_sentece[x][1]), reverse=True)

    
    return final_sentece[:n]

if __name__ == "__main__":
    main()
