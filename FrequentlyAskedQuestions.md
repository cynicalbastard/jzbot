This document contains some commonly-asked questions about JZBot and answers for those questions. There are a couple of things to remember when reading this page:
  * JZBot's factoid language is called **Fact**, and is referred to by that name within this page.
  * A **pm**, when used on this page, refers to a message sent directly to the bot instead of at a channel or a chat room. Some people also know this as **querying**. Most IRC clients let you send these with `/msg <person> <message...>`, where `<person>` is the person to send to and `<message>` is the message to send. People that chat over GMail or Facebook almost exclusively use <i>pm</i>s to chat; Indeed, Facebook **only** allows chatting with <i>pm</i>s. pm is short for Private Message.
  * **JZBot** and **Marlen**/**Marlen Jackson**/_etc._ do not mean the same thing. There's a FAQ question on that below; If you don't know the difference between these, you should probably read it.

## Table of Contents ##



## Is there a way to get the process id (pid) of a bot by messaging it? ##
There is. Send `exec {mbean|java.lang:type=Runtime|Name}` to your bot in a pm, and it will respond with `pid@host`, where pid is the process id. You must be a superop to do this.

## Where did the name "JZBot" come from? ##
The JZBot project was started by [javawizard](People#Alex.md). Javawizard had attained the nickname "javawiz" on IRC before he switched nicknames to jcp. The "JZ" in JZBot's name comes from "JavawiZ". The "Bot" part should be obvious.

## How fast is JZBot's Fact interpreter? ##
First off, Fact was not designed to be fast; it was designed to be concise and easy-to-use. That said, JZBot's Fact interpreter is not the slowest thing around. Below are some benchmarks that were run on a Sony Vaio VGN-FZ298CE with a 1.66GHz Intel Core 2 Duo and 3GB of RAM (of which JZBot used about 4MB). Each benchmark is given as a Fact program, a short explanation of what it does, and the average execution time over 5 runs. This can also be used as a general reference as to which functions perform the fastest.

Parse time is the amount of time it took the fact interpreter to parse the factoid into its internal representation, and usually corresponds to the length, in characters, of the factoid and the number of `{` sequences present in the factoid. Run time is the time the factoid actually spent running.

All times are given in milliseconds.

<table cellpadding='1' border='1' cellspacing='0'><tr><th>Fact program</th><th>Description</th><th>Output</th><th>Parse time</th><th>Run time</th><th>Total</th></tr>

<tr>
<td><code>Hello world</code></td>
<td>Prints out a simple piece of text.</td>
<td>Hello world</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>

<tr>
<td><code>{split| |{numberlist|1|5}|v|%v%| -- }</code></td>
<td>Iterates over the numbers 1 through 5.</td>
<td>1 -- 2 -- 3 -- 4 -- 5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>

<tr>
<td><code>{split| |{numberlist|1|10000}|v|%v%| -- }</code></td>
<td>Iterates over the numbers 1 through 10,000 using a split loop.</td>
<td>1 -- 2 -- 3 -- <i>etc.</i> -- 9998 -- 9999 -- 10000</td>
<td>1</td>
<td>22</td>
<td>23</td>
</tr>

<tr>
<td><code>{for|1|10000|v|%v%| -- }</code></td>
<td>Iterates over the numbers 1 to 10,000 using a for loop.</td>
<td>1 -- 2 -- 3 -- <i>etc.</i> -- 9998 -- 9999 -- 10000</td>
<td>0</td>
<td>7</td>
<td>7</td>
</tr>

<tr>
<td><code>Hello world</code></td>
<td>Prints out a simple piece of text.</td>
<td>Hello world</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>

</table>

## Is there a limit on the size of the call stack when executing factoids? ##
Technically, no, but practically, yes. The interpreter and Fact itself do not impose a stack depth limit, but Java does, and every Fact stack frame (a stack frame being where a factoid imports another factoid) adds 11 Java stack frames. Running some tests on the same machine as the benchmarks of the previous question with the factoid `rtest` having the contents `{pset|rvalue|%1%}{import|rtest|{eval|%1%+1}}` and being invoked as `rtest 0`, I was able to get 483 Fact stack frames before a stack overflow occurred. This might differ depending on the Java VM you're using and the settings you use when running the Java VM. I hope to include a factpack in JZBot in the future that will benchmark this on any given JZBot.

So, in essence, the Fact interpreter is only limited by the Java platform on which it is running. JZBot catches all stack overflow errors, however, so if one does occur, it will be reported to the user the same as any other factoid syntax error, and will not cause the bot to crash.

## Is there a limit on how many servers a bot can be connected to? ##
There isn't any built-in limit. However, the maximum number of servers is generally constrained by available memory and limits of the JVM. A practical limit is 200 servers, although I highly doubt anyone would ever need that many connections.

For the technically inclined, each server tends to take up around 1KB in the database (in addition to any factoids and other information added at that sever). An IRC connection starts two threads, a BZFlag connection starts four threads, and an XMPP connection start a number of threads that I haven't currently investigated, although I think it's approximately 3 threads. Facebook Chat uses XMPP, so it would have the same number of threads, but Facebook External will most likely use 1 thread.

## Is there a limit on how many plugins can be loaded? ##
As with the previous two questions, there isn't such a fixed limit, but each plugin is run in its own process (which means it takes up some memory), and each plugin uses a TCP socket connection, so the operating system JZBot is being run on can end up enforcing a practical limit. A good value would be to keep loaded plugins at less than 50.

## Does JZBot support IPv6? ##
Yes! We fully support the 'new' version of IP, and can connect and similar, just as you would with IPv4.

## I've heard the terms "JZBot", "Marlen", "Marlen Jackson", "multimarlen", "devmarlen", and others, used when discussing things related to JZBot. What's the difference between all of these? ##
The JZBot developers, [Alex](People#Alex.md) included, have an unfortunate tendency to get these constantly mixed up. So we might refer to one when we mean the other. But technically, they mean these things, respectively:
  * **JZBot** is the name used for the entire project, and the program itself that the project has created.
  * **Marlen** generally refers collectively to the group made up of Marlen Jackson, multimarlen, and devmarlen, although the developers sometimes use it informally to refer specifically to one of those, and sometimes to refer instead to JZBot.
  * **Marlen\_Jackson** is a collection of 3 specific installations of JZBot residing on [Alex](People#Alex.md)'s server, connecting to three different IRC networks. They run [revision 929](http://code.google.com/p/jwutils/source/detail?r=929) of JZBot, which is extremely outdated. Once all content has been moved from them to multimarlen, they will be shut down, and multimarlen will most likely be renamed to Marlen\_Jackson. Note here, however, that Marlen Jackson on Facebook is actually multimarlen, **not** Marlen\_Jackson; see below.
  * **multimarlen** is an installation of JZBot residing on Alex's server that is generally kept up-to-date with all of the latest features. Alex generally updates multimarlen at least once per week. multimarlen, unlike Marlen\_Jackson, can connect to multiple severs and can connect over protocols other than IRC. Marlen Jackson on Facebook is actually multimarlen; The account was just created back when only Marlen\_Jackson existed and there wasn't a multimarlen, which is why it was named Marlen Jackson.
  * **devmarlen** is an installation of JZBot residing on Alex's laptop. Indeed, it runs off of the exact same files Alex develops on, and thus devmarlen always has the newest features that the JZBot team, and Alex in particular, has written.
  * **schrottbot** is an installation of JZBot residing on Max's laptop in much the same way that devmarlen resides on Alex's laptop. As such, schrottbot always has the newest features that the JZBot team, and Max in particular, has written.
All of the bots join [the JZBot chat room](ChatRoom.md) under their respective nicknames.
To the JZBot developers: If any of the bots run by developers (anyone on the JZBot commit list) are missing here, tell Alex at #jzbot.
## What should I do if I have a question that's not on here? ##
Ask it, by all means! Log in with your Google account (see that **Sign In** link in the upper-right corner; you'll need a Google account to ask a question), and then fill out [this form](http://code.google.com/p/jzbot/issues/entry?template=Question). We'll get back to you shortly. Or you could join our [chat room](ChatRoom.md) and ask us directly.