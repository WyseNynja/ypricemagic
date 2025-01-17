
import logging
from typing import Any, Optional

from brownie import chain
from multicall.utils import await_awaitable
from y import convert
from y.datatypes import AnyAddressType, Block, UsdPrice
from y.networks import Network
from y.utils.logging import yLazyLogger
from y.utils.raw_calls import raw_call_async

logger = logging.getLogger(__name__)

#yLazyLogger(logger)
def is_froyo(token: AnyAddressType) -> bool:
    address = convert.to_address(token)
    return chain.id == Network.Fantom and address == '0x4f85Bbf3B0265DCEd4Ec72ebD0358ccCf190F1B3'

#yLazyLogger(logger)
def get_price(token: Any, block: Optional[Block] = None) -> UsdPrice:
    return await_awaitable(get_price_async(token, block))
    

async def get_price_async(token: AnyAddressType, block: Optional[Block] = None) -> UsdPrice:
    pool = '0x83E5f18Da720119fF363cF63417628eB0e9fd523'
    virtual_price = await raw_call_async(pool, "get_virtual_price()", block=block, output='int')
    return UsdPrice(virtual_price / 1e18)
