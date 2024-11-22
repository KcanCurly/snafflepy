from setuptools import setup, find_packages

setup(
    name="snafflepy",
    version="1.0.0",
    author="KcanCurly",
    description="Snaffler reimplementation in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/snafflepy",
    packages=find_packages(),
    install_requires=[
        "argcomplete==3.1.1",
        "blinker==1.6.2",
        "cffi==1.15.1",
        "chardet==5.1.0",
        "click==8.1.3",
        "cryptography==41.0.3",
        "dnspython==2.3.0",
        "Flask==2.3.2",
        "future==0.18.3",
        "impacket==0.10.0",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "ldap3==2.9.1",
        "ldapdomaindump==0.9.4",
        "MarkupSafe==2.1.3",
        "packaging==23.1",
        "pipx==1.2.0",
        "pyasn1==0.5.0",
        "pycparser==2.21",
        "pycryptodomex==3.18.0",
        "pyOpenSSL==23.2.0",
        "six==1.16.0",
        "termcolor==2.3.0",
        "toml==0.10.2",
        "userpath==1.8.0",
        "Werkzeug==2.3.6"

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ldap2json=src.ldap2json:main",
            "ldap2json-analysis=analysis.analysis:main"
        ],
    },
)