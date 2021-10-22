# Ulysses S. Grant Select
A Slack bot that grants select permission on a table in Redshift.



Usage: first, download the App from the following url: https://ruggable.slack.com/apps/A02G0GTLUE4-ulysses-s-grant-select?next_id=0



Then, issue the following command in the Slackbot channel: `/grant [user] [schema.table]`.



Spinning up the app is a bit more difficult. You'll need SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET from the app administration page, then set the appropriate values as environment variables. Currently, the app is running using ngrok, but will eventually be deployed to a Linux microinstance. Enjoy!
