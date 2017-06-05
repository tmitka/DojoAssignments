class Song < ActiveRecord::Base
    belongs_to :user
    has_many :starred_users, through: starred
end
