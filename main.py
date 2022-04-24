from pprint import pprint

import vk_api
import json

from models.post import Post
from models.user import User

vk_session = vk_api.VkApi(
    token="595349d95819413e2899d177b499fb6071fef51528117729b3b6bd9756dab86fe7be957cec942e26a19d4"
)

vkU = vk_session.get_api()

jsonResponse = vkU.newsfeed.getRecommended()

json_object = json.dumps(jsonResponse, indent=2)

with open("posts.json", "w", encoding="utf8") as file:
    file.write(json_object)

items = jsonResponse.get("items")

for item in items:
    if item.get("source_id") is not None:
        post = Post(item)
        string = f"\nPost:  {post.post_id}\n" + f"Post text: {post.text}\n" + f"Post likes count: {post.likes_count}\n"

        with open("posts.txt", "a", encoding="utf8") as f:
            f.write(string)
#
profiles = jsonResponse.get("profiles")
for profile in profiles:
    user = User(profile)
    string = f"\nAuthor name: {user.first_name} {user.last_name}\n"
    with open("posts.txt", "a", encoding="utf8") as f:
        f.write(string)
