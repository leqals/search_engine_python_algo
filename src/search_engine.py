import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class TFIDF:
    def __init__(self, docs):
        self.docs = docs
        self.tokenized_docs = None
        self.filtered_docs = None
        self.vocabulary = None
        self.tf = None
        self.idf = None
        self.tf_idf = None
        
        self.tokenize()
        self.build_vocabulary()
        self.calculate_tf()
        self.calculate_idf()
        self.calculate_tf_idf()

    def tokenize(self):
        stop_words = set(stopwords.words('english'))
        self.tokenized_docs = [word_tokenize(doc.lower()) for doc in self.docs]
        self.filtered_docs = [[word for word in doc if not word in stop_words] for doc in self.tokenized_docs]

    def build_vocabulary(self):
        self.vocabulary = set()
        for doc in self.filtered_docs:
            self.vocabulary.update(doc)

    def calculate_tf(self):
        self.tf = []
        for doc in self.filtered_docs:
            doc_tf = {}
            for term in self.vocabulary:
                doc_tf[term] = doc.count(term)
            self.tf.append(doc_tf)

    def calculate_idf(self):
        N = len(self.filtered_docs)
        self.idf = {}
        for term in self.vocabulary:
            n = sum([1 for doc in self.filtered_docs if term in doc])
            self.idf[term] = math.log(N / n)

    def calculate_tf_idf(self):
        self.tf_idf = []
        for i, doc in enumerate(self.filtered_docs):
            doc_tf_idf = {}
            for term in self.vocabulary:
                tf_val = self.tf[i][term]
                idf_val = self.idf[term]
                doc_tf_idf[term] = tf_val * idf_val
            self.tf_idf.append(doc_tf_idf)

    def search(self, query):
        query_tokens = [word.lower() for word in word_tokenize(query) if not word in stopwords.words('english')]
        query_tf_idf = {}
        for term in query_tokens:
            if term in self.vocabulary:
                tf_val = query_tokens.count(term)
                idf_val = self.idf[term]
                query_tf_idf[term] = tf_val * idf_val

        doc_vectors = []
        for doc in self.tf_idf:
            vector = []
            for term in self.vocabulary:
                if term in doc:
                    vector.append(doc[term])
                else:
                    vector.append(0)
            doc_vectors.append(vector)

        query_vector = []
        for term in self.vocabulary:
            if term in query_tf_idf:
                query_vector.append(query_tf_idf[term])
            else:
                query_vector.append(0)

        similarity_scores = cosine_similarity([query_vector], doc_vectors)[0]
        sorted_indexes = np.argsort(similarity_scores)[::-1]
        return sorted_indexes