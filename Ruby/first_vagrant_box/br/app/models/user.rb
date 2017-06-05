class User < ActiveRecord::Base
  has_secure_password
  has_many :events
  has_many :messages
  has_many :attendings
  has_many :attending_events, through: :attendings, source: :event
  validates :first_name, :last_name, :email, :location, :state, presence: true

end
