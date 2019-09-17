from distutils.core import setup
f=open("README")
setup(name='pycryptopan', version='0.01f',
            py_modules=['cryptopan'],
            install_requires=['pycrypto'],                  
            requires=['pycrypto'],                  
            url="https://github.com/aaronkaplan/pycryptopan",
            author="Aaron Kaplan",
            author_email="aaron@lo-res.org",
            description="""A python implementation of Crypto-PAn 
              a ip anonymization algorithm. Original first author: Michael Bauer (mihi@lo-res.org). 
              Aaron Kaplan (second author, aaron@lo-res.org) is continuing the work when needed. 
              Mihi R.I.P. Your code remembers you on the Internet.""",
            long_description="\n".join(f)
                  )
