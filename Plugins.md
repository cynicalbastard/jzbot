> _This page contains information on how plugins work and how to write them. For information on popular plugins, see PluginList._

## Plugins ##
JZBot supports a notion of plugins. Plugins are pieces of code that can provide advanced functionality beyond what factoids can provide.

Plugins in JZBot are somewhat different from plugins for other applications (such as Eclipse or Firefox) in that they can be written in **any** programming language, as long as it supports TCP sockets. Plugins themselves don't interact with JZBot code; all communication between JZBot and a particular plugin is done over a TCP socket.

Furthermore, external applications can, with suitable authorization (I'll get to what "suitable authorization" means a bit further on), act as plugins themselves. This allows external applications to interface with the bot and provide additional services. For example, [BZNetwork](http://bznetwork.googlecode.com) will soon be able to interface with JZBot to send notifications to channels when a particular event happens on a BZFlag server.

## Writing a Plugin ##
Plugins are executable scripts or programs placed in JZBot's `storage/plugins` folder. Each file within this folder is a plugin.

When JZBot is going to load a plugin, it simply executes the plugin's script, with some command line parameters in this order:
  * The text `run`. This indicates run mode. The other mode (information mode) will be discussed shortly.
  * The hostname or IP address that the plugin should connect to
  * The port that the plugin should connect over
  * A unique key for the plugin to authenticate with. I'll discuss more on this later.

When a user requests information on currently-installed plugins, or information on a particular installed plugin, JZBot runs the plugin script with these command line parameters in this order:
  * The text `info`. This indicate information mode.

### Information Mode ###
When a plugin is run in information mode, it should print to stdout some general information about itself. There isn't a well-defined format for this output yet, other than that this output will be sent to the user that requested the information and that it will be truncated at 32KB in length. If anyone has a plugin that legitimately needs to send more information than this, get in touch with [javawizard](People#Alex.md) and he can raise this.

If the plugin process takes longer than 10 seconds to run in information mode, it will be killed and an error message reported to the user requesting the information.

Output sent by the plugin to stderr will be ignored.

### Run Mode ###
When a plugin is run in run mode, it should connect to the host and port specified as command-line arguments and authenticate with the server using the protocol described below. If it does not do so within 20 seconds, the plugin process will be killed and an error message reported to the user.

If the plugin process dies while the plugin is still supposed to be loaded, JZBot unloads the plugin and logs an error message.

If JZBot requests that the plugin unload (how, exactly, it does this will be covered later in the Protocol section) and it fails to do so after 20 seconds, the plugin process will be killed, the plugin forcibly unloaded, and an error message reported to the user that requested the plugin be unloaded.

## Protocol ##
The protocol for communication has been documented in docs/technotes/plugin-rpc-protocol.txt in the JZBot source tree. I'll get around to writing more documentation here on it sometime soon.

## External Plugins ##
External plugins are programs that load themselves as plugins without actually being scripts in the plugins folder. This provides an API that external applications can use to communicate with JZBot.

Since external plugins need to know a port to connect to, JZBot writes the port it listens for plugins on to storage/plugin-port. To allow for plugins running on other hostnames to be able to connect without being able to read files on the file system, a file called storage/requested-plugin-port can be present, and JZBot will read this file on startup. This file, if present, must only contain one line with a valid port number on it, and JZBot will listen on this port for plugins. When this file is present, JZBot will still write storage/plugin-port; it will contain exactly the same number as storage/requested-plugin-port.

Plugin scripts are passed a unique plugin key to authenticate with via command-line parameters as discussed above. Since external plugins aren't invoked like plugins are, they need to have a key ahead of time. The JZBot command `~plugin newkey <name>` can be used to generate a plugin key that persists until `~plugin deletekey <name>` is used. `<name>` is the "plugin name" that will be used in lieu of a plugin script name for the plugin when the plugin loads itself.

External plugins are loaded and unloaded somewhat differently from standard plugins. An external plugin can't be loaded by running any command; instead, it loads itself simply by connecting and authenticating with a particular key. If a plugin with that name is already loaded, the plugin trying to load itself will be disconnected.

An external plugin can be unloaded in the same manner that a normal plugin can be unloaded. However, JZBot doesn't actually terminate the plugin process; it simply requests that the plugin unload itself. If the plugin fails to do so after 20 seconds, JZBot forcibly unloads the plugin and closes the TCP connection to it, and reports an error message to the JZBot user that requested the plugin unload.