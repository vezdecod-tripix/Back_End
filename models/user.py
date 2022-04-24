

class User:

    def __init__(self, json):
        self.id = json.get("id")
        self.first_name = str(json.get("first_name"))
        self.last_name = str(json.get("last_name"))
        self.can_access_closed = json.get("can_access_closed")
        self.is_closed = json.get("is_closed")
        self.sex = json.get("sex")
        self.screen_name = json.get("screen_name")
        self.photo_50 = json.get("photo_50")
        self.photo_100 = json.get("photo_100")
        self.online = bool(json.get("online"))
