So you want to get your JZBot to connect as a Facebook user? Cool! This wiki page should help you out with that.

First off, I should mention that to connect to a single Facebook account, you typically have to add <i>two</i> servers, not just one. The reason for this is that Facebook chat is available via XMPP, so you connect to chat with an XMPP server. The rest of the functions (such as wall posts, "What's on your mind?" posts, comments, photos, etc.) are done using a Facebook server. You can choose to use only one of these if you want, but you'll be missing half of the functionality.

You'll need to create a Facebook account for your bot. [FrequentlyAskedQuestions#I've\_heard\_the\_terms_"JZBot",_"Marlen", Marlen] uses http://facebook.com/marlenjackson as his account. You'll also need to make sure that the account has a [username](http://www.facebook.com/help/?page=896) associated with it. Once you've got the account set up, continue on to find out how to set up an XMPP server and a Facebook server to connect your bot to its Facebook profile.

## XMPP ##
First, I'll discuss how to get chat up and working. This is actually fairly simple: A message to your bot consisting of "addserver server add &lt;servername> xmpp chat.facebook.com 0 &lt;username> &lt;password>" should do the trick. &lt;servername> is the name to use for the server, which can really be anything. &lt;username> is the username you created for your Facebook profile (IE going to http://www.facebook.com/&lt;username> shows the facebook profile you created for your bot). &lt;password> is the password used on your Facebook account.

That's really about it. In a browser, sign into your own Facebook profile (not your bot's), and send "ping" to your bot. The nickname it sees you as is somewhat long and ugly; that's something that the JZBot developers need to work on. But hey, at least it works.

## Facebook ##
More to come on this soon