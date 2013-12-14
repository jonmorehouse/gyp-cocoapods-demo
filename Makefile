all: project pods build

build:
	xcodebuild

project:
	gyp --depth=.

pods:
	pod install 

clean:
	rm -rf Pod.lock
	rm -rf Pods
	rm -rf *.xc*
