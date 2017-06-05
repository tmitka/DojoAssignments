class User < ActiveRecord::Base
  has_secure_password
  has_many :songs
  has_many :starred_playlist, through :starred, source: :song 
end
