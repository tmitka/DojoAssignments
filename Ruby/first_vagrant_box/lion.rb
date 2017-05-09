require_relative 'mammal'

class Lion < Mammal
    def initialize
    super
        @health = 170
        puts "This is a lion"
    end

    def fly
        @health -= 10
        self
    end

    def attack_town
        @health -= 50
        self
    end

    def eat_humans
        @health += 20
        self
    end

end

lion = Lion.new

lion.attack_town.attack_town.attack_town.eat_humans.eat_humans.fly.fly.display_health