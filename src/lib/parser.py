import spacy

class Parser:
  def __init__(self):
    self.nlp = spacy.load('ja_ginza')
  
  def parse(self, text):
    doc = self.nlp(text)

    sentences = []

    for sentence in doc.sents:
      current_sentence = {
        'parts': [],
        'original_sentence': ''
      }

      for token in sentence:
        parts = {
          'index': token.i,
          'word': token.orth_,
          'lemma': token.lemma_,
          'pos': token.pos_,
          'tag': token.tag_,
          'dep': token.dep_,
          'head_index': token.head.i
        }
        current_sentence['parts'].append(parts)
        current_sentence['original_sentence'] += token.orth_
      
      sentences.append(current_sentence)
    
    return sentences