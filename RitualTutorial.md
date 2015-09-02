# The Basic Syntax #
The basic syntax of a factoid:
<font color='blue'>~factoid</font> <font color='red'>create</font> <font color='orange'>factoid name</font> <font color='lime'>Do something</font>
  * Make sure which trigger your bot used to (for example "~" ">" "`_`")
  * Use <font color='red'>create</font> for creating a new factoid, <font color='red'>replace</font> to replace an existing factoid or <font color='red'>delete</font> to delete it
### Example ###
<table><tr>
<td> <b>Code:</b> </td><td> <b>Comment:</b> </td>
</tr><tr>
<td><pre><code><br>
&lt;schrottplatz&gt; ~factoid create test Hello World!<br>
&lt;Marlen_Jackson&gt; Factoid test created.<br>
&lt;schrottplatz&gt; ~test<br>
&lt;Marlen_Jackson&gt; Hello World!<br>
&lt;schrottplatz&gt; ~factoid delete test<br>
&lt;Marlen_Jackson&gt; Factoid test deleted.<br>
</code></pre></td>
<td>
<pre><code><br>
create the new factoid<br>
the bot acknowledges the new factoid without an Error message<br>
call the factoid<br>
the bot executes the function<br>
lets clean everything up again :)<br>
and we are done :D<br>
</code></pre>
</td></tr></table>

# Functions #
in ritual the functions are called like this:
|{ | function |`|` Parameter1 |`|` Parameter2 | ... | } |
|:-|:---------|:--------------|:--------------|:----|:--|
|the { start a new function | the function name | most functions need parameters | another parameter | Parameters are seperated by `|` | the } close the function again |

### Function Example ###
<table><tr>
<td> <b>Code:</b> </td><td> <b>Comment:</b> </td>
</tr><tr>
<td><pre><code><br>
&lt;schrottplatz&gt; ~factoid create test {action}slaps schrottplatz with an old green fish<br>
&lt;Marlen_Jackson&gt; Factoid test created.<br>
&lt;schrottplatz&gt; ~test<br>
* Marlen_Jackson slaps schrottplatz with an old green fish<br>
&lt;schrottplatz&gt; ~factoid delete test<br>
&lt;Marlen_Jackson&gt; Factoid test deleted.<br>
</code></pre></td>
<td>
<pre><code><br>
in this case the function "action" doesnt need any parameters<br>
the bot acknowledges the factoid<br>
call the factoid<br>
the bot executes the function<br>
lets clean everything up again :)<br>
and we are done again :D<br>
</code></pre>
</td></tr></table>
a list with all functions is available via `~help functions` or the [Functions list](FactoidFunctions.md)

### Workflow Example ###
Now i want to show you my workflow.
At fist I run a `~help functions` to check what could be the function, that I need. Then I run a `~help functions <function name>` for further information.
In this example I want to create a List of members. This was how I searched the function:
```

<schrottplatz> ~help functions

<Marlen_Jackson> [...]
---> Subpages ("~help functions <pagename>" to show a page):
---> ifneq   ignore   import   indexof   intcompare   isfuture   isop   javadoc   kick
lastindexof   length   lget   lgvars   listhttp   listresources   llvars   longrandom   lower   lpvars   lset   match   members   mode   n   numberlist   override
pad   pastebin   pdelete   pget   pset   radix   random   randomint [...]

<schrottplatz> ~help functions members
<Marlen_Jackson> Syntax: {members|<channel>} -- Evaluates to a space-separated list of the nicknames of the people that are currently in <channel>.
```
<table><tr>
<td> <b>Code:</b> </td><td> <b>Comment:</b> </td>
</tr><tr>
<td><pre><code><br>
&lt;schrottplatz&gt; ~factoid create memberlist<br>
Members in the channel ##jzbot: {members|##jzbot}<br>
&lt;Marlen_Jackson&gt; Factoid memberlist created.<br>
&lt;schrottplatz&gt; ~memberlist<br>
&lt;Marlen_Jackson&gt; Members in the channel ##jzbot: Marlen_Jackson ChanServ MrDudle schrottplatz<br>
&lt;schrottplatz&gt; ~factoid delete memberlist<br>
&lt;Marlen_Jackson&gt; Factoid memberlist deleted.<br>
</code></pre></td>
<td>
<pre><code><br>
What I did now was actually just pasting {members|&lt;channel&gt;}<br>
and changing &lt;channel&gt; to the channel ##jzbot<br>
the bot acknowledges the factoid<br>
now I call the factoid<br>
the bot executes the function... and everything worked great<br>
lets clean everything up again :)<br>
and we are done again :D<br>
</code></pre>
</td></tr></table>

