import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def init_svm(df):
    vectorizer = CountVectorizer()    
    X = vectorizer.fit_transform(df["payload"].values.astype("U"))

    label_encoder = LabelEncoder()    
    y = label_encoder.fit_transform(df["is_malicious"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)    

    svm_classifier = svm.SVC(kernel='linear', C=1.0)
    svm_classifier.fit(X_train, y_train)
    return (svm_classifier, vectorizer, label_encoder)
