# Ulysses S. Grant Select
A Slack bot that grants select permission on a table in Redshift.

<img src="images\grant.jpg" alt="grant" style="zoom:50%;" />

> "I'd rather be GRANTING" 
>
> -- Ulysses S. Grant Select



## Using the application

Usage: first, download the App from the following url: https://ruggable.slack.com/apps/A02G0GTLUE4-ulysses-s-grant-select?next_id=0

If you are the administrator of the app, you will need to add collaborators to the app configuration.

Then, issue the following command in the Slackbot channel: `/grant your-redshift-username schemaname.tablename`. The program checks if the username provided has usage on the provided schema. If it does, it tries to grant select on the table.

Future functionality should include granting access to all tables within a given schema, as well a restrictions on which users a Slack account can grant select to. An open pull request provides functionality for asynchronous granting, which should be fun to try out. Early results have been positive.

## Running the application

Spinning up the app is a bit more difficult. You'll need SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET from the app administration page, then set the appropriate values as environment variables. You'll also need to expose port 3000-3030 for incoming traffic, so any elastic IP that is attached to the microinstance needs to be adjusted accordingly. 

Once inside the us-grant-select repository on your microinstance, simply run `nohup python3 app.py`. `nohup` enables you to exit this bash terminal and return to it, so that a) the process runs in the background and b) you can exit the Putty ssh session. 

`nohup` puts all the logs from a process's run in `nohup.out`. This can be useful for diagnosing how the application last failed, if it is in fail state. If the process is in fail state, ensure that you kill the process using `kill <PID>` before relaunching the application.
