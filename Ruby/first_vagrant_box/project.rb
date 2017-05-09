class Project
    def initialize(name, description)
        @name = name
        @description = description
    end

    def name
        puts "#{@name}"
    end

    def elevator_pitch
        puts "#{@name}, #{@description}"
    end

end

project1 = Project.new("Project 1", "Description 1")
puts project1.name
puts project1.elevator_pitch