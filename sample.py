#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample use cases for running DNSBL checks.
"""

import asyncio

from icecream import ic
import pydnsbl


######################################################################
## check IP address

ip_checker = pydnsbl.DNSBLIpChecker()
result = ip_checker.check("8.8.8.8")
# <DNSBLResult: 8.8.8.8  (0/52)>
ic(result)

result = ip_checker.check("68.128.212.240")
# <DNSBLResult: 68.128.212.240 [BLACKLISTED] (6/52)>
ic(result)

ASYNC_LOOP: asyncio.SelectorEventLoop = asyncio.get_event_loop()  # type: ignore

result = ASYNC_LOOP.run_until_complete(
    ip_checker.check_async("68.128.212.240")
)
ic(result)


######################################################################
## check domain

domain_checker = pydnsbl.DNSBLDomainChecker()
result = domain_checker.check("google.com")
# <DNSBLResult: google.com  (0/4)>
ic(result)

result = domain_checker.check("belonging708-info.xyz")
# <DNSBLResult: belonging708-info.xyz [BLACKLISTED] (2/4)>
ic(result)
