todo
====

**Twitter as a Push Notification Service**

```
pip install push
```


Usage
-----

```
$ push Hey, don't forget that one thing. -- (sent from the command line)
```


What is this?
-------------

Basically, this is a simple script that combines the powers of [`foauth`][foauth],
[`requests`][req], and a private Twitter account into push notifications from the
command line. Before using, there are three important environment variables
you'll need to set.

```bash
export FOAUTH_USER="myfoauthemail@me.com"
export FOAUTH_PASS="foauth_password"
export FOAUTH_TWITTER="@zachwill"
```

You'll also need to sign up for a new (and most likely private) Twitter account,
and connect that with your [`foauth` account][foauth].


[foauth]: https://foauth.org/
[req]: http://docs.python-requests.org/en/latest/
