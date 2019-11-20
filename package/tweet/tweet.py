from nltk.tokenize import TweetTokenizer
from textblob import TextBlob

# Stances
NEU = 'neutral'
SUP = 'support'
ATK = 'attack'


class Tweet:
    """
    See
    https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    """
    tknzr = TweetTokenizer()

    def __init__(self, **kwargs):
        self.id_str = kwargs.get('id_str', None)
        self.full_text = kwargs.get('full_text', None)
        self.created_at = kwargs.get('created_at', None)
        self.screen_name = kwargs.get('screen_name', None)
        self.display_text_range = kwargs.get('display_text_range', None)
        self.in_reply_to_status_id_str = kwargs.get('in_reply_to_status_id_str', None)

        self.tokens = None
        self.stance = NEU
        self.replies = None

        self.text()
        self.tokenizer()

    def text(self):
        self.full_text = self.full_text[self.display_text_range[0]:].lower()

    def tokenizer(self):
        self.tokens = self.tknzr.tokenize(self.full_text)

    def set_stance(self, stance):
        # attack, or support
        self.stance = stance

    def is_attack(self, lexicon):
        attack = False
        for token in self.tokens:
            if token in lexicon:
                self.set_stance(ATK)
                attack = True
                break
        return attack

    def is_support(self):
        analysis = TextBlob(self.full_text)
        try:
            eng = analysis.translate(to='en')
            if eng.sentiment.polarity > 0:
                self.set_stance(SUP)
        except:
            pass

    def is_controversial(self, lexicon):
        attacks = 0
        for reply in self.replies:
            if reply.is_attack(lexicon):
                attacks += 1
        return attacks >= 2
