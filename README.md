# PyFemap
Python scrips to work with Femap

Instalation
To use the Femap interface you must pip install pywin32 and run the script

import sys
from win32com.client import makepy
sys.argv = ["makepy", "-o PyFemap.py", r"{YOUR FEMAP INSTALATION DIRECTORY}\femap.tlb"]
makepy.main()
source: https://community.sw.siemens.com/s/article/writing-the-femap-api-in-python
