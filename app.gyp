{
	# This file should contain any project specific configuration / applications
	# All xcode config files should be agile between projects
	# should be primarily responsible for any user-changing elements 
	# ie: frameworks, provisioning profile, output paths etc

	# initialize global variables as needed for application
	"variables" : {

		# sdk version of application being used
		"ios_sdk_version": "7.0",

		# sdk directory that we are currently using
		"ios_sdk_dir": "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS",

		"plist_file": "src/app-Info.plist"
	},

	# global conditions for application
	"target_defaults" : {

		"xcode_settings" : {

			"INFOPLIST_FILE" : "<(plist_file)>",
			"CODE_SIGN_IDENTITY": "",
			"PRODUCT_NAME": "",
			"GCC_PREFIX_HEADER": "",
			"GCC_PRECOMPILE_PREFIX_HEADER": "",
			"ALWAYS_SEARCH_USER_PATHS": "No",
		},

		"link_settings": {

			"libraries": [

				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/CoreGraphics.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/Foundation.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/UIKit.framework",
			],
		}

	}, # GLOBAL CONDITIONS ETC

	# Schemes are user derived for running targets once they are built -- we don't want this as we want all developers to be able to run this automatically
	# targets = ["device", "development (just build)", "sim (development) + run in sim", "testflight", "release"]
	"targets": [
		{
			"target_name": "development",
			"type": "executable",
			"mac_bundle": 1,
			"include_dirs" : [

				"src"
			],

			"sources": [

				"src/SGAppDelegate.m", 
				"src/SGViewController.m",
				"src/main.m",
				"src/fruitstrap-demo-Info.plist"
			],

			"link_settings": {
				
				# extra libraries needed for this target only
				"libraries": [],

				# default libraries to not include
				"libraries!": []
			},

      			"xcode_config_file": "../config/development.xcconfig",

		},
		{
			# this is responsible for placing onto the device i'm currently testing with
			"target_name": "device",
			"type": "executable",
			"mac_bundle": 1,
			"dependencies": [
			
				"development",

			],
			"run_as": {
				
				# environment variables that need to be exported to be run on this application
				"environment": {},
				"working_directory": "/Users/MorehouseJ09/Desktop",
				"action": ["test.sh"]
			},
			
		}, # end of target
	]# end of all targets



}
