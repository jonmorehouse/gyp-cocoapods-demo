require "xcodeproj"

def update_project(project)

	project_file = File.join(Dir.pwd, project + ".xcodeproj")

	if  not File.exist? project_file 

		puts "Project file #{project_file} doesn't exist"

		return 
	end

	# now go ahead and open the project 
	project = Xcodeproj::Project.open project_file

	# now lets loop through each of the targets that are associated with this project file ...
	project.targets.each do |target|

		# xcconfig_file path 
		path = File.join Dir.pwd, "config", "#{target.name}.xcconfig"

		# grab the xxconfig file
		xcconfig_file = project.files.select do |f|

			# check that the names are correct and return this configuration file 
			f.name == "#{target.name}.xcconfig2"

		end.first || lambda do
			
			# make sure file exists and if so, add it to the file
			if File.exist? path
				
				# new file
				config_file = project.new_file path

				return config_file
			
			else

				return nil
			end

		end.call

		# stuck here -- keep getting weird "argument 
		if xcconfig_file == nil
			
			next
		end
			
		# now lets set the configuration ...
		target.build_configurations.each do |config|
				
			# if we have already created a configuration, update the path etc
			if config.base_configuration_reference
			
				config.base_configuration_reference.path = path

			# otherwise just create a new base_configuration
			else
				config.base_configuration_reference = xcconfig_file

			end
		end
	end

	# save the project
	project.save
end

if __FILE__ == $0

	update_project "app"		
	puts "Updated project app"

end


