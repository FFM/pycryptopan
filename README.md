PyCrypto-PAn
============

A IP address anonymizer in Python using the Crypot-PAn algorithm.

* Crypto-PAn: http://www.cc.gatech.edu/computing/Telecomm/projects/cryptopan/

Based on IP::Anonymous by John Kristoff 

* http://search.cpan.org/dist/IP-Anonymous/lib/IP/Anonymous.pm


usage:
```python

from cryptopan import CryptoPan
c=CryptoPan("".join([chr(x) for x in range(0,32)]))
c.anonymize("192.0.2.0")
```

Acknowledgements
----------------

This work was funded by the EU FP7 Project "CONFINE"
http://www.confine-project.eu
