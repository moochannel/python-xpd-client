allowed_commands = [
    'addmultisigaddress', 'addnode', 'addredeemscript', 'backupwallet', 'checkwallet',
    'createmultisig', 'createrawtransaction', 'decoderawtransaction', 'decodescript', 'dumpblock',
    'dumpblockbynumber', 'dumpprivkey', 'dumpwallet', 'encryptwallet', 'getaccount',
    'getaccountaddress', 'getaddednodeinfo', 'getaddressesbyaccount', 'getaddrmaninfo ',
    'getbalance', 'getbestblockhash', 'getblock', 'getblockbynumber', 'getblockcount',
    'getblockhash', 'getblocktemplate', 'getcheckpoint', 'getconnectioncount', 'getdifficulty',
    'getinfo', 'getmininginfo', 'getnettotals', 'getnewaddress', 'getpeerinfo', 'getrawmempool',
    'getrawtransaction', 'getreceivedbyaccount', 'getreceivedbyaddress', 'getsubsidy',
    'gettransaction', 'getwork', 'getworkex', 'help', 'importprivkey', 'importaddress',
    'importwallet', 'keypoolrefill', 'keypoolreset', 'listaccounts', 'listaddressgroupings',
    'listmintings', 'listreceivedbyaccount', 'listreceivedbyaddress', 'listsinceblock',
    'listtransactions', 'listunspent', 'makekeypair', 'mergecoins', 'move', 'ntptime',
    'removeaddress', 'repairwallet', 'resendtx', 'reservebalance', 'scaninput', 'sendalert',
    'sendfrom', 'sendmany', 'sendrawtransaction', 'sendtoaddress', 'setaccount', 'settxfee',
    'signmessage', 'signrawtransaction', 'stop', 'validateaddress', 'verifymessage', 'walletlock',
    'walletpassphrase', 'walletpassphrasechange'
]


def is_xpd_command(command):
    return command in allowed_commands
