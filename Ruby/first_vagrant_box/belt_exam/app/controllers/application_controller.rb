class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception
  

  def current_user
    @user = User.find(session[:current_user_id]) if session[:current_user_id]
  end

  helper_method :current_user


end

