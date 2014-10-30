one
===

Easy MediaFire file management from the command line.

###Installation
[Create MediaFire account](https://www.MediaFire.com/ssl_login.php)  
Follow the MediaFire instructions to install the [Python SDK](https://github.com/roman-yepishev/MediaFire-python-open-sdk)   
Install Python [xattr library](https://pypi.python.org/pypi/xattr)  
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
Run "one push [files]" to upload files to a MediaFire account  
  You can specify a path on MediaFire. e.g. "one push test1.txt -p MediaFire_Folder_1/MediaFire_Folder_2"  
Ex: "$one push test1.txt test2.docx" will upload test.txt and test2.docx to the signed in account  

####"one pull"
Run "one pull [files]" to download files from a MediaFire account  
  You can specify a path on MediaFire. e.g. "one pull MediaFire_Folder_1/MediaFire_Folder_2/test1.txt"  
Ex: "$one pull test1.txt test2.docx" will download test.txt and test2.docx to the current folder  

####"one diff"
Run "one diff [files]" to see if the remote or local file is more up to date
  You can specify a path on MediaFire. e.g. "one diff test1.txt -p MediaFire_Folder_1/MediaFire_Folder_2/test1.txt"  
Ex: "$one diff test1.txt -p MediaFire_Folder_1/test1.txt" will state if the file on MediaFire is more or less up to date than the local file  

####"one share" (Soon to be deprecated)  
Run "one share [files]" to receive the direct download link to a file and optionally email that link to anyone  
  
####"one list"  
Run "one list" to receive a list of the files currently stored on the signed in MediaFire account  
  You can specify a path on MediaFire. e.g. "one list MediaFire_Folder_1/MediaFire_Folder_2/"  

####"one del"  
Run "one del [files]" to delete a file from MediaFire    
Ex: "$one del test1.txt test2.docx" will delete test1.txt and test2.docx from the signed in MediaFire account  
  You can specify a path on MediaFire. e.g. "one del MediaFire_Folder_1/MediaFire_Folder_2/test1.txt"  
