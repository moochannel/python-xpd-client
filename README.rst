*****************
python-xpd-client
*****************

XPd(Experience Points daemon program) JSON-RPC Binding for Python

Description
===========

This package is an Experience Points (XP) client for Python, and communicates
with XP daemon (XPd) via JSON-RPC.

Requirement
===========

You'll need a running instance of `XP daemon program (XPd)
<https://github.com/eXperiencePoints/XPCoin>` to connect with.

XPd doesn't allow connect via JSON-RPC port by default. So you'll need change
some settings below, then reboot XPd.

XP.conf::

  server=0 → 1
  rpcallowip=127.0.0.1 → <your ip address>

Usage
=====

Some code examples below::

  from xpd_client import XPdClient

  connection = XPdClient('http://localhost:28191', 'rpc-user', 'rpc-password')
  print(conn.getinfo())

While you connect to XPd, you can call `XPd's commands
<https://github.com/soeLexicon/node-ExperiencePoints/#commands>`.

License
=======

`MIT <https://github.com/moochannel/python-xpd-client/blob/master/LICENSE>`

Author
======

`moochannel (Katsuhisa Ueda) <https://github.com/moochannel/>`
