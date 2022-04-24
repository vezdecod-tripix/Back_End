from models.attachment import Attachment


class Post:

    def __init__(self, json):
        self.source_id = json.get("source_id")
        self.is_user = self.source_id > 0
        self.is_group = self.source_id < 0

        self.date = json.get('date')
        self.can_doubt_category = json.get("can_doubt_category")
        self.can_set_category = json.get("can_set_category")
        self.is_favorite = json.get("is_favorite")
        self.post_type = json.get("post_type")
        self.text = str(json.get("text"))
        self.signer_id = json.get("signer_id")
        self.marked_as_ads = json.get("marked_as_ads")
        self.post_source = json.get("post_source")
        self.comments_count = json.get("comments").get("count")
        self.likes_count = json.get("likes").get("count")
        self.reports_count = json.get("reposts").get("count")
        self.views_count = json.get("views")
        self.post_id = json.get("post_id")
        self.type = json.get("type")
        self.attachments = [Attachment(attachment_json) for attachment_json in
                            json.get("attachments")]
