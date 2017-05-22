class LoginController < ApplicationController
  def index
  end

  def login
    user = User.find_by_username(params[:username])
    if user.password == params[:password]
      session[:id] = user.id
      redirect_to '/'
    else
      redirect_to'/login/index'
    end

   
  end
  def register
    # Redesigned to be "flatter"
    @user = User.new(username: params[:username], password: params[:password])
    if params[:password] != params[:confirm_password]
      flash[:errors] = ['Passwords do not match']
    end
    if !@user.valid?
      flash[:errors] = @user.errors.full_messages
    end
    if flash[:errors]
      render 'index'
    else
      @user.save
      session[:id] = @user.id
      return redirect_to '/'
    end
  end

  def logout
    reset_session
    redirect_to'/login/index'
  end

end
