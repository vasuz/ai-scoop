from newspaper import Article
from .override_processor import process_override
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from .components.vocabulary import get_definition_merriam
from .components.wordsearch import get_word_search
from .components.simplifier import simplify_text

# requires NLTK
# In the python console, use these two commands
# import nltk
# nltk.download()
# In the window that opens, specify download directory as C:\nltk_data (this will save you trouble from updating environment path and stuff)

# How to use:
# initialize processor with the URL that you'd like to scrape as the argument
# call functions

# TODO: Literally any error processing this is one exception away from blowing up into a bajillion byte-sized pieces
class ArticleProcessor:
    def __init__(self, url):
        self.url = url
        self.article = None

        self.__retrieve()

        self._summary = self.__summarize()
        self._keywords = self.__keywords()
        self._keyword_definitions = self.__keyword_defs()
    
    def __keywords(self):
        word_list = self.article.keywords
        remove_list = []
        summary = self.get_summary()

        for word in word_list:
            if (summary.count(word) < 0 or any(char.isdigit() for char in word)):
                remove_list.append(word)

        for word in remove_list:
            word_list.remove(word)

        return word_list
    
    def __keyword_defs(self):
        dict = {}
        words = self.get_keywords()

        for word in words:
            definition = get_definition_merriam(word)
            
            if definition:
                dict[word] = definition

        return dict
    
    def __summarize(self):
        article = self.article

        # To extract summary
        # Object of automatic summarization.
        auto_abstractor = AutoAbstractor()
        # Set tokenizer.
        auto_abstractor.tokenizable_doc = SimpleTokenizer()
        # Set delimiter for making a list of sentence.
        auto_abstractor.delimiter_list = [".", "\n"]
        # Object of abstracting and filtering document.
        abstractable_doc = TopNRankAbstractor()
        # Summarize document.
        result_dict = auto_abstractor.summarize(process_override(article.text), abstractable_doc)

        summ_article = ""

        # Output result.
        for sentence in result_dict["summarize_result"]:
            summ_article += sentence
        
        simplified = simplify_text(summ_article)

        return simplified

    def __retrieve(self):
        # For different language newspaper refer above table
        article = Article(self.url, language="en")  # en for English

        # To download the article
        article.download()
        print("Successfully downloaded article")

        # To parse the article
        article.parse()
        print("Successfully parsed article")

        # To perform natural language processing ie..nlp
        article.nlp()
        print("Successfully processed article")

        self.article = article

    def get_heading(self):
        return self.article.title

    def get_raw_text(self):
        return self.article.text

    def get_image(self):
        return self.article.top_image

    def get_authors(self):
        return self.article.authors

    def get_keywords(self):
        return self._keywords

    def get_keyword_definitions(self):
        return self._keyword_definitions
    
    def get_word_search(self):
        return get_word_search(self.get_keywords())

    def get_summary(self):
        return self._summary