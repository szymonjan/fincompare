#### General info
This repositorium contains automated tests for Twitter webpage (https://twitter.com/). Three features are being tested:
- sending a tweet
- searching for a twitter profile
- following profile

#### Project organization

	/twitter_tests
		/assets - place non-code files used tests (e.g. drivers)
		/configs - location of config files.
		/data - data files (like CSV files).
		/reference-screenshots - if enabled, reference screenshots are placed here.
		/reports - test result HTML files.
		/screenshots - if enabled, screenshots taken on test failures will go here.
		/tests - top level package for test code.
			/flows - high level reuseable multipage flows.
			/models - data models go here. (like DataBase ORM code)
			/pages - page objects go here.
			/support - reuseable support utility functions go here.
			/testdata - custom code for working with test data.
			/tests - all tests go here.

#### Requirements
* Python 3.4+
* Pip 9+
* Chrome 62+

#### How to run tests
1. Clone this repository 

```git clone https://github.com/szymonjan/twitter_tests.git```

2. Install all required packages 

```pip install -r requirements.txt```

3. Install modified WTFramework from github

```pip install git+https://github.com/szymonjan/wtframework_mod.git```

4. Run the tests 

```python runtests.py```