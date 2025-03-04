#  "virtualenv env1" i used to create virtual enviroment from this very eaisly
'''
PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> .\env1\scripts\activate.ps1
(env1) PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> pip install pandas
Collecting pandas
  Using cached pandas-2.2.3-cp313-cp313-win_amd64.whl.metadata (19 kB)
Collecting numpy>=1.26.0 (from pandas)
  Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl.metadata (60 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Using cached pytz-2025.1-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Using cached tzdata-2025.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Using cached pandas-2.2.3-cp313-cp313-win_amd64.whl (11.5 MB)
Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl (12.6 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.1-py2.py3-none-any.whl (507 kB)
Using cached tzdata-2025.1-py2.py3-none-any.whl (346 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.3 pandas-2.2.3 python-dateutil-2.9.0.post0 pytz-2025.1 six-1.17.0 tzdata-2025.1
(env1) PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> pip install pyjokes
Collecting pyjokes
  Downloading pyjokes-0.8.3-py3-none-any.whl.metadata (3.4 kB)
Downloading pyjokes-0.8.3-py3-none-any.whl (47 kB)
Installing collected packages: pyjokes
Successfully installed pyjokes-0.8.3
(env1) PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> pip freeze > requirement.txt
(env1) PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> deactivate
PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> .\env2\scripts\activate.ps1
(env2) PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps> pip install -r requirement.txt
Collecting numpy==2.2.3 (from -r requirement.txt (line 1))
  Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl.metadata (60 kB)
Collecting pandas==2.2.3 (from -r requirement.txt (line 2))
  Using cached pandas-2.2.3-cp313-cp313-win_amd64.whl.metadata (19 kB)
Collecting pyjokes==0.8.3 (from -r requirement.txt (line 3))
  Using cached pyjokes-0.8.3-py3-none-any.whl.metadata (3.4 kB)
Collecting python-dateutil==2.9.0.post0 (from -r requirement.txt (line 4))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz==2025.1 (from -r requirement.txt (line 5))
  Using cached pytz-2025.1-py2.py3-none-any.whl.metadata (22 kB)
Collecting six==1.17.0 (from -r requirement.txt (line 6))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting tzdata==2025.1 (from -r requirement.txt (line 7))
  Using cached tzdata-2025.1-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl (12.6 MB)
Using cached pandas-2.2.3-cp313-cp313-win_amd64.whl (11.5 MB)
Using cached pyjokes-0.8.3-py3-none-any.whl (47 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.1-py2.py3-none-any.whl (507 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tzdata-2025.1-py2.py3-none-any.whl (346 kB)
Installing collected packages: pytz, tzdata, six, pyjokes, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.3 pandas-2.2.3 pyjokes-0.8.3 python-dateutil-2.9.0.post0 pytz-2025.1 six-1.17.0 tzdata-2025.1
(env2) PS C:\workspace\01 code per day\python tutorial\chp13\chap13ps>
'''