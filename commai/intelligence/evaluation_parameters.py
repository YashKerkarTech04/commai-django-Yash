####################################### Clarity Evaluation Function

from textstat import flesch_reading_ease

# def evaluate_clarity(text):
#     if not text:
#         return 0.00  
#     score = flesch_reading_ease(text)
#     if score > 100:
#         score = 100 - (100 / (score - 99))
#     return round(min(score, 100), 2)

# updated clarity parameter

def evaluate_clarity(text):
    if not text.strip():
        return 0.0
    
    score = flesch_reading_ease(text)
    
    return round(max(0, min(score, 100)), 2)



####################################### Conciseness Evaluation Function 

# def evaluate_conciseness(text):
#     if not text.strip():  
#         return 0.00  

#     words = len(text.split())
#     sentences = len([s for s in text.split('.') if s.strip()])  
    
#     if sentences == 0:  
#         return 100.00

#     avg_sentence_length = words / sentences

#     score = 100 - avg_sentence_length  

#     return round(max(min(score, 100), 0), 2)

import re

def evaluate_conciseness(text):
    text = text.strip()

    if not text:
        return 0.00

    words = text.split()
    word_count = len(words)

    # Split sentences using ., ! or ?
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)

    if sentence_count == 0:
        return 0.00

    avg_length = word_count / sentence_count

    # --------------------------------------------------
    # Handle extremely short/choppy sentences
    # Example: "The. Cat. Sat."
    # --------------------------------------------------
    if avg_length < 5:
        score = avg_length * 15

    else:
        ideal_length = 15

        if avg_length <= ideal_length:
            # Mild penalty for being slightly shorter than ideal
            difference = ideal_length - avg_length
            score = 100 - (difference * 2)

        else:
            # Stronger penalty for long/wordy sentences
            difference = avg_length - ideal_length
            score = 100 - (difference * 5)

    # --------------------------------------------------
    # Penalize excessive repetition
    # (Only for reasonably long text)
    # --------------------------------------------------
    unique_words = len(set(word.lower() for word in words))
    variety_ratio = unique_words / word_count

    if word_count >= 20 and variety_ratio < 0.5:
        score -= 20

    # Clamp score between 0 and 100
    score = max(0.0, min(100.0, score))

    return round(score, 2)
    



####################################### Sentiment Evaluation Function

from textblob import TextBlob

def evaluate_sentiment(text):
    if not text.strip():  
        return 0.00  

    blob = TextBlob(text)
    sentiment = blob.sentiment

    subjectivity = sentiment.subjectivity * 100

    return round(min(max(subjectivity, 0), 100), 2)



####################################### Engagement Evaluation Function

import re

def evaluate_engagement(text):
    text = text.strip()
    if not text:  
        return 0.00  

    sentences = re.split(r'\s*[.!?]+\s*', text)
    sentences = [s for s in sentences if s.strip()]  
    num_sentences = len(sentences)

    questions = len(re.findall(r'\?\s*', text))  
    exclamations = len(re.findall(r'!\s*', text))  

    if num_sentences == 0:
        return 0.00  

    engagement_score = (questions * 2) + (exclamations * 1.5)  
    
    max_possible_score = (num_sentences * 2) + (num_sentences * 1.5)  
    if max_possible_score > 0:
        engagement_score = min((engagement_score / max_possible_score) * 100, 100)

    return round(engagement_score, 2)



###################################### Grammer Evaluation Function

import requests

def evaluate_grammar(text):

    url = "https://api.languagetool.org/v2/check"

    data = {
        "text": text,
        "language": "en-US",
    }

    try:
        response = requests.post(url, data=data, timeout=10)

        # Temporary debugging
        print("Grammar API Status:", response.status_code)

        if response.status_code != 200:
            print("Grammar API Response:")
            print(response.text)
            return 0.00

        try:
            result = response.json()
            print("=" * 60)
            print("STATUS:", response.status_code)
            print("TEXT LENGTH:", len(text.split()))
            print("BODY:")
            print(response.text)
            print("=" * 60)
        except ValueError:
            print("Grammar API returned invalid JSON")
            print(response.text)
            return 0.00

        num_errors = len(result.get("matches", []))
        num_words = len(text.split())

        if num_words == 0:
            return 0.00

        num_uppercase = sum(1 for char in text if char.isupper())
        num_lowercase = sum(1 for char in text if char.islower())

        total_letters = num_uppercase + num_lowercase

        uppercase_ratio = (
            num_uppercase / total_letters
            if total_letters > 0
            else 0
        )

        error_penalty = num_errors / num_words

        score = (1 - error_penalty) * 100
        score *= (1 - (uppercase_ratio * 0.1))

        return round(max(0.0, min(score, 100.0)), 2)

    except requests.exceptions.RequestException as e:
        print("Grammar API Request Failed:", e)
        return 0.00


###################################### Vocabolary Usage Evaluation Function

import re
from collections import Counter
import math

STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 
    'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 
    'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
    'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 
    'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
    "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 
    'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 
    'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 
    'won', "won't", 'wouldn', "wouldn't"
}

FILLERS = {'um', 'uh', 'like', 'you know'}

def evaluate_vocabulary_usage(text):
    text = re.sub(r'\W+', ' ', text.lower()).strip()
    
    if not text:  
        return 0.00 

    words = text.split()
    
    if len(words) == 0:
        return 0.00  
    
    filtered_words = [word for word in words if word not in STOP_WORDS and word not in FILLERS]
    
    if len(filtered_words) == 0:
        return 0.00
    
    word_counts = Counter(filtered_words)
    unique_words = len(word_counts)  
    total_words = len(filtered_words) 
    
    diversity_ratio = unique_words / total_words
    
    if total_words < 10:
        diversity_ratio *= math.log2(total_words + 1) / 4
    
    score = diversity_ratio * 100
    
    return round(min(score, 100), 2)



###################################### Grammer Evaluation Function

from sklearn.feature_extraction.text import TfidfVectorizer

def evaluate_response_appropriateness(text):
    text = text.strip()
    
    if not text:
        return 0.00
    
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([text])

    tfidf_sum = tfidf_matrix.sum()

    score = min(tfidf_sum * 10, 100)  

    return round(score, 2)



###################################### Politeness Evaluation Function

import re

def evaluate_politeness(text):
    if not text:  
        return 0.00
    
    polite_keywords = [
        "please", "thank you", "kindly", "would you mind", "ok", "thank", "thanks", "you",
        "could you", "appreciate", "grateful", "sorry", "excuse me"
    ]
    
    text_cleaned = re.sub(r'[^\w\s]', '', text.lower())
    
    polite_count = sum(text_cleaned.count(keyword) for keyword in polite_keywords)
    
    total_keywords = len(polite_keywords)
    
    politeness_score = (polite_count / total_keywords) * 100 if polite_count else 0
    
    final_score = min(politeness_score, 100)
    
    return round(final_score, 2)




####################################### 

def evaluate_text(text):
    if text is None:
        return {
            "Clarity": 0,
            "Conciseness": 0,
            "Sentiment": 0,
            "Engagement": 0,
            "Grammar": 1,
            "Usage": 0,
            "Response": 0,
            "Politeness": 0
        }
    
    results = {
        "Clarity": evaluate_clarity(text),
        "Conciseness": evaluate_conciseness(text),
        "Sentiment": evaluate_sentiment(text),
        "Engagement": evaluate_engagement(text),
        "Grammar": evaluate_grammar(text),
        "Usage": evaluate_vocabulary_usage(text),
        "Response": evaluate_response_appropriateness(text),
        "Politeness": evaluate_politeness(text)
    }
    
    return results

####################################### 