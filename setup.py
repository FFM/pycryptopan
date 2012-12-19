from distutils.core import setup
f=open("README")
setup(name='pycryptopan', version='0.01a',
            py_modules=['cryptopan'],
            url="https://github.com/FFM/pycryptopan",
            author="Michael Bauer",
            author_email="mihi@lo-res.org",
            description="""A python implementation of Crypto-PAn 
              a ip anonymization algorithm""",
            long_description="\n".join(f)
                  )
install_requires=['pycrypto']                  
