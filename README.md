iOS Gyp / CocoaPods Sample Project
----------------------------------

Overview
--------

Proof of concept app for iOS team management. Project and dependencies are all scripted so as to promote easy building and cross developer collaboration between teams. No Xcode Required!!!

Build Xcode Project Using Gyp
----------

Install Gyp:

```
brew tap jonmorehouse/tap
brew install gyp
make gyp
```
Install Cocoapods
-----------------

```
bundle install
rvm reload
pod install
```

Initialize XCodeSchemes
-----------------------

In the future, this should be automated -- possibly using the Podfile post_install block?

```
open app.xcworkspace
```

Build Project
------------

```
xcodebuild -workspace app.xcworkspace -scheme -all build
```

List Project Schemes
------------

```
xcodebuild -workspace app.xcworkspace -list
```

