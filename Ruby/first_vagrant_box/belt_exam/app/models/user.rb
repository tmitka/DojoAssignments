class User < ActiveRecord::Base
  has_secure_password
  has_many :songs
  has_many :playlists
  has_many :playlist_songs, through: :playlists, source: :song
  validates :first_name, :last_name, :email, presence: true
end