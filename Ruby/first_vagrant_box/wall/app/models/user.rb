class User < ActiveRecord::Base
    has_many :messages
    has_many :comments
    validates :name, :email, :password, presence => true
    validates :email, uniqueness => true
end
