#CSE 111 - Week 2: Writing Functions
#Name: Bruno de Sousa Teixeira


import random

def get_determiner(quantity):
  
  if quantity == 1:
      articles = ["a", "one", "the"]
  else:
      articles = ["some", "many", "the"]
  article = random.choice(articles)
  # Randomly choose and return a determiner.
  return article.capitalize()
  # Just to return an article capitalized

def get_adjective():
   adjs = ['beautiful', 'strange', 'yellow', 'fat', 'orange', 'fast', 'big']
   adj = random.choice(adjs)
   return adj
   #Just to exceed the requirements, I added adjectives. 

def get_noun(quantity):
  
  if quantity == 1:
     nouns = ['bird', 'lion', 'cat', 'dinossaur', 'shark', 'squirrel']
  else:
     nouns = ['birds', 'lions', 'cats', 'dinossaurs', 'sharks', 'squirrels']

  noun = random.choice(nouns)
  return noun

def get_verb(quantity, tense):
   
   if tense == 'past':
      verbs = ['drank', 'slept', 'reached', 'screamed', 'shared', 'ran', 'fell']
   elif quantity == 1 and tense == 'present':
      verbs = ['drink', 'sleep', 'reach', 'scream', 'share', 'run', 'fall']
   elif quantity > 1 and tense == 'present':
      verbs = ['drinks', 'sleeps', 'reaches', 'screams', 'shares', 'runs', 'falls']
   else:
      verbs = ['will drink', 'will sleep', 'will reach', 'will scream', 'will share', 'will run', 'will fall']
   verb = random.choice(verbs)  
   return verb

def get_country():
   countries = ['in Brazil', 'in China', 'in Jamaica', 'in Germany', 'in Morocco', 'in Singapore']
   country = random.choice(countries)
   return country
#Just to exceed the requirements, I added countries to explain where these things are happening.

def make_sentence (quantity,tense):
   article = get_determiner(quantity)
   noun = get_noun(quantity)
   verb = get_verb(quantity, tense)
   adj = get_adjective()
   country = get_country()
   phrase = (f"{article} {adj} {noun} {verb} {country}.")
   return phrase

def main():
   
   sentence = make_sentence(1,'past')
   print(sentence)

   sentence = make_sentence(1, 'present')
   print (sentence)

   sentence = make_sentence(1, 'future')
   print (sentence)

   sentence = make_sentence(2, 'past')
   print(sentence)

   sentence = make_sentence(2, 'present')
   print(sentence)

   sentence = make_sentence(2, 'future')
   print (sentence)

main()