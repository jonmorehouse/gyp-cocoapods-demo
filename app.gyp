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

		"plist_file": "src/app-Info.plist",

		"build_directory": "<!(pwd)/build",
	},

	# global conditions for application
	"target_defaults" : {

		"xcode_settings" : {

			"INFOPLIST_FILE" : "<(plist_file)",
			"CODE_SIGN_IDENTITY": "iPhone Developer: Sean McCoy (VB4U59V8X7)",
			"PRODUCT_NAME": "fruitstrap-demo",
			"GCC_PREFIX_HEADER": "",
			"GCC_PRECOMPILE_PREFIX_HEADER": "",
			"ALWAYS_SEARCH_USER_PATHS": "No",
			"INSTALLATION_DIRECTORY": "<(build_directory)",
			"CONFIGURATION_BUILD_DIR": "<(build_directory)",
			"HEADER_SEARCH_PATHS": "$(inherited)",
		},

		"link_settings": {

			"libraries": [

				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/CoreGraphics.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/Foundation.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/UIKit.framework",
			],
		},

		"type": "executable",
		"mac_bundle": 1,

		"include_dirs" : [

			"src"
		],

		# now go ahead and grab all of the correct source files for this application and insert them here
		"sources": ["<!@(find src -type f \( -name \"*.m\" -o -name \"*.h\" -o -name \"*.xib\" -o -name \"*.plist\" \))"],

	}, # GLOBAL CONDITIONS ETC

	# Schemes are user derived for running targets once they are built -- we don't want this as we want all developers to be able to run this automatically
	# targets = ["debug", "test", "release"]
	"targets": [

		# debug is for device testing as well as general development testing
		# this can also be updated to testflight as well
		{
			"target_name": "debug",
      			"product_name": "app.debug",
      			"xcode_config_file": "./config/debug.xcconfig",
			
			"postbuilds": [

				{
					"postbuild_name": "test",
					"action": ["/bin/bash", "/Users/MorehouseJ09/Desktop/test.sh"], 
				}
			],
		},

		# test is for testing only - unit testing in general
		{
			"target_name": "test",
			"product_name": "app.test",
      			"xcode_config_file": "./config/test.xcconfig",
		},

		# release for iOS application development
		{
			"target_name": "release",
			"product_name": "app.release",
      			"xcode_config_file": "./config/release.xcconfig",
      			"mac_bundle_resources": [

				# "test.xib",
				# "test.strings"
      			]
		},

		# now create an all target
		{
		
			"target_name": "all",
			"product_name": "app.all",
			"dependencies": [
				
				"debug",
				"test",
				"release",
			],
			
			"postbuilds": [

				{
					"postbuild_name": "test",
					"action": ["/bin/bash", "/Users/MorehouseJ09/Desktop/test.sh"], 
				}
			],
		}


	]# end of all targets
}
