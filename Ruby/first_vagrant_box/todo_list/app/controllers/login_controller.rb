class LoginController < ApplicationController
  def index
  end

  def login
    user = User.find_by(username: params[:username])
    if user.password == params[:password]
      session[:id] = user.id
      puts session[:id]
      redirect_to '/'
    else
      redirect_to'/login/index'
    end

   
  end
  def register
    if params[:password] == params[:confirm_password]
     user = User.create(username: params[:username], password: params[:password])
    end

    session[:id] = user.id
    redirect_to '/'
    

  end
  def logout
    reset_session
    redirect_to'/login/index'

  end

end
