Want to run you own JZBot, but not sure how to get started? You're at the right place. Read on.

**One quick note first**, and this is a rather technical one, so just skip this paragraph after reading the first sentence or so if it confuses you. I promise the rest of this tutorial isn't this confusing. Anyway, JZBot currently works on Linux, Mac OS X, and Windows (for most things). You should know that I assume you're using a Linux distribution that uses apt-get (such as Ubuntu and Debian); you might need to do some googling if you're not on such a distribution.

# Installing #

Anyway, let's get started. The first thing we need to do is download some programs that you'll need to run JZBot:
  * JZBot is written in a programming language called Java, so you'll need Java on your computer.
    * If you're on **Linux**, open a terminal and type "sudo apt-get install sun-java6-jdk". If you're on another distro, then I'll be getting instructions for you soon, but a simple google search should get you the information you need. Just make sure to install at least Java 6 (or Java 1.6) or later.
    * If you're on **Mac OS X**, you don't need to do anything; all macs come with Java installed.
    * If you're on **Windows**, you'll need to download and install the [Java Developer Kit](http://java.sun.com/javase/downloads/widget/jdk6.jsp).
JZBot is stored in a Subversion repository (you don't need to know what that means), so you'll need Subversion to download JZBot.
    * If you're on **Linux**, open a terminal and type "sudo apt-get install subversion".
    * If you're on **Mac OS X**, you don't need to do anything; all macs come with Subversion installed. If your mac doesn't have Subversion installed, get in touch with one of the JZBot developers and tell them this.
    * If you're on **Windows**, you don't need to do anything; the installer comes with an SVN client.

## For Linux and Mac OS X ##
Now you're ready to actually download JZBot. Open a terminal and cd to the folder that you want JZBot to be stored in. If you have no clue what that means, then just type these commands:
```
mkdir jzbot
cd jzbot
```
Those commands will create a folder called "jzbot" where we'll download JZBot to.

Now, run these commands, replacing `<nick>` with a nickname you want for your bot, and `<hostname>` with your hostname or hostmask on IRC (read <a href='#Hostname'>here</a> if you don't know what your hostname is):
```
svn co http://jwutils.googlecode.com/svn/trunk/projects/jzbot2-old .
./build
./jzbot addserver freenode irc irc.freenode.net 6667 <nick> <hostname>
./jzbot
```
The first command will take a long time to run, and will download JZBot. The second command should print `BUILD SUCCESSFUL` when it's done; if it prints `BUILD FAILED` instead, get in touch with the JZBot developers and ask them for more help, since this indicates a serious problem. The third command should take a couple of seconds to run, and print a message about a new server being added after it's done. The fourth command won't finish running; it actually runs JZBot and won't stop running until you shut down your bot.

## For Windows ##
Now you're ready to actually download JZBot. Go to the Downloads page on this website, and download the file [WindowsInstaller.zip](http://jzbot.googlecode.com/files/WindowsInstaller.zip). Extract this to the folder you want to run JZBot and double click on "install.bat". This program will install and configure JZBot for you after you specify what nickname you want it to use and what your hostname is. To start it in the future, double click on the file named jzbot.bat


---


Now, connect to irc.freenode.net, and send this in a direct message to your bot (which will now be using the nickname `<nick>`, where `<nick>` is the nickname you used in the sequence of commands above):
```
join #jzbot
```
This will instruct your bot to join the channel #jzbot. You're welcome to leave your bot there; #jzbot welcomes spam related to bot development, so don't worry about excessive message sending. You're not required to leave your bot there, however, and we'll get to how you can have your bot leave #jzbot if you want to later on.

# Additional Notes #

## Hostname ##
If you don't know what your hostname is on a particular IRC server, you can find out by signing on to the IRC server, and running "/whois `<yournick>`", where `<yournick>` is your nickname on the IRC server. One of the lines sent back to you will contain some text of the format "user@host". `host` is your hostname.

The server that this tutorial connects you to is the Freenode Chat Network; to find out your hostname there, you would connect to irc.freenode.net.