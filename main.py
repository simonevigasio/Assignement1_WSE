from mastodon import Mastodon, StreamListener
import re

with open("usercred.secret", "r") as f:
    access_token = f.readline().strip()

mastodon = Mastodon(
    access_token=access_token,
    api_base_url="https://mastodon.social"
)

def clean_html(html):
    return re.sub("<.*?>", "", html)

class Listener(StreamListener):
    def on_update(self, status):
        author = status["account"]["acct"]
        text = clean_html(status["content"])
        url = status["url"]

        print("\n----------------------------------")
        print(f"AUTHOR: {author}")
        print(f"TEXT: {text}")
        print(f"URL: {url}")
        print("----------------------------------", flush=True)

    def on_delete(self, status_id):
        # ignore deletes
        pass

    def on_error(self, error):
        print("ERROR:", error, flush=True)

listener = Listener()
mastodon.stream_public(listener)