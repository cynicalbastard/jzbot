Ritual is the factoid language used by JZBot. When you create a factoid, you're actually writing a miniature Ritual program.

The name is a cross between "Rich", because Ritual allows for rich text and factoids to be created, and "Factual", derived from "factoid".

Ritual has two essential symbolic constructs: functions and local variable references. Function calls start with `{` and end with `}`. Function arugments are separated by `|`. The first argument is the name of the function to call. Local variable references are specified by %_something_% where _something_ is the name of a local variable. This actually gets translated to {lget|_something_} by the interpreter.

A local variable is a variable local to that factoid. I'll get to what "local to that factoid" means in a bit, but it has to do with importing and persistence. Suffice it to say that a global variable (as contrasted with local variable) persists across multiple invocations of the factoid; you can use global variables to store persistent data.

When a factoid is run, the local variable _1_ is the first argument given to it, _2_ is the second arugments, and so on. _1-_ is the first argument and everything after it, _2-_ is the second argument and everything after it, and so on. _0_ is the sender, _channel_ is the channel, and _source_ is the sender if the message was sent in a pm or the channel if the message was sent directly to a channel.