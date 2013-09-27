"""

    Utils for extracting information about bitcoin transactions.


"""
import json

from .utils import bitcoind


def get_transaction_first_sending_address(txid):
    """ Get bitcoin transaction info.

    Use transaction id to extract data directly from bitcoind.
    Mostly useful for getting "from" addresses from the transaction.

    Based on:

    http://bitcoin.stackexchange.com/a/5982/5464

    https://bitcointalk.org/index.php?topic=138752.msg1481892#msg1481892

    Example:

        echo "import django_bitcoin.txutils ; print django_bitcoin.txutils.get_transaction_first_sending_address('b3a4f855c4b20f8256861af6d65888eea9c35a5ac7c81651d57a28c9e5a15c3b')" | python manage.py shell

    """
    raw = bitcoind.bitcoind_api.getrawtransaction(txid)
    #print raw
    txdata_raw = bitcoind.bitcoind_api.decoderawtransaction(raw)

    print txdata_raw
    for itx in txdata_raw["vin"]:
        print itx

    return
    first_input = txdata_raw["vin"][0]


    print first_input["txid"]
    try:
        first_raw = bitcoind.bitcoind_api.getrawtransaction(first_input["txid"])
    except Exception as e:
        print e.error, e.message
    print first_raw
    first_txdata_raw = bitcoind.bitcoind_api.decoderawtransaction(first_raw)

    print first_txdata_raw['vout'][first_input['vout']]['scriptPubKey']['addresses'][0]

