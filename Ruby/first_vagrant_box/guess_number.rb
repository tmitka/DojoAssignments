def guess_number(guess)
    number = 25
    if guess > number
        puts "The guess was too high"
    elsif guess < number
        puts "The guess was too low"
    else
        puts "You got it!"
    end
end

guess_number(26)
guess_number(24)
guess_number(25)