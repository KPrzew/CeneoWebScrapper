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
        pass

    def extract_opinion(self, opinion):
        for key, value in selectors.items():
            setattr(self,key,get_item(opinion, *value))
        self.opinion_id= opinion["data-entry-id"]
        return self
        