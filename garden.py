import spacy

# Initialize spaCy's English language
nlp = spacy.load('en_core_web_sm') 

# Define a list of Garden Path sentences
garden_path_sentences = [
    "The cotton clothing is made of grows in Mississippi.",
    "When Fred eats food gets thrown.",
    "Helen is expecting tomorrow to be a bad day.",
    "The man who hunts ducks out on weekends",
    "Mary plays the piano and sings beautifully"
]

# Tokenize and perform Entity recognition for each sentence
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
    print()

# Write a comment about two unusual entities

# In the second sentence, "Helen" was recognized with the label "ORG" (organization).
# This is unexpected because is not typically a known organization.

# In the second sentence, "a bad day" was recognized 
# with the label "DATE".
# This is also unexpected because "a bad day" is not a date.