# Variables #
There are two different types of Variables in ritual:
  * Channel based variables
  * Global variables

## Channel Based Variables ##
<table><tr>
<td> <b>Variable:</b> </td><td> <b>Description:</b> </td>
</tr><tr>
<td><pre><code><br>
%1% %2% ... or %1-% %2-%<br>
</code></pre></td>
<td>
<pre><code><br>
These are used as parameters for your function %(x)% would be the (x) Parameter. %(x)-% would be everything after (x).<br>
</code></pre>
</td></tr></table>
### Variable Example 1 ###
```

<schrottplatz> ~factoid create parameters first parameter: %1% | second parameter: %2% | everything below: %3-%
<Marlen_Jackson> Factoid parameters created.
<schrottplatz> ~parameters foo bar hello world! how are you?
<Marlen_Jackson> first parameter: foo | second parameter: bar | everything below: hello world! how are you?
<schrottplatz> ~factoid delete parameters
<Marlen_Jackson> Factoid parameters deleted.
```

<table><tr>
<td> <b>Variable:</b> </td><td> <b>Description:</b> </td>
</tr><tr>
<td><pre><code><br>
%0%<br>
%self%<br>
%source% / %channel%<br>
</code></pre></td>
<td>
<pre><code><br>
The nick of the person who called the function<br>
The nick of the bot<br>
The channel where the factoid was called from / current channel<br>
</code></pre>
</td></tr></table>
### Variable Example 2 ###
```

<schrottplatz> ~factoid create call Hello %0%. My name is %self%. You are talking in the channel %source%.
<Marlen_Jackson> Factoid call created.
<schrottplatz> ~call
<Marlen_Jackson> Hello schrottplatz. My name is Marlen_Jackson. You are talking in the channel ##jzbot.
<schrottplatz> ~factoid delete call
<Marlen_Jackson> Factoid call deleted.
```
## Global Variables ##
Global variables can be set by yourself using the {set`|``|``<`varname>`|``|``<`value>}
and called using `$varname$` or {get`|``|``<`varname>}


# Call Factoids Using A Factoid #
You can do that using the {import`|``|``<`factoid>`|``|``<`argument1>|...}
You can return values directly or using variables.
### Factoid Example ###
```

<schrottplatz> ~factoid create return1 {eval||%1%+%2%}
<Marlen_Jackson> Factoid return1 created.
<schrottplatz> ~factoid create return2 {set||returnvalue||{eval||%1%+%2%}}
<Marlen_Jackson> Factoid return2 created.
<schrottplatz> ~factoid create add Normal return: {import||return1||%1%||%2%} Return using a Variable: {import||return2||%1%||%2%}$returnvalue$
<Marlen_Jackson> Factoid add created.
<schrottplatz> ~add 3 4
<Marlen_Jackson> Normal return: 7 Return using a Variable: 7
<schrottplatz> ~factoid delete add
<Marlen_Jackson> Factoid add deleted.
<schrottplatz> ~factoid delete return1
<Marlen_Jackson> Factoid return1 deleted.
<schrottplatz> ~factoid delete return2
<Marlen_Jackson> Factoid return2 deleted.
```

# Tips #
Here a few tips below:
## The Functionlist ##
At [FactoidFunctions](FactoidFunctions.md) you can find all available functions.
## Escaping ##
If you have strings, which are used in the normal Ritual language, then you have to escape using a '\'.
### Escape Example ###
without escaping:
```

~factoid create emoticon >($.$)<
<Marlen_Jackson> Factoid emoticon created.
<schrottplatz> ~emoticon
<Marlen_Jackson> >()<
```
with escaping:
```

<schrottplatz> ~factoid replace emoticon >(\$.\$)<
<Marlen_Jackson> Factoid emoticon replaced.
<schrottplatz> ~emoticon
<Marlen_Jackson> >($.$)<
<schrottplatz> ~factoid delete emoticon
<Marlen_Jackson> Factoid emoticon deleted.
```
## Think Before Coding ##
Maybe it sounds stupid but think before you code! If you have no plan you have to change x functions every minute.
## IRC Support ##
You can get help at our official channel <a href='irc://irc.freenode.net/##jzbot'>irc.freenode.net/##jzbot</a>
## Requests ##
You need a factoid function? Just ask in our channel or [report](http://http://code.google.com/p/jzbot/issues/list) a request.