import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex_futures import BitmexClient
from interface.root_component import Root

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient("5680cfa75f5bb50033912afa39fae9bb752d6aabec1789c13ac183748a621522",
                                   "5d04972eabef4bb2fb632a65a6ae46b4f9c0b8a2075517ab6a04fd202ff3fa21",
                                   testnet=True, futures=True)
    bitmex = BitmexClient("FLtRBQiE4LOTxgQ8HIadPszE", "GDhltmEL10PDHnCdC8rRc7phw9hW5cMCMV87vGInFLUV_BW8", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
