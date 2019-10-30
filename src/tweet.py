from collections import defaultdict
from nltk.tokenize import TweetTokenizer


class Tweet:

    # See
    # https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    def __init__(self, **kwargs):
        self.replies = None
        self.id_str = kwargs.get('id_str', None)
        self.full_text = kwargs.get('full_text', None)
        self.reply_count = kwargs.get('reply_count', 0)
        self.created_at = kwargs.get('created_at', None)
        self.display_text_range = kwargs.get('display_text_range', None)
        self.conversation_id_str = kwargs.get('conversation_id_str', None)

        self.get_text()

    def get_text(self):
        self.full_text = self.full_text[self.display_text_range[0]:]


class PostNew(Tweet):

    def is_controversial(self, lexicon):
        attacks = 0
        for reply in self.replies:
            if reply.is_attack(lexicon):
                attacks += 1
            if reply.replies:
                for subreply in reply.replies:
                    subreply.is_attack(lexicon)
        return attacks >= 2

    def replies_attack(self):
        return [reply for reply in self.replies if reply.stance == 'attack']


class Reply(Tweet):

    tknzr = TweetTokenizer()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tokens = None
        self.stance = None
        self.screen_name = kwargs.get('screen_name', None)
        self.in_reply_to_status_id_str = kwargs.get('in_reply_to_status_id_str', None)

        self.tokenizer()

    def set_stance(self, stance):
        # attack, or support
        self.stance = stance

    def tokenizer(self):
        self.tokens = self.tknzr.tokenize(self.full_text)

    def is_attack(self, lexicon):
        attack = False
        for token in self.tokens:
            if token in lexicon:
                self.set_stance('attack')
                attack = True
                break
        return attack
