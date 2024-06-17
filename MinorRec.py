import os
import pymysql
import pandas as pd
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_minor(interests, minors):
    client = OpenAI(api_key=os.environ.get("general_API"))
    interests_embedding = client.embeddings.create(input=interests, model="text-embedding-3-small").data[0].embedding
    minors_embeddings = minors["embedding"].apply(lambda x: np.array(list(map(float, x.split()))))

    # Calculate cosine similarity
    similarities = cosine_similarity([interests_embedding], minors_embeddings.tolist())[0]

    # Add similarities to the DataFrame
    minors['similarity'] = similarities

    # Calculate the maximum similarity value
    max_similarity = minors['similarity'].max()
    print(max_similarity)

    # Filter the DataFrame to keep rows where the similarity is not more than 0.05 less than the maximum similarity
    top_minors = minors[minors['similarity'] >= max_similarity - 0.05]

    # Sort the DataFrame by 'similarity' in descending order
    top_minors.sort_values(by='similarity', ascending=False, inplace=True)
    
    # Keep relevant columns and convert to dictionary
    top_minors = top_minors[['Minor', 'School','Description', 'Total_ECTS']]
    # Remove duplicates
    top_minors = top_minors.drop_duplicates()
    print(top_minors)
    minors_dict = top_minors.set_index('Minor').to_dict(orient='index')
    print(minors_dict)

    return minors_dict