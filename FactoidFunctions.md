<a href='Hidden comment: Paste this into the "FactoidFunctions" page. Dont forget the Navigation (run ~jzwikinav)'></a>
# Functions #
## action ##
> Syntax: {action} -- Causes the factoid to appear using "/me". It essentially causes the bot to do the equivalent of prepending the message with "/me" on a typical IRC client.
## addregex ##
> Syntax: {addregex`|``<`desc>} -- Adds a regex to the current channel. This acts as if "regex add `<`desc>" has been run at this channel.
## afterpad ##
> Syntax: {afterpad`|``<`number>`|``<`char>`|``<`value>} -- Evaluates to `<`value>, but with `<`char> (which must be a single character) appended until the resulting length is at least equal to `<`number>. For example, {pad`|`7`|`0`|`1234} would evaluate to "1234000".
## args ##
> Syntax: {args`|``<`regex>`|``<`text>} -- Splits `<`text> around the regular expression `<`regex>, then runs the function named by the first string in this sublist, passing the rest of the strings as arguments. For example, "{args`|`,`|`sendmessage,%0%,Hello}" would function exactly the same as "{sendmessage`|`%0%`|`Hello}", assuming %0% does not contain any commas.
## ascii ##
> Syntax: {ascii`|``<`char>} -- Evaluates to the numerical code that represents the ascii character `<`char>. For example, {ascii`|` } results in "32", {ascii`|`1} results in "49", and {ascii`|`A} results in "65". An error will occur if `<`char> is not a single character.
TODO: Right now, this function, instead of returning the ascii char value, returns the value of the character in whatever charset you've configured the bot with.
## b ##
> Syntax: {b} -- Inserts the IRC bold character, which causes all following text to be shown as bold.
This function is deprecated, and "\b" should be used instead.
## bf ##
> Syntax: {bf`|``<`code>`|``<`input>`|``<`size>} -- Executes `<`code> as BF code and evaluates to whatever the code outputs. The memory bank provided to the code is `<`size> positions. `<`size> is optional, and will be 1024 if not present. Each position is a 32-bit signed integer. `<`input> is also optional, and, if present, provides textual input to the bf program.
## bzflist ##
> Syntax: {bzflist`|``<`prefix>`|``<`action>`|``<`delimiter>} -- Contacts the public BZFlag list server and retrieves a list of all servers. For each server, `<`action> is then invoked, with several variables starting with "`<`prefix>-" set. The best way to get a list of all of these variables is to run {bzflist} with the action being {llvars`|``<`prefix>-}.
If the action sets a variable called `<`prefix>-quit to the value "1", {bzflist} will stop iterating over servers and return immediately. {bzflist} evaluates to what its actions evaluated to, separated by `<`delimiter>. Unlike most iterating functions, "`<`prefix>-" variables set during iteration will not be deleted afterward.
## bzfquery ##
> NOT IMPLEMENTED YET. When this is implemented, it will connect to the specified bzflag server and pull some stats from it, such as the list of players that are there, the current team scores, and so on.
## c ##
> Syntax: {c} -- Inserts the IRC color change character. Immediately following this should be two digits, which represent the color of text that should show up.
Create a factoid with the text "{split`|` `|`{numberlist`|`1`|`15}`|`c`|`{c}{lset`|`c`|`{pad`|`2`|`0`|`%c%}}%c%%c%`|` }" (without quotes), then run it; the result will be a list of numbers and the color they represent.
This function is deprecated, and "\c" should be used instead.
## cancel ##
> Syntax: {cancel`|``<`key>} -- Cancels the future task that was created with the specified key. If there is no such future task, nothing happens.
## cascade ##
> Syntax: {cascade`|``<`regex>`|``<`factoid>`|``<`argument1>`|`...} -- Identical to the {import} function, with one exception: any local variable in this factoid whose name matches the regular expression `<`regex> will be handed down to `<`factoid> when it is run. Note that changes to the variable inside that factoid will not prepegate up to this factoid. Also, special local variables (such as
%1% or %self%) can't be overriden with this function, meaning that they will be set to whatever they would be had {import} been used instead of {cascade}. As an example, "{import`|`testfact`|`something}" would function exactly the same as "{lset`|`1`|`something}{cascade`|`1`|`testfact}". However, using "{lset`|`1`|`something}{cascade`|`1`|`testfact`|`other}", "testfact" would have %1% equal to "other", not "something".
## catch ##
> Syntax: {catch`|``<`action>`|``<`prefix>`|``<`onerror>} -- Evaluates to `<`action>. If `<`action> ends up throwing an exception, `<`onerror> is run instead. A few local variables are set if an error does occur. Their names are `<`prefix>-class, which is the name of the class of the error (this is usually jw.jzbot.fact.FactoidException), `<`prefix>-message,
which is the error message of the exception, and `<`prefix>-root-class and `<`prefix>-root-message, which are the class and message of the root cause of the exception. This function will catch all errors (including too-many-message and too-many-import errors) except an error indicating that the factoid used up too much time, for the
obvious reason that this could lead to factoids that never stop running. This will not allow for circumvention of the message limit, however, as each successive invocation of {sendmessage} would just throw another error instead of sending a message if the quota has been exceeded.
## cget ##
> Syntax: {cget`|``<`varname>} -- Evaluates to the value of the specified chain variable.
## char ##
> Syntax: {char`|``<`number>} -- Evaluates to a single character, which is the ASCII character denoted by the base-10 number `<`number>. For example, {char`|`32} results in " ", {char`|`49} results in "1", and {char`|`65} results in "A".
TODO: Right now, this actually converts the number to a character in the bot's current charset instead of in ASCII. Perhaps consider using two different functions for that, or a separate UTF-8 function.
## compare ##
> Syntax: {compare`|``<`first>`|``<`second>`|``<`case>`|``<`if>} -- Compares `<`first> with `<`second> to see which would come first in a dictionary. This function then evaluates to -1 if `<`first> comes before `<`second>, 0 if they are the same, and 1 if `<`first> comes after `<`second>. `<`case> and `<`if> are optional, and default to 1 and 0, respectively. When `<`case> is 1, case is taken into account (IE "A" comes before "a"), and when
it is 0, case is ignored (IE "A" and "a" are the same). When `<`if> is 1, this function evaluates to 0 instead of -1 if `<`first> comes before `<`second>, thereby making the output suitable for directly passing to the {if} function. When `<`if> is 0, -1, 0, and 1 are returned as specified above.
## comparesort ##
> Syntax: {comparesort`|``<`regex>`|``<`string>`|``<`delimiter>`|``<`prefix>`|``<`comparator>} -- Splits `<`string> around the regular expression `<`regex>, then applies a comparison sort to the resulting sublist. This comparison sort is currently a modified mergesort. Pairs of items are compared by setting the local variable `<`prefix>-1 to be the first value, and `<`prefix>-2 to be the second value, and then evaluating `<`comparator>.
The result of this evaluation should be negative, 0, or positive if the first item comes before, is the same as, or comes after, the second item, respectively. Once the list is sorted, {comparesort} evaluates to a `<`delimiter>-separated list of the sorted items.
## contains ##
> Syntax: {contains`|``<`substring>`|``<`string>} -- Evaluates to 1 if `<`string> contains `<`substring> anywhere in it, or 0 if it doesn't.
## count ##
> Syntax: {count`|``<`regex>`|``<`string>} -- Splits `<`string> around `<`regex>, and then counts the number of items in this list. This essentially counts how many times `<`regex> appears in `<`string>, and then returns this number plus 1, or 0 if `<`string> is empty. Trailing blank items are not counted.
## cset ##
> Syntax: {cset`|``<`varname>`|``<`value>} -- Sets the specified chain variable to the specified value. Chain variables are almost exactly the same as local variables; the only difference is that when a factoid imports another factoid, both factoids (and any that are in turn imported by the imported factoid) use the same set of chain variables.
## datasize ##
> Syntax: {datasize`|``<`size>} -- Formats `<`size>, which is a size in bytes, into a more human-readable format. For example, {datasize`|`12345} would result in "12.1KB".
## dateformat ##
> Syntax: {dateformat`|``<`value>} -- Formats `<`value>, which should be a number of milliseconds since Midnight January 1, 1970 UTC, as a human-readable date string. If you want a custom date format instead of the default one that this function provides, consider using {format} with a custom format string instead of {dateformat}.
## delete ##
> Syntax: {delete`|``<`varname>} -- Deletes the global variable named `<`varname>.
## error ##
> Syntax: {error`|``<`message>} -- Causes a syntax error to be reported with the specified message. If the error is later caught with {catch}, the exception class will be jw.jzbot.fact.CustomFactoidException and the message will be `<`message>.
## escape ##
> Syntax: {escape`|``<`text>} -- Escapes `<`text> with backslashes, "\n", and such, so that the resulting text, when embedded directly within a factoid, would evaluate to `<`text>. For example, all "|" characters, "{" characters, and "}" characters are prefixed with a "\". `<`text> can also contain non-ascii-visible characters, and these will
be replaced with a call to the {char} function. Currently, this doesn't correctly support UTF-8.
## eval ##
> Syntax: {eval`|``<`toeval>} or {eval`|``<`engine>`|``<`toeval>} -- Evaluates `<`toeval> as a mathematical equation. Engine specifies the engine to use. Each engine exhibits different properties and equation syntax.
Allowed engines are (separated by a space): jeplite caltech jeval
## exact ##
> Syntax: {exact`|``<`factoid>`|``<`arg1>`|``<`arg2>`|`...} -- Same as {import}, but imports the factoid at exactly the same scope as this factoid. If this is a global factoid, then this will end up calling the specified global factoid even if an equivalent, channel-specific factoid exists.
## example ##

