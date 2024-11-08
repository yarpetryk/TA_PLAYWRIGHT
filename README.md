## Setup (Python 3.10+)

1. Configure a virtual environment for PyCharm: 
   1. File>Settings>Project Interpreter>Settings icon> Add Local 
2. Change Test Runner for PyCharm: 
   1. File>Settings>Tools>Python Integrated Tools>Default test runner>PyTest
3. Execute in terminal: 
   1. pip install -r requirements.txt
4. Change your local settings in config.json'


### Run all tests

```
pytest
```

### Run tests matching given mark expression

```
pytest -m smoke
```


### Run an arbitrary file
```
pytest <NameOfFile>.py
```

### Install playwright browser engine's
```
playwright install
```

### Run playwright test with different options
```
pytest -m <mark> [*options]
options:
--headed
--browser [chromium, firefox, webkit]
--device ["iPhone 13",]
--screenshot [on, only-on-failure]
--video [on, retain-on-failure]
--tracing [on,]
```

### Run an Allure report generation
1. Download and extract Allure into the Program Files (https://github.com/allure-framework/allure2/releases/)
2. Add Path in the system variables to the allure bin folder:
   1. Path (C:\Program Files\allure\bin)


```
pytest --alluredir=allure-results
allure serve ./allure-results
```