class Song < ActiveRecord::Base
    belongs_to :user
    has_many :playlists
    has_many :playlist_users, through: :playlists, source: :user
    validates :title, :artist, presence: true, length: {minimum: 2}
end
