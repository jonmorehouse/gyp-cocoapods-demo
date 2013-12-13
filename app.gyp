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

			"INFOPLIST_FILE" : "<(plist_file)",
			"CODE_SIGN_IDENTITY": "iPhone Developer: Sean McCoy (VB4U59V8X7)",
			"PRODUCT_NAME": "app",
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
				
			#"_sources": ["!@(find src -type f \( -name \"*.m\" -o -name \"*.h\" -o -name \"*.xib\" -o -name \"*.plist\" \))"],
			"sources": ['!@(pkg-config --libs-only-l apr-1)']
		}

	}, # GLOBAL CONDITIONS ETC

	# Schemes are user derived for running targets once they are built -- we don't want this as we want all developers to be able to run this automatically
	# targets = ["debug", "test", "release"]
	"targets": [
		{
			"target_name": "debug",
			"type": "executable",
			"mac_bundle": 1,
			"include_dirs" : [

				"src"
			],


			"link_settings": {
				
				# extra libraries needed for this target only
				"libraries": [],

				# default libraries to not include
				"libraries!": []
			},

      			"xcode_config_file": "../config/debug.xcconfig",
		},
	]# end of all targets
}
