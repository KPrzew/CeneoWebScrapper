from app.utils import get_item
from app.parameters import selectors

class Opinion:
    def __init__(self,score,recommendation,author,useful,useless,content,pros,cons,purchase_date,publish_date):
        self.score=score
        self.recommendation=recommendation
        self.author=author
        self.useful=useful
        self.useless=useless
        self.content=content
        self.pros=pros
        self.cons=cons
        self.purchase=purchase_date
        self.publish=publish_date
        return self

    def __str__():
        pass

    def __repr__():
        pass

    def to_dict(self):
        return {
            "score": self.score,
            "recomendation": self.recommendation,
            "author": self.author,
            "useful": self.useful,
            "useless": self.useless,
            "content": self.content,
            "pros": self.pros,
            "cons": self.cons,
            "purchase_date": self.purchase,
            "publish_date": self.publish
        }

    def extract_opinion(self, opinion):
        for key, value in selectors.items():
            setattr(self,key,get_item(opinion, *value))
        self.opinion_id= opinion["data-entry-id"]
        return self
        