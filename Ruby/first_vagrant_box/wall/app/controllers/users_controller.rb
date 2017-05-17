class UsersController < ApplicationController
  def index
  end

  def login
    user = User.find_by(username: params[:username])
    if user.password == params[:password]
      session[:id] = user.id
      puts session[:id]
      redirect_to '/wall'
    else
      redirect_to'/index'
    end
  end
  end
