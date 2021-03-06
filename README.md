#### Requirements
* Python 3.4+
* Pip 9+
* Chrome 66+
* Latest chromedriver (add it to the `assets` folder)

#### Environment setup
1. Clone this repository 
```git clone https://github.com/szymonjan/fincompare.git```
2. Install all required packages 
```pip install -r requirements.txt```
3. Install modified WTFramework from github
```pip install git+https://github.com/szymonjan/wtframework_mod.git```
4. Add basic auth data from 1pass - vault Fincompare - in /tests/testdata/settings

##### To run tests locally on Chrome
* Run tests ```python runtests.py -c chrome```

##### To run tests on android emulator
* Run appium server - ```appium --chromedriver-executable assets/chromedriver```
* Run android emulator - ```$ANDROID_HOME/tools/emulator -avd EM1```
* Run tests - ```python runtests.py -c android```

