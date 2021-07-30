# Screenshot Manager
Moves screenshots to an archive folder on a schedule so you can clear the clutter.

# Install
* Create a screenshot directory wherever you'd like it and change the corresponding variables in the ScreenshotManager.py file
* Add a cron job using `crontab -e` with the contents `0 * * * * python3 /Users/derekwebb/dev/screenshot-manager/ScreenshotManager.py &> /Users/derekwebb/dev/screenshot-manager/ScreenshotManager.log"`
* On Mac you may need to do grant full disk access to cron

# Granting Full Disk Access to cron
Reference link: https://blog.bejarano.io/fixing-cron-jobs-in-mojave/

Go to System Preferences > Security & Privacy > Privacy > Full Disk Access:open system settings, go to the security and privacy section, on the privacy tab, click on the full disk access item

Click on the (+) icon to add an item to the list

Press command+shift+G to open the Go to Folder… dialog, type /usr/sbin/cron and press Enter:open the go-to-folder dialog and search for /usr/sbin

Select the cron file and click Open:select /usr/sbin/cron

That’s it! Now my script can access my user’s $HOME/Library folder and all its contents!click ok

Warning: this is not a great idea security-wise, if a malicious actor can create cron jobs or edit the scripts ran as cron jobs, he or she would have Full Disk Access too. Monitor the system’s installed cron jobs manually or with a tool such as KnockKnock and proceed with caution.