# TODO: Generalizar, y heredar


class PostNew:

    def __init__(self, **kwargs):
        self.created_at = kwargs.get('created_at', None)
        self.reply_count = kwargs.get('reply_count', None)
        self.conversation_id_str = kwargs.get('conservation_id_str', None)
        self.full_text = kwargs.get('full_text', None)
        self.is_controversial = False 
        self.replies = []

    def tweets_attack(self):
        pass

class Tweet:

    def __init__(self, **kwargs):
        self.created_at = kwargs.get('created_at', None)
        self.id_str = kwargs.get('id_str', None)
        self.screen_name = kwargs.get('screen_name', None)
        self.text = kwargs.get('text', None)
        self.in_reply_to_status_id_str = kwargs.get('in_reply_to_status_id_str', None)
        self.reply_count = kwargs.get('reply_count', 0)
        self.stance = None
 
    def set_stance(self, stance):
        # attack, or support
        self.stance = stance
