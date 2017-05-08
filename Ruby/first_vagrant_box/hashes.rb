2.3.1 :002 > h = {:first_name => "Coding", :last_name => "Dojo"}
 => {:first_name=>"Coding", :last_name=>"Dojo"}
2.3.1 :003 > h.delete(:last_name)
 => "Dojo"
2.3.1 :004 > print h
{:first_name=>"Coding"} => nil
2.3.1 :005 > print h #
{:first_name=>"Coding"} => nil
2.3.1 :006 > def new_user user = {first_name: "first", last_name: "last"}
2.3.1 :007?>
2.3.1 :008 >
2.3.1 :009 >     puts "Welcome to our site, #{user[:first_name]} #{user[:last_name]}!"
2.3.1 :010?>   end
 => :new_user
2.3.1 :011 > our_user = {first_name: 'Oscar', last_name: "Vazquez"}
 => {:first_name=>"Oscar", :last_name=>"Vazquez"}
2.3.1 :012 > new_user
Welcome to our site, first last!
 => nil
2.3.1 :013 > new_user our_user
Welcome to our site, Oscar Vazquez!
 => nil
2.3.1 :014 > def new_user first_name: "first", last_name: "last"
end2.3.1 :015?>     puts "Welcome to our site, #{first_name} #{last_name}!"
2.3.1 :016?>   end
 => :new_user
2.3.1 :017 >
2.3.1 :018 >   def new_user greeting="Welcome", first_name: "first", last_name: "last"
2.3.1 :019?>       puts "#{greeting}, #{first_name} #{last_name}"
2.3.1 :020?>   end
 => :new_user
2.3.1 :021 >
2.3.1 :022 >   our_user = {first_name: "Oscar", last_name: "Vazquez"}
 => {:first_name=>"Oscar", :last_name=>"Vazquez"}
2.3.1 :023 > new_user
Welcome, first last
 => nil
2.3.1 :024 > new_user "Hello", our_user
Hello, Oscar Vazquez
 => nil
