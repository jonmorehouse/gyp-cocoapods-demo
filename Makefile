all: project pods build

build:
	xcodebuild

gyp:
	gyp app.gyp --depth=. -f xcode -DOS=ios

pods:
	pod install 

clean:
	rm -rf ~/Library/Developer/Xcode/DerivedData/
	rm -rf Pod.lock
	rm -rf Pods
	rm -rf *.xc*
	rm -rf Gemfile.lock
