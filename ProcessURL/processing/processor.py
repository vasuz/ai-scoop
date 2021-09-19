from newspaper import Article
from .override_processor import process_override
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from dictionary import get_definition_merriam

# requires NLTK
# In the python console, use these two commands
# import nltk
# nltk.download()
# In the window that opens, specify download directory as C:\nltk_data (this will save you trouble from updating environment path and stuff)

# How to use:
# initialize processor with the URL that you'd like to scrape as the argument
# call functions

# TODO: Literally any error processing this is one exception away from blowing up into a bajillion byte-sized pieces
class Processor:
    def __init__(self, url):
        self.url = url
        self.article = None

        self.__retrieve()

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

    def heading(self):
        return self.article.title

    def text(self):
        return self.article.text

    def image(self):
        return self.article.top_image

    def authors(self):
        return self.article.authors

    def keywords(self):
        word_list = self.article.keywords
        remove_list = []
        summary = self.summarize();

        for word in word_list:
            if (summary.count(word) < 0 or any(char.isdigit() for char in word)):
                remove_list.append(word);

        for word in remove_list:
            word_list.remove(word)

        return self.word_list;

    def keyword_defs(self):
        dict = {};
        words = self.keywords();

        for word in words:
            dict[word] = get_definition_merriam(word)

        return dict

    # Summarizes the
    def summarize(self):
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

        return summ_article