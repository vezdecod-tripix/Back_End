

class Size:

    def __init__(self, json):
        self.height = json.get("height")
        self.url = json.get("url")
        self.type = json.get("type")
        self.width = json.get("width")


class Photo:

    def __init__(self, json):
        self.album_id = json.get("album_id")
        self.date = json.get("date")
        self.id = json.get("id")
        self.owner_id = json.get("owner_id")
        self.access_key = json.get("access_key")
        self.post_id = json.get('post_id')
        self.text = json.get("text")
        self.user_id = json.get("user_id")
        self.sizes = [Size(size_json) for size_json in json.get("sizes")]


class Attachment:

    def __init__(self, json):
        self.type = json.get("type")
        self.is_photo = self.type == "photo"
        self.photo = Photo(json.get("photo")) if self.is_photo else None