## extensiontype ##
> Syntax: {extensiontype`|``<`name>} -- Evaluates to the content type of a number of known file extensions. If name does not contain any "." characters, it is taken to be the name of a file extension. If it does contain "." characters, the extension is taken to be everything after the last "." character.
For example, {extensiontype`|`txt} and {extensiontype`|`myfile.txt} both evaluate to "text/plain", and {extensiontype`|`gif} and {extensiontype`|`something.gif} both evaluate to "image/gif".
## factoverride ##
> Syntax: {factoverride} -- Only useful in a factoid called by a regex. Indicates that no other factoids should be run after this regex. This differs from {override} in that other regexes will still be run, but actual factoids will not. As with {override}, this does not block commands from running.
## facts ##
> Syntax: {facts`|``<`scope>} -- Returns a space-separated list of the names of all factoids in the scope that this factoid is in. If `<`scope> is "channel", and this is a global factoid, then this will list channel-specific factoids at whatever channel this is being run at. Otherwise, `<`scope> has no effect. `<`scope> is optional.
## filter ##
> Syntax: {filter`|``<`regex>`|``<`string>`|``<`condition>`|``<`delimiter>} -- Splits `<`string> around the regular expression `<`regex>, then reconstructs a string made up of these strings, but delimited by `<`delimiter>. Only substrings that match the regular expression `<`condition> will be included.
For example, {filter`|`,`|`first,second,third,fourth`|`<sup>[</sup>i]**$`|`-} would evaluate to "second-fourth".
## first ##
> Syntax: {first`|``<`arg1>`|``<`arg2>`|`...} -- Evaluates to the first argument that is not the empty string.
## firstvar ##
> Syntax: {firstvar`|``<`varname>`|``<`arg1>`|``<`arg2>`|`...} -- Sets the local variable `<`varname> to be the first argument that comes after it whose value does not evaluate to the empty string, ignoring whitespace and newlines.
## flip ##
> Syntax: {flip`|``<`text>} -- Flips the specified text upside-down. This involves reversing the text and substituting each letter for an equivalent character that is flipped upside-down. This only works correctly if UTF-8 is used as the charset.
## format ##
> Syntax: {format`|``<`formatstring>`|``<`arg1>`|``<`arg2>`|`...} -- Applies C-style printf formatting to `<`formatstring> with `<`arg1>, `<`arg2>, etc. being the format arguments. This could be considered an equivalent to C's printf(`<`formatstring>,`<`arg1>,`<`arg2>,...), but output, instead of being sent to stdout, is put into the factoid.
Arguments that can be parsed as whole numbers are passed to the formatting method as 64-bit signed integers. Arguments that can be parsed as fractional numbers (including numbers with a decimal point but that only have zeros after it) are passed as 64-bit floating point numbers. Other arguments are passed as strings.
## future ##
> Syntax: {future`|``<`key>`|``<`delay>`|``<`factoid>`|``<`argument1>`|`...} -- Schedules a factoid to be run some time in the future. `<`key> is a unique key. Whenever an event is scheduled for a particular key, any events that have been scheduled for that key but not yet run are canceled. `<`delay> is the number of seconds in the future that the factoid should be run.
`<`factoid> is the name of the factoid to run. `<`argument1>, `<`argument2>, etc. are arguments to pass to the factoid.
## futures ##
> Syntax: {futures} -- Evaluates to a newline-separated list of the keys of all future tasks scheduled with {future} that have not yet been run.
## get ##
> Syntax: {get`|``<`varname>} -- Gets the value of the global variable named `<`varname>.
## getresource ##
> Syntax: {getresource`|``<`name>} -- Gets the resource by the specified name. Resources are files present in the "resources" folder under the bot's main folder. If the resource's content is longer than 100KB, an error will occur.
## global ##
> Syntax: {global`|``<`factoid>`|``<`arg1>`|``<`arg2>`|`...} -- Same as {import}, but imports the specified global factoid only. This acts as if there were no channel-specific factoids named `<`factoid>, even if one does exist.
## google ##
> Syntax: {google`|``<`search>} -- Uses the Google search engine to search for `<`search>, and returns the results with each result separated with a "|" character. Each result is made up of the URL for that result, a space, and a summary of that result.
## hasfactdb ##
> Syntax: {hasfactdb`|``<`channel>} -- Evaluates to 1 if the specified channel has a fact database, or 0 if the specified channel does not have a fact database. A channel with a fact database is one at which channel-specific factoids can be created and run. A channel acquires a fact database when {join} is issued for that channel, but not
when {tempjoin} is issued for the channel. Currently, once a channel has a fact database, that channel's fact database cannot be removed. To see if a channel with a fact database is also an auto-join channel, use {isautojoin}. To see if the bot is actually on a channel, use {isat}.
## hash ##
> Syntax: {hash`|``<`text>} -- Computes a 32-character hash of the text specified. Specifically, the hash is the first 32 characters of a signed base-16 conversion of the bytes of the SHA-512 hash of `<`text>. The resulting text is guaranteed to be exactly 32 characters in length.
## help ##
> Syntax: {help`|``<`page>} -- Evaluates to the contents of the specified help page. `<`page> should be a page formatted so that sending "help `<`page>" to the bot in a pm would get the relevant help page. The resulting help page can contain newlines. If the specified help page does not exist, {help} evaluates to nothing.
{help`|`} evaluates to the contents of the top level help page (IE the one that you see if you pm "help" to the bot). Also, the literal string "%HELPCMD" may appear in the result, which should be translated to "~help" or "/msg Marlen\_Jackson help", depending on where the message was sent from.
## helplist ##
> Syntax: {helplist`|``<`page>} -- Evaluates to a space-separated list of all subpages of the help page `<`page>. This also means that you can get a space-separated list of all functions allowed in factoids by using {helplist`|`functions}. {helplist`|`} evaluates to a list of top-level help pages (IE those that you would see
if you sent "help" in a pm to the bot).
## hide ##
> Syntax: {hide`|``<`arg1>`|``<`arg2>`|`...} -- Does nothing, and evaluates to nothing. Specifically, this does not evaluate any of its arguments, so, for example, if you had an {lset} function call in one of the arguments, it would not be run and the variable would not be set. This function can be used to comment out some code in a factoid.
## htmldecode ##
> Syntax: {htmldecode`|``<`text>} -- Decodes all HTML-escaped characters in the specified text. This is the opposite of {htmlencode}.
## htmlencode ##
> Syntax: {htmlencode`|``<`text>} -- Escapes all HTML special characters in `<`text>. For example, "`<`" gets changed to "&lt;".
## i ##
> Syntax: {i} -- Inserts the IRC reverse character, which, depending on the client, either reverses the foreground and background colors or shows text as italic.
This function is deprecated, and "\i" should be used instead.
## identity ##
> Syntax: {identity`|``<`arg1>`|``<`arg2>`|`...} -- Evaluates to all of its arguments, concatenated and with a space inbetween. Essentially the same as "`<`arg1> `<`arg2> ...". This function is primarily intended for the factoid language interpreter's internal use but can be used in factoids as well.
## if ##
> Syntax: {if`|``<`condition>`|``<`trueaction>`|``<`falseaction>} -- Evalutes to `<`trueaction> if `<`condition> is one of the "true" values, and `<`falseaction> if `<`condition> is one of the "false" values. If `<`condition> is neither a true value nor a false value, it is interpreted as an equation (as if it were passed to {eval}), and then compared again.
The true values are y, yes, t, true, 1, and 1.0, and the false values are n, no, f, false, 0, and 0.0. These values are case-insensitive. `<`falseaction> is also optional.
## ife ##
> Syntax: {ife`|``<`compare>`|``<`trueaction>`|``<`falseaction>} -- Evaluates to `<`trueaction> if `<`compare> is either empty or made up only of whitespace, or `<`falseaction> if `<`compare> is not empty and is not made up entirely of whitespace. `<`falseaction> is optional, and if it's not present {ife} will act as if `<`falseaction> were empty. This function is the opposite of {ifne}.
## ifeq ##
> Syntax: {ifeq`|``<`compare1>`|``<`compare2>`|``<`trueaction>`|``<`falseaction>} -- Evaluates to `<`trueaction> if `<`compare1> is the same as `<`compare2>, ignoring case, or `<`falseaction> if they are not equal. `<`falseaction> is optional, and if not present {ifeq} will act as if `<`falseaction> were empty. This function is essentially the opposite of {ifneq}.
## ifjoined ##
> Syntax: {ifjoined`|``<`nick>`|``<`trueaction>`|``<`falseaction>} -- Evaluates to `<`trueaction> if the user `<`nick> is currently a member of the channel that the factoid is being run on, and `<`falseaction> if the user is not currently a member of that channel or if the user is offline. `<`falseaction> is optional. if `<`trueaction> and `<`falseaction> are bot missing, then this
function evaluates to 1 if the user is joined to the channel and 0 if the user is not joined.
## ifne ##
> Syntax: {ifne`|``<`compare>`|``<`trueaction>`|``<`falseaction>} -- Evaluates to `<`trueaction> if `<`compare> is not empty and is not made up only of whitespace, or `<`falseaction> if `<`compare> is empty or made up entirely of whitespace. `<`falseaction> is optional, and if it's not present {ifne} will act as if `<`falseaction> were empty. This function is the opposite of {ife}.
## ifneq ##
> Syntax: {ifneq`|``<`compare1>`|``<`compare2>`|``<`trueaction>`|``<`falseaction>} -- Evaluates to `<`trueaction> if `<`compare1> is not the same as `<`compare2>, ignoring case, or `<`falseaction> if they are equal. `<`falseaction> is optional, and if not present {ifneq} will act as if `<`falseaction> were empty. This function is essentially the opposite of {ifeq}.
## ignore ##
> Syntax: {ignore`|``<`value>} -- Evaluates `<`value>, but doesn't insert it into the factoid. For example, "Hello {ignore`|`World}" would produce a factoid that, when run, outputs "Hello ", not "Hello World". This is most useful for including comments in the factoid.
## import ##
> Syntax: {import`|``<`factoid>`|``<`argument1>`|`...} -- Imports the specified factoid into this one. This function evaluates to whatever the factoid indicated ends up outputting. `<`factoid> is the name of the factoid, and `<`argument1>, `<`argument2>, etc. are the arguments to be passed to the factoid.
## indexof ##
> Syntax: {indexof`|``<`substring>`|``<`string>`|``<`from>} -- Evaluates to the index within `<`string> that `<`substring> first occurs, or -1 if `<`substring> isn't present anywhere within `<`string>. `<`from> is optional, and if it's present it specifies an index that the search will begin at.
## intcompare ##
> Syntax: {intcompare`|``<`first>`|``<`second>`|``<`if>} -- Same as {compare}, but compares whole numbers for numerical ordering. For example, {intcompare`|`1`|`3} evaluates to -1, {intcompare`|`7`|`12} evaluates to -1 (whereas {compare`|`7`|`12} would evaluate to 1), and {intcompare`|`13`|`8} evaluates to 1. `<`if> is optional, and defaults to false.
## interval ##
> Syntax: {interval`|``<`seconds>} -- Formats the specified number of seconds as an interval. For example, {interval`|`137} would evaluate to "2 minutes 17 seconds". This function supports all the way up to years (meaning {interval`|`31536000} evaluates to "1 year").
## isadmin ##
> Syntax: {isadmin`|``<`channel>`|``<`nick>} -- Exactly the same as {isop}, but checks to see if the user is a channel admin. On most servers, this is mode +a.
## isat ##
> Syntax: {isat`|``<`channel>} -- Evaluates to 1 if the bot is currently at the specified channel, or 0 if the bot is not currently joined to the specified channel. This does not take into account whether or not the bot is currently on the bot's auto-join list; it simply takes into account what channels the IRC server would see the bot
as being on. To find out if a particular channel is on the bot's auto-join list, use {isautojoin} instead.
## isautojoin ##
> Syntax: {isautojoin`|``<`channel>} -- Evaluates to 1 if the bot is set to auto-join the specified channel, or 0 if the bot is not set to auto-join the specified channel. If you just want to see if the bot is currently at a channel, not whether it is set to auto-join, use {isat}. If you want to see if the bot has a factoid database
for the specified channel, use {hasfactdb}.
## isfounder ##
> Syntax: {isfounder`|``<`channel>`|``<`nick>} -- Exactly the same as {isop}, but checks to see if the user is a channel founder. On most servers, this is mode +q.
## isfuture ##
> Syntax: {isfuture`|``<`key>} -- Evaluates to 1 if there is currently a scheduled future task with the key `<`key> that has not run yet, or 0 if there is no such scheduled future task.
## ishalfop ##
> Syntax: {ishalfop`|``<`channel>`|``<`nick>} -- Exactly the same as {isop}, but checks to see if the user is a channel halfop. On most servers, this is mode +h.
## isinrange ##
> Syntax: {isinrange`|``<`number>`|``<`min>`|``<`max>} -- Checks to see if `<`number> is greater than or equal to `<`min> and less than or equal to `<`max>. If `<`number> is not within this range, or if `<`number> is not a whole integer (or if it's not a number at all), then {isinrange} evaluates to 0. Otherwise, {isinrange} evaluates to 1.
## isop ##
> Syntax: {isop`|``<`channel>`|``<`nick>} -- Evaluates to "1" if the nick specified is a channel operator at this channel or "0" if the nick specified is not a channel operator at this channel. %self% can be used to get the bot's own nick, so {isop`|`%self%} would indicate whether the bot has operator privileges at this channel.
`<`channel> means the channel to check at. If it's not present, then the channel that this factoid is being run at will be used.
## isresource ##
> Syntax: {isresource`|``<`name>} -- Returns 1 if `<`name> denotes a valid resource (IE {getresource`|``<`name>} could be called without an error occuring), or 0 if `<`name> does not denote a valid resource.
## isvoiced ##
> Syntax: {isvoiced`|``<`channel>`|``<`nick>} -- Exactly the same as {isop}, but checks to see if the user is voiced. On most servers, this is mode +v.
## javadoc ##
> Syntax: {javadoc`|``<`action>`|``<`desc>} -- Performs a javadoc-related action on a class or method descriptor `<`desc>. `<`desc> can be one of "`<`package>.`<`class>", "`<`class>" (which will only work if there is only one class named `<`class> in the javadoc tree that this command searches), "`<`package>.`<`class>.`<`method>", or "`<`class>.`<`method>". `<`method> is the name of a method, with
argument types enclosed with parentheses at the end. All subpages of this page are different actions that you can use for `<`action>, and each subpage describes what that action does.
## join ##
> Syntax: {join`|``<`channel>} -- Causes the bot to join the specified channel and add the specified channel to the bot's auto-join list. This also creates a factoid database for the channel if one does not already exist.
## kick ##
> Syntax: {kick`|``<`nick>`|``<`reason>} -- Kicks the specified nickname off of the current channel. If the bot is not an op at the channel, this function does nothing. `<`reason> is optional, and the bot's name will be used as the reason if no reason is provided.
## lastindexof ##
> Syntax: {lastindexof`|``<`substring>`|``<`string>`|``<`from>} -- Evaluates to the last index within `<`string> that `<`substring> occurs, or -1 if `<`substring> isn't present anywhere within `<`string>. `<`from> is optional, and if it's present it specifies an index that the search will begin at (the search goes backward, so `<`from> would be the maximum index that this function could evaluate to).
## lcvars ##
> Syntax: {lcvars`|``<`regex>} -- Same as {lgvars} but for chain variables instead of global variables.
## ldelete ##
> Syntax: {ldelete`|``<`varname>} -- Deletes the local variable with the specified name.
## length ##
> Syntax: {length`|``<`value>} -- Evaluates to the number of characters that are in `<`value>. For example, {length`|`hello} evaluates to "5", and {length`|`hello world} evaluates to "11".
## lengthto ##
> Syntax: {lengthto`|``<`regex>`|``<`text>`|``<`length>`|``<`delimiter>} -- Splits `<`text> around `<`regex>, then reconstrucs the resulting items into a new string, with each item being delimited by `<`delimiter>. Items will be added until the total size of the string would be more than `<`length>. In this way, the resulting text will never be longer than `<`length>,
while fitting as many items as possible into the string.
## lget ##
> Syntax: {lget`|``<`varname>} -- Evaluates to the value of the specified local variable. {lget`|`something} is equivalent to %something%. However, using percent signs doesn't allow for dynamic variable names (as an example, you couldn't do something like %param-%index%% for syntax reasons), which is where you would use {lget}.
## lgvars ##
> Syntax: {lgvars`|``<`regex>} -- Returns a pipe-delimited list of global variable names, with pipes in those names escaped (pipes in variable names are still a bad idea anyway) with backslashes. This is mostly for when you're trying to debug stuff and you want to see the list of global variables that exist.
`<`regex> is optional, but if it's present, only the names of variables that match `<`regex> will be returned.
## listhttp ##
> Syntax: {listhttp} -- Returns a pipe-separated list of server port numbers representing all currently-running HTTP servers. See {starthttp} for information on what HTTP servers are.
## listresources ##
> Syntax: {listresources} -- Returns a forward-slash-separated list of resources available to the bot. See {getresource} for information on what a resource is.
## llvars ##
> Syntax: {llvars`|``<`regex>} -- Same as {lgvars} but for local variables instead of global variables.
## logs ##
> Syntax: {logs`|``<`max>} -- Returns the last few messages that were sent at this channel. The resulting log events will be separated by a newline character. Each line is of the format `<`action> `<`time> `<`source> `<`details>. `<`action> is the action that occured, which is one of "mode", "kick",
"joined", "left", "nick", "message", or "action" right now. `<`time> is the number of milliseconds since the epoch. `<`source> is the nick that caused the action to occur. `<`details> varies depending on the action. For mode, details is the IRC-format mode string that happened, such as "+o jcp". For kick, details is the name of the person that was kicked, a space, and the reason that the person was kicked.
For joined, details is "username@host" for that user. For left, details is empty. For nick, details is the new nick of the user. For action and message, details is the action or message sent by that user. For topic, details is the new topic of the channel.
## longrandom ##
> Syntax: {longrandom} -- Generates a random string of digits. The length of this string is generally around 40 characters, and is guaranteed not to be longer than 42 characters. This is intended for instances where some sort of unique ID is needed.
## lower ##
> Syntax: {lower`|``<`value>} -- Converts the specified value to lower case.
## lpvars ##
> Syntax: {lpvars`|``<`regex>} -- Same as {lgvars}, but lists persistent variables instead of global variables. See "%HELPCMD% functions pset" for information on the difference between persistent variables and global variables.
## lset ##
> Syntax: {lset`|``<`varname>`|``<`value>} -- Sets the specified local variable to the specified value. Local variables are those that can be read by using percent signs. For example, after {lset`|`something`|`Hello world} is run in a factoid, %something% could be used and would be replaced with "Hello world".
## mapinline ##
> Syntax: {mapinline`|``<`listregex>`|``<`itemregex>`|``<`text>`|``<`prefix>} -- Converts `<`text> into an associative array by splitting it into a list of items around `<`listregex>, and then by splitting each of those items into two pieces around the first occurence of `<`itemregex>. Each item in this associative array is then stored as a local variable,
with the prefix plus the item's name being the key and the item's value being the value of the variable.
## mapread ##
> Syntax: {mapread`|``<`listregex>`|``<`itemregex>`|``<`text>`|``<`key>} -- Converts `<`text> into an associative array by splitting it into a list of items around `<`listregex>, and then by splitting each of those items into two pieces around the first occurence of `<`itemregex>. The item with the key named `<`key> is then looked up, and mapread evaluates to that item's value.
## match ##
> Syntax: {match`|``<`regex>`|``<`test>} -- Evaluates to 1 if `<`test> matches the regular expression `<`regex>, or 0 if it does not.
## mbean ##
> Syntax: {mbean`|``<`object>`|``<`attribute>} -- Gets the attribute of the specified mbean object from the platform-local MBean server. To get a list of all valid objects and attributes, start the bot up and attach to it with JConsole, then go to the MBeans tab. Each item in the tree that has children named "attributes" or "operations"
is an object that can be used, and you can hover your mouse over it to see the name that `<`object> needs to be. Each item under "attributes" is an attribute that can be used as `<`attributes>. If there is no such attribute, an exception will be thrown.
## members ##
> Syntax: {members`|``<`channel>} -- Evaluates to a space-separated list of the nicknames of the people that are currently in `<`channel>.
## mode ##
> Syntax: {mode`|``<`arguments>} -- Sets the specified mode on the channel. For example, to make the person "jcp" an op, you could use {mode`|`+o jcp}. To take away ops from jcp, you could use {mode`|`-o jcp}. To add color lock to the channel (a hyperion-specific mode), you could use {mode`|`+c}. If you wanted
to op both jcp and schrottplatz, but deop Marlen\_Jackson, voice MrDudle, add color lock, and ban**!**@1.2.3.4 all at the same time, you could do {mode`|`+oo-o+vcb jcp schrottplatz Marlen\_Jackson MrDudle**!**@1.2.3.4}.
## n ##
> Syntax: {n} -- Resets any coloring that has been applied in the factoid, so that all succeeding text has no special formatting.
This function is deprecated, and "\p" should be used instead.
## numberlist ##
> Syntax: {numberlist`|``<`start>`|``<`end>`|``<`step>} -- Evaluates to a space-separated list of the whole integers starting with `<`start> and ending with `<`end>. `<`step> is optional, and specifies if numbers should be skipped. Whether or not `<`step> is positive or negative has no effect on the ordering of numbers; which one (of start and end) is above the other is what determines ordering.
For example, {numberlist`|`1`|`5} evaluates to "1 2 3 4 5", {numberlist`|`5`|`1} evaluates to "5 4 3 2 1", {numberlist`|`3`|`3} evaluates to "3", {numberlist`|`45`|`8`|`10} evaluates to "45 35 25 15", {numberlist`|`8`|`45`|`10} evaluates to "8 18 28 38", and {numberlist`|`8`|`45`|`-10} evaluates to "8 18 28 38". This can be used with {split} to create a for loop.
## override ##
> Syntax: {override} -- Only useful in a factoid called by a regex. Indicates that no other factoids should be run, including other regexes and factoids matching the channel's trigger. This does not block commands from running.
## pad ##
> Syntax: {pad`|``<`number>`|``<`char>`|``<`value>} -- Evaluates to `<`value>, but with `<`char> (which must be a single character) prepended until the resulting length is at least equal to `<`number>. For example, {pad`|`7`|`0`|`1234} would evaluate to "0001234".
## part ##
> Syntax: {part`|``<`channel>} -- Causes the bot to leave the specified channel, and remove the channel from the bot's auto-join list. Channel-specific factoids will still be remembered for the next time that the bot is asked to join the channel. If you want the bot to leave the channel without removing the channel from the
bot's auto-join list, use {temppart}.
## pastebin ##
> Syntax: {pastebin`|``<`text>`|``<`duration>} -- Creates a post at http://pastebin.com with the specified text and the specified duration (which should be either "day" or "month"). `<`duration> is optional, and will default to "day" if not present.
## pdelete ##
> Syntax: {pdelete`|``<`varname>} -- Same as {delete`|``<`varname>}, but deletes the specified persistent variable instead of the specified global variable. See "%HELPCMD% functions pset" for information on the difference between persistent variables and global variables.
## pget ##
> Syntax: {pget`|``<`varname>} -- Same as {get`|``<`varname>}, but gets the specified persistent variable instead of the specified global variable. See "%HELPCMD% functions pset" for information on the difference between persistent variables and global variables.
## pset ##
> Syntax: {pset`|``<`varname>`|``<`value>} -- Sets the specified persistent variable to the specified value. Persistent variables are different from global variables in that global variables are lost whenever the bot is restarted, whereas persistent variables are stored in the database and so are not lost when the bot restarts.
## radix ##
> Syntax: {radix`|``<`from>`|``<`to>`|``<`value>} -- Converts `<`value>, which is a number in base-`<`from>, to be a value in base-`<`to>. For example, {radix`|`10`|`16`|`12} evaluates to "c", and {radix`|`10`|`16`|`35} evaluates to "23". Fractional numbers are not currently allowed.
## random ##
> Syntax: {random`|``<`choice1>`|``<`choice2>`|`...} -- Evaluates to one of the choices at random. For example, {random`|`bye`|`see ya`|`laters`|`so long} would evaluate to one of "bye", "see ya", "laters", or "so long", chosen at random.Only the choice that is chosen is evaluated.
## randomint ##
> Syntax: {randomint`|``<`number>} -- Returns a number between 0, inclusive, and `<`number>, exclusive, chosen at random. The number will always be a whole integer. If you want a number between 1 and `<`number>, inclusive, you could use {eval`|`{random`|``<`number>}+1} to do that.
## randomize ##
> Syntax: {randomize`|``<`regex>`|``<`string>`|``<`delimiter>} -- Splits `<`string> around the regular expression `<`regex>, shuffles the resulting list of strings, and then evaluates to a `<`delimiter>-separated list of those strings. For example, {randomize`|`\\\.`|`first.second.third.fourth`|`-} could evaluate to "third-second-first-fourth" or maybe "second-first-fourth-third".
## randomsplit ##
> Syntax: {randomsplit`|``<`text>`|``<`delimiter>`|``<`regex>} -- Splits `<`text> around the delimiter `<`delimiter> (which is a regular expression), and then chooses one of the resulting strings at random and evaluates to that string. If `<`regex> is present (`<`regex> is entirely optional), then only strings that exactly match `<`regex> will be considered for random choosing.
## readpaste ##
> Syntax: {readpaste`|``<`pasteurl>} -- Reads a pastebin post made at any of the enabled pastebin providers.
## remaining ##
> Syntax: {remaining`|``<`key>} -- Evaluates to the number of milliseconds left before the future whose key is `<`key> will run, or the empty string if there is no future with the specified key.
## replace ##
> Syntax: {replace`|``<`mode>`|``<`text>`|``<`search>`|``<`replacement>} -- Replaces `<`search> in the text `<`text> with `<`replacement> if `<`mode> is "text", or replaces any string that matches the regular expression `<`search> in the text `<`text> with `<`replacement> (which can contain back references) if `<`mode> is "regex". `<`mode> can be omitted, and will default to regex.
## restrict ##
> Syntax: {restrict`|``<`text>`|``<`length>} -- Evaluates to `<`text> if its length is shorter than `<`length>. Otherwise, evaluates to the first `<`length>-3 characters of `<`text>, with three dot characters on the end to form an ellipsis. For example, {restrict`|`Hello everyone`|`15} would be
"Hello everyone", but {restrict`|`Hello everyone`|`11} would be "Hello ev...".
## rmself ##
> Syntax: {rmself} -- Deletes this factoid. This can be used for one-time factoids, such as post-install configuration factoids for factpacks.
## round ##
> Syntax: {round`|``<`number>`|``<`precision>} -- Rounds the specified number to have the specified precision. For example, {round`|`12345`|`2} is "12000", and {round`|`1.2345`|`2} is "1.2".
## safeimport ##
> Syntax: {safeimport`|``<`factoid>`|``<`arg1>`|``<`arg2>`|`...} -- Exactly the same as {import`|``<`factoid>`|``<`arg1>`|``<`arg2>`|`...}, except that this function won't run restricted or library factoids. If a restricted or library factoid is passed as `<`factoid>, {safeimport} will throw an exception.
## sdateformat ##
> Syntax: {sdateformat`|``<`format>`|``<`date>} -- Formats the date `<`date>, which is a number of milliseconds since January 1, 1970, using the Java SimpleDateFormat string `<`format>. See http://java.sun.com/javase/6/docs/api/ for information on the syntax of `<`format>.
## sdateparse ##
> Syntax: {sdateparse`|``<`format>`|``<`text>} -- Parses `<`text>, which is a date in the format specified by `<`format> (which should be a Java SimpleDateFormat string), into a number representing the parsed date.See http://java.sun.com/javase/6/docs/api/ for information on the syntax of `<`format>.
## sendaction ##
> Syntax: {sendaction`|``<`to>`|``<`message>} -- Sends the specified message to the specified recipient as if it were typed at an IRC client with "/me" at the beginning.
## sendmessage ##
> Syntax: {sendmessage`|``<`to>`|``<`message>} -- Sends the specified message to the specified recipient, which can be a channel or a nickname.
## sendsplit ##
> Syntax: {sendsplit`|``<`to>`|``<`regex>`|``<`delimiter>`|``<`message>} -- Divides `<`message> into a list of strings split around the regular expression `<`regex>, then attempts to reconstruct the string, delimiting each string in the list with `<`delimiter>, and send the resulting string to `<`to>. If the resulting string would be longer than approximately 450 characters (IRC limits maximum line
length to 512 characters), then the message is split exactly where a delimiter would occur so that the first message is as long as possible while falling within the limit. The delimiter will be omitted at such boundaries. If you're still confused about how this works, probably the best way to find out would be to use numberlist to create a long string and then experiment with using this function on that string.
## set ##
> Syntax: {set`|``<`varname>`|``<`value>} -- Sets the named global variable to the specified value.
## sort ##
> Syntax: {sort`|``<`regex>`|``<`string>`|``<`delimiter>`|``<`case>} --  Splits `<`string> around the regular expression `<`regex>, sorts this resulting list of substrings (case-sensitively if `<`case> is 1, otherwise case-insensitively), then reconstructs a new string by delimiting the substrings with `<`delimiter>. `<`case> is optional, and defaults to 1 if not present.
## split ##
> Syntax: {split`|``<`regex>`|``<`string>`|``<`varname>`|``<`action>`|``<`delimiter>} -- Splits `<`string> into a list of strings around the regular expression `<`regex>, then evaluates `<`action> once for each item in the list of strings, with the local variable `<`varname> set to the current item in the list. {split} then evaluates to what each of the evaluations of `<`action> evaluated to, separated by `<`delimiter>.
As an example, {split`|`\\.`|`first.second.third`|`thevalue`|`This is the %thevalue%`|` -- } would result in "This is the first -- This is the second -- This is the third". `<`delimiter> is optional.
Currently, empty values at the end of the list are ignored. This means that in the above example, if "first.second.third" were replaced with "first.second.third...", the output would still be the same. {split} can be used with `<`string> being the {numberlist} function to effectively create a for loop. Also, if `<`string> is empty, `<`action> is not evaluated.
## splitchars ##
> Syntax: {splitchars`|``<`text>`|``<`delimiter>} -- Evaluates to `<`text>, but with `<`delimiter> inbetween each character in `<`text>. For example, "{splitchars`|`hello`|`-}" results in "h-e-l-l-o".
## splitindex ##
> Syntax: {splitindex`|``<`regex>`|``<`text>`|``<`max>`|``<`index>} -- Splits `<`text> around the regular expression `<`regex> to a maximum length of `<`max>, and then returns the `<`index>th element in that new list. For example, {splitindex`|`_`|`first\_second\_third\_fourth`|`10`|`3} evaluates to "third", and {splitindex`|`_`|`first\_second\_third\_fourth`|`2`|`2} evaluates to "second\_third\_fourth".
In other words, all tokens after (and including) the `<`max>th token are concatenated (split by the delimiter that `<`regex> matched) and used as the last token. If `<`index> is greater than the number of items that there are in the list, splitindex evaluates to the empty string.
## starthttp ##
> Syntax: {starthttp`|``<`port>`|``<`factoid>} -- Starts an HTTP server on the specified port. Use "%HELPCMD% functions starthttp details" for more info.
## stophttp ##
> Syntax: {stophttp`|``<`port>} -- Stops an HTTP server running on the specified port. See {starthttp} for more information on what HTTP servers are.
## substring ##
> Syntax: {substring`|``<`start>`|``<`end>`|``<`text>} -- Evaluates to a substring of `<`text>, which starts at the index specified by `<`start> and ends at `<`end>. If the specified indexes are out of bounds, they will be changed to be within bounds. Indexes are 0-based, with start being inclusive and end being exclusive. For example, {substring`|`3`|`6`|`0123456789} evaluates to "345".
## switch ##
> Syntax: {switch`|``<`value>`|``<`test1>`|``<`case1>`|``<`test2>`|``<`case2>`|`...`|``<`default>} -- If `<`value> is equal (this is case-sensitive) to `<`test1>, then this evaluates to `<`case1>. If not, then if `<`value> is equal to `<`test2>, then this evaluates to `<`case2>, and so on. If `<`value> isn't equal to any of the `<`test> arguments, then the switch function evaluates to `<`default>.
`<`default> is entirely optional. If it's not present, and none of the `<`test> arguments match `<`value>, then the switch function will evaluate to nothing. For example, {switch`|`2`|`1`|`first`|`2`|`second`|`3`|`third`|`missing} would evaluate to "second", and {switch`|`5`|`1`|`first`|`2`|`second`|`3`|`third`|`missing} would evaluate to "missing".
## tempjoin ##
> Syntax: {tempjoin`|``<`channel>} -- Causes the bot to join the specified channel, but without setting this channel to auto-join or creating a factoid database for the channel.
## temppart ##
> Syntax: {temppart`|``<`channel>`|``<`reason>} -- Causes the bot to leave the specified channel, but without removing the channel from the bot's auto-join list. If `<`reason>, which is optional, is specified, then that reason is used to leave the channel.
## timems ##
> Syntax: {timems} -- Returns the server's current time in milliseconds since January 1, 1970 Midnight UTC.
## topic ##
> Syntax: {topic} or {topic`|``<`newtopic>} -- If used without any arguments, evaluates to the current channel's topic. If used with one argument, sets the current channel's topic to be `<`newtopic>. The bot must be a channel operator on most channels before this can be run.
## transfer ##
> Syntax: {transfer`|``<`from>`|``<`to>`|``<`regex>`|``<`varname>`|``<`namegen>} -- Transfers a set of variables from one variable type to another variable type, or bulk-renames a set of variables. `<`from> and `<`to> are one of "global", "local", "persistent", or "chain", or the first letter of one of those. They specify the type of variable to copy
from and the type of variable to copy to. All variables whose names match `<`regex> will be copied. `<`varname> and `<`namegen> are optional, and if present, for each variable copied, a local variable named `<`varname> will be set to the name of the variable to copy, and `<`namegen> will be run. `<`namegen> should then evaluate to the new
name for the variable. If `<`varname> and `<`namegen> are absent, the variable's original name is kept. If `<`namegen> evaluates to the empty string, the variable is not copied.
## trigger ##
> Syntax: {trigger} or {trigger`|``<`new>} -- When invoked as {trigger}, evaluates to the current channel's trigger. When invoked as {trigger`|``<`new>}, sets the current channel's trigger to `<`new>. If there isn't a current channel (IE this is a global factoid and the user pm'ed us), then this does nothing and evaluates to nothing.
## trim ##
> Syntax: {trim`|``<`text>} -- Removes all leading and trailing whitespace from `<`text>.
## twiliocall ##
> Syntax: {twiliocall`|``<`target>`|``<`callback>} -- Uses the Twilio service to place a call to the phone number `<`target>, calling back to `<`callback> when the call has been put through. This function then evaluates to an XML document describing the result. Note that the file storage/twilio-account must exist, as well as the file**

