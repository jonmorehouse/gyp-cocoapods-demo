all: clean gyp pods open

list:
	xcodebuild -workspace 'app.xcworkspace' -list

build:
	xcodebuild -workspace 'app.xcworkspace' -scheme all

gyp:
	gyp app.gyp --depth=. -f xcode -DOS=ios

pods:
	pod install 

open:
	open app.xcworkspace

clean:
	rm -rf ~/Library/Developer/Xcode/DerivedData/
	rm -rf Pod.lock
	rm -rf Pods
	rm -rf *.xc*
	rm -rf Gemfile.lock
