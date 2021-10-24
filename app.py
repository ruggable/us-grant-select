import os
from slack_bolt import App

from libs.redshift import handle_grant

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command("/grant")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    username, *tablename = command['text'].split()
    handled = handle_grant(username, tablename[0])
    if handled:
        respond(f"You've just been GRANTED.\nI've just PRESERVED the UNION between you and {tablename[0]}.")
    else:
        respond(f"grant {command['text']}? Nope, nope I won't do that.")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))