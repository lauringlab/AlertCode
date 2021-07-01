# hades and the #underworld

### System:

In the Lauring Lab Slack, there is a channel called \#underworld. This channel has a bot associated with it, called "hades".

hades can be used to automate messaging after or during code-sets.

### Current Files:

* count_samples.py: This alert code set counts the number of rows in the full_compiled_data.csv file. The message is: "From plate runs dated str(min(samples['PlateDate']))[0:10] to str(max(samples['PlateDate']))[0:10], total COVID-19 samples sequenced = samples.shape[0]"

    * full_run_code.R has a batch file call for this code set.

### Set-Up

1) Create a folder on your local computer, specifically for this code and associated files.

2) In that folder, you should have:
    * Downloaded count_samples.py (or whichever alert code set(s) you'd like)

    * A text file called hades_info.txt - this should contain the bot/channel url associated with hades WITH single quotes around the url (ex. 'https://hooks.slack.com/services/ABC001/DEF001/GHI001')

3) Open count_samples.py and edit the file paths on line 14 (should point to hades_info.txt) and line 21 (should point to full_compiled_data.csv) and save the file.

4) Create a batch file.
    * Open a text editor to a new file (atom, notepad, etc.)

    * Include the following text on one line:
        > <path to python> <path to count_samples.py>

    * For example, mine looks like:
        > "c:\users\juliegil\appdata\local\programs\python\python38\python.exe" "C:\Users\juliegil\Documents\UofM_Work\Lab_Organization\AlertCode\count_samples.py"

    * Save the file as sample_count_run.bat (or whatever you like, you just need to include the .bat ending) in the folder you created in step 1.

5) Open full_run_code.R and edit line 9 (file path to your folder in step 1) and line 29 (name of your batch file)

### Required Libraries

Python:

* json - https://docs.python.org/3/library/json.html#
* requests - https://docs.python-requests.org/en/master/
* pandas - https://pandas.pydata.org/
