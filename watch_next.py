import spacy

# Load the spaCy medium-sized language model
nlp_md = spacy.load('en_core_web_md')

# Function to read movie descriptions from a file
def read_movie_descriptions(filename):
    with open(filename, 'r') as f:
        descriptions = f.readlines()
    return [desc.strip() for desc in descriptions]

# Function to find the most similar movie description
def find_similar_movie(target_description, movie_descriptions):
    # Process the target description with spaCy
    target_doc = nlp_md(target_description)
    
    # Initialize variables to track the most similar movie
    max_similarity = 0.0
    most_similar_movie = ""

    # Compare the target description with each movie description
    for description in movie_descriptions:
        # Process the current movie description with spaCy
        desc_doc = nlp_md(description)
        
        # Calculate the similarity between the two processed descriptions
        similarity = target_doc.similarity(desc_doc)

        # Update the most similar movie if a higher similarity is found
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = description

    return most_similar_movie

if __name__ == "__main__":
    # The target description from the movie "Planet Hulk"
    target_description = (
        "Will he save their world or destroy it? When the Hulk becomes too dangerous for the "
        "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a "
        "planet where the Hulk can live in peace. Unfortunately, Hulk land on the "
        "planet Sakaar where he is sold into slavery and trained as a gladiator."
    )

    # Read movie descriptions from the 'movies.txt' file
    movie_descriptions = read_movie_descriptions('movies.txt')

    # Find the most similar movie description
    most_similar_movie = find_similar_movie(target_description, movie_descriptions)
    
    # Print the most similar movie description
    print(f"The most similar movie description is: {most_similar_movie}")