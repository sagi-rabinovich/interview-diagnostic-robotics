from GoogleNext.search_engine import SearchEngine
from GoogleNext.similarity.dice_coefficient_measure import DiceCoefficientMeasure
from GoogleNext.tokenizer.path_tokenizer import PathTokenizer

if __name__ == '__main__':
    print("Tokenize by space and count shared tokens")
    texts = ['the cow says moo', 'the cat and the hat', 'the dish ran away with the spoon']
    engine = SearchEngine()
    engine.index(texts)
    search_string = 'a cat ran away'
    print(engine.search(search_string))

    print("Tokenize by path and use dice coefficient measure")
    texts = ['path/to/person', 'path', 'different_path/to/person', 'path/to/person/in/company']
    engine = SearchEngine(tokenizer=PathTokenizer(), similarity_measure=DiceCoefficientMeasure())
    engine.index(texts)
    search_string = 'path/to'
    print(engine.search(search_string))
