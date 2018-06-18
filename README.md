### How to run tests on android emulator
* Run appium server - $appium --chromedriver-executable /Users/sjankowski/Work/fincompare/assets/chromedriver
* Run android emulator - $ANDROID_HOME/tools/emulator -avd EM1
* Run tests - $python runtests.py -c android
