import spacy

# Load the spaCy models
nlp_md = spacy.load("en_core_web_md")  # Medium model with vectors
nlp_sm = spacy.load("en_core_web_sm")  # Small model without vectors

def find_similar_movie(input_description, movie_descriptions, model):
    """
    Finds the most similar movie description to the input description using the specified spaCy model.

    Args:
    input_description (str): The description of the movie to compare.
    movie_descriptions (list of str): List of movie descriptions to compare against.
    model: The spaCy language model to use for comparison.

    Returns:
    str: The title of the recommended movie.
    """
    nlp = model  # Use the specified spaCy model
    input_doc = nlp(input_description)  # Process the input description
    
    max_similarity = -1
    recommended_movie = ""
    
    for description in movie_descriptions:
        doc = nlp(description)  # Process each movie description
        similarity = input_doc.similarity(doc)  # Calculate similarity
        
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = description.split(":")[0]  # Assuming title is before ":" in description
    
    return recommended_movie

def main():
    """
    Main function to read movie descriptions from a file, process an input description,
    and find the most similar movie description.
    """
    with open("movies.txt", "r", encoding="utf-8") as f:
        movie_descriptions = [line.strip() for line in f.readlines()]  # Read and strip each line
    
    input_description = (
        "Will he save their world or destroy it? When the Hulk becomes too dangerous for the "
        "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet "
        "where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where "
        "he is sold into slavery and trained as a gladiator."
    )
    
    # Find the recommended movie using the medium model
    recommended_movie_md = find_similar_movie(input_description, movie_descriptions, nlp_md)
    print(f"Recommended movie to watch next using en_core_web_md: {recommended_movie_md}")
    
    # Find the recommended movie using the small model
    recommended_movie_sm = find_similar_movie(input_description, movie_descriptions, nlp_sm)
    print(f"Recommended movie to watch next using en_core_web_sm: {recommended_movie_sm}")

if __name__ == "__main__":
    main()
