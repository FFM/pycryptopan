from distutils.core import setup
f=open("README")
setup(name='pycryptopan', version='0.01d',
            py_modules=['cryptopan'],
            install_requires=['pycrypto'],                  
            requires=['pycrypto'],                  
            url="https://github.com/FFM/pycryptopan",
            author="Michael Bauer",
            author_email="mihi@lo-res.org",
            description="""A python implementation of Crypto-PAn 
              a ip anonymization algorithm""",
            long_description="\n".join(f)
                  )
