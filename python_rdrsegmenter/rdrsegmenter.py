from os import path as op
from functools import lru_cache
from typing import *
from typing import Callable

DIR_PATH = op.dirname(op.abspath(__file__))
RDR_PATH = op.join(DIR_PATH, 'wordsegmenter.rdr')
VOCAB_PATH = op.join(DIR_PATH, 'vi-vocab')
CLASS_PATH = op.join(DIR_PATH, 'rdrsegmenter.jar')


class TokenizerWrapper:

    def __init__(self):
        self.tokenizer:Callable = lambda text: text

    def tokenize(self, text:str) -> str:
        return self.tokenizer(text)


@lru_cache(typed=True)
def get_segmenter(**kwargs):
    return TokenizerWrapper()


@lru_cache(typed=True)
def load_class(*options, cls:str=CLASS_PATH):
    import jnius_config

    for option in options:
        jnius_config.add_options(option)

    jnius_config.set_classpath(cls)
    from jnius import autoclass
    Vocabulary = autoclass('corenlp.rdrsegmenter.Vocabulary')
    WordSegmenter = autoclass('corenlp.rdrsegmenter.WordSegmenter')

    return Vocabulary, WordSegmenter


@lru_cache(typed=True)
def load_segmenter(*options, cls:str=CLASS_PATH, model:str=RDR_PATH, vocab:str=VOCAB_PATH, **kwargs):
    Vocabulary, WordSegmenter = load_class(*options, cls=cls)
    
    vocabulary = Vocabulary(vocab)
    segmenter = WordSegmenter(model, vocabulary)

    wrapper = get_segmenter(*kwargs)
    wrapper.tokenizer = segmenter.segmentTokenizedString
    return wrapper