storage/twilio-secret. The file storage/twilio-from must also exist.
## type ##
> Syntax: {type`|``<`factoidname>} -- Evaluates to the type of factoid that `<`factoidname> is. This is either "global", "channel", or "none". Global means that the factoid is a global factoid, channel means that the factoid is a channel-specific factoid, and nonexistent means that the factoid in question does not exist. This checks for channel-specific factoids only on the current channel.
If there is both a channel-specific factoid and a global factoid with the name `<`factname>, "both" will be returned.
## u ##
> Syntax: {u} -- Inserts the IRC underline character, which causes all succeeding text to be underlined.
This function is deprecated, and "\u" should be used instead.
## upper ##
> Syntax: {upper`|``<`value>} -- Converts the specified value to upper case.
## uptime ##
> Syntax: {uptime} -- Returns the time, in milliseconds since Midnight January 1, 1970, at which the bot started up.
## urldecode ##
> Syntax: {urldecode`|``<`text>} -- Decodes the url-encoded text specified.
## urlencode ##
> Syntax: {urlencode`|``<`text>} -- Encodes the text specified so that it is suitable for including in a URL.
## urlget ##
> Syntax: {urlget`|``<`url>`|``<`method>`|``<`data>} -- Gets the page at the specified url. `<`url> is the url to get. This currently must only be an http or https url. `<`method> and `<`data> are both optional, but `<`method> is required if `<`data> is to be used. `<`method> is the HTTP method to use, which defaults to GET. `<`data> is the request data to send to the server.
Currently, if `<`method> is POST and `<`data> is not empty, an additional header, "Content-Type", will be sent along with the request with a value of "application/x-www-form-urlencoded". This will most likely changed in the future.
## wait ##
> Syntax: {wait`|``<`duration>} -- Waits `<`duration> milliseconds before continuing. The bot has a built-in timer that won't let a factoid run longer than 60 seconds, so don't make `<`duration> longer than that.
## weather ##
> Syntax: {weather`|``<`zipcode>`|``<`prefix>} -- Gets information on the current weather conditions for `<`zipcode> by contacting the WeatherBug and Yahoo servers. Weather information is then placed in a number of different local variables, each prefixed with `<`prefix> to avoid conflicting variable names. `<`prefix> is optional, and will default to nothing (IE no prefix) if not present.
## while ##
> Syntax: {while`|``<`condition>`|``<`action>} -- Evaluates `<`condition>, and if it's 1, evaluates `<`action> and then evaluates `<`condition> again. This keeps going on and on until `<`condition> evaluates to 0. {while} doesn't evaluate to anything, even if its action did, so if you want any output you'll need to use a variable to store it.
## xmladd ##
> Syntax: {xmladd`|``<`target>`|``<`index>`|``<`tagname>} -- Adds an XML tag, with the tag name `<`tagname>, to the target element `<`target> at the position `<`index>. 0 is the first element. This then evaluates to
## xmlparse ##
> Syntax: {xmlparse`|``<`name>`|``<`text>} -- Parses `<`text>, which should be a valid XML document, and stores it as a document called `<`name>. Within the local scope of this factoid, various {xml`<`something>} functions can be called to get access to stuff within this XML document.
## xmlsearch ##
> Syntax: {xmlsearch`|``<`name>`|``<`path>} -- Searches the XML document named `<`name> for any elements or attributes that match the XPath `<`path>, and evaluates to a newline-separated list of unambiguous XPaths that represent each matching item. The search is performed with the root element of the doucument as the context.
## xmltext ##
> Syntax: {xmltext`|``<`name>`|``<`path>} -- Finds the element or attribute within the document named by `<`name> that matches `<`path>, and evaluates to its text contents if it's an element or its attribute value if it's an attribute.
[Back to top](FactoidFunctions.md)