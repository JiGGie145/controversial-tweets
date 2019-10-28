from collections import defaultdict
from nltk.tokenize import TweetTokenizer


class PostNew:

    def __init__(self, **kwargs):
        self.replies = []
        self.full_text = kwargs.get('full_text', None)
        self.created_at = kwargs.get('created_at', None)
        self.reply_count = kwargs.get('reply_count', None)
        self.conversation_id_str = kwargs.get('conversation_id_str', None)

    def get_threads(self):
        threads = defaultdict(list)
        for reply in self.replies:
            if reply.in_reply_to_status_id_str != self.conversation_id_str:
                threads[reply.in_reply_to_status_id_str].append(reply)
        return threads

    def is_controversial(self, lexicon):
        attacks = 0
        for reply in self.replies:
            if reply.is_attack(lexicon):
                attacks += 1
        return attacks >= 2

    def replies_attack(self):
        return [reply for reply in self.replies if reply.stance == 'attack']


class Tweet:

    tknzr = TweetTokenizer()

    def __init__(self, **kwargs):
        self.tokens = None
        self.stance = None
        self.text = kwargs.get('text', None)
        self.id_str = kwargs.get('id_str', None)
        self.reply_count = kwargs.get('reply_count', 0)
        self.created_at = kwargs.get('created_at', None)
        self.screen_name = kwargs.get('screen_name', None)
        self.conversation_id_str = kwargs.get('conversation_id_str', None)
        self.in_reply_to_status_id_str = kwargs.get('in_reply_to_status_id_str', None)

        self.tokenizer()
 
    def set_stance(self, stance):
        # attack, or support
        self.stance = stance

    def tokenizer(self):
        self.tokens = self.tknzr.tokenize(self.text)

    def is_attack(self, lexicon):
        attack = False
        for token in self.tokens:
            if token in lexicon:
                self.set_stance('attack')
                attack = True
                break
        return attack
