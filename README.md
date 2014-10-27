one
===

Easy file Mediafire file management from the command line.

###Installation
[Create Mediafire account](https://www.mediafire.com/ssl_login.php)  
Follow the [Mediafire instructions](https://github.com/roman-yepishev/mediafire-python-open-sdk) to install the Python SDK  
git clone https://github.com/cdpetty/one.git ~/One

Add this line to your bashrc (or zshrc, etc):
alias one="python3 ~/One/one.py"

###Documentation
Explanation of the various commands

####"one init"
Run "one init" to sign into one for the first time

####"one out"
Run "one out" to sign out of one

####"one change"
Run "one change" to switch users

####"one push"
Run "one push [files]" to upload files to a Mediafire account
Ex: "$one push test1.txt test2.docx" will upload test.txt and test2.docx to the signed in account

####"one pull"
Run "one pull [files]" to download files from a Mediafire account
Ex: "$one pull test1.txt test2.docx" will download test.txt and test2.docx to the current folder

####"one diff"
Run "one diff [files]" to see if the remote or local file is more up to date
Ex: "$one diff test1.txt" will state if the file on Mediafire is more or less up to date than the local file

####"one share"
Run "one share [files]" to receive the direct download link to a file and optionally email that link to anyone

####"one list"
Run "one list" to receive a list of the files currently stored on the signed in Mediafire account

####"one del"
Run "one del [files]" to delete a file from Mediafire
Ex: "$one del test1.txt test2.docx" will delete test1.txt and test2.docx from the signed in Mediafire account
