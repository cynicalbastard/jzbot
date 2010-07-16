# This file is used to configure JZBot. It should be located in the storage
# folder, and it should be named "config.py". If this file is named
# "default-config.py" and is located in a folder named "files", then you're
# reading the wrong file, and you should look for the one in the storage
# folder instead.
#
# Since you're still reading, I'll assume that this really is "config.py".
# So, you use this file to configure some things about JZBot.
#
# First, JZBot uses MongoDB to store its information. You'll need to specify
# in this file the name of the MongoDB database you want to use. You'll need
# MongoDB installed and running on your computer before you can start JZBot.
#
# So, specify the name of the database on the next line, in the double-quotes.
# The database name cannot contain any double quotes (but I'm fairly certain
# MongoDB doesn't allow that anyway). Yes, the "r" right before the first
# quote is intentional and should be left alone unless you know what you're
# doing. The default database name is jzbot.
database_name = r"jzbot"

# That's it for configuration options right now. The next line, "exit = True",
# tells JZBot that it should stop and issue a message that you haven't
# edited this file yet. Once you've edited this file and specified a database
# name above (or once you're sure you want to leave it as the default), you
# should delete the "exit = True" line so that JZBot can actually run.
exit = True
 