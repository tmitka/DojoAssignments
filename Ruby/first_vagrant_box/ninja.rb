require_relative 'human'

class Ninja < Human
    def initialize
        super
        @stealth = 174
    end

    def get_away
        @health -= 15
    end

    def steal(obj)
        if obj.class.ancestors.include?(Human)
            @health += 10
            true
        else
            false
        end
    end
end