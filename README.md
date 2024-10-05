# PyFemap
Python tools to interact with Femap

## Instalation

To use the Femap interface you must `pip install pywin32` and run the script
```python3
import sys
from win32com.client import makepy
sys.argv = ["makepy", "-o PyFemap.py", r"{YOUR FEMAP INSTALATION DIRECTORY}\femap.tlb"]
makepy.main()
```
source: https://community.sw.siemens.com/s/article/writing-the-femap-api-in-python

after that, you must move the PyFemap.py file to your python Lib folder.

to test if everything is working right, open your femap and run the following code:

```python3
import pythoncom
import Pyfemap
from Pyfemap import constants as cs
import sys

try:
    existObj = pythoncom.connect(Pyfemap.model.CLSID) #Grabs active model
    app = Pyfemap.model(existObj)#Initializes object to active mode
    app.feAppMessage(0,"Hello word, congrats everything is working right")

except:
    sys.exit("femap not open") #Exits program if there is no active femap model
```
