class UsersController < ApplicationController
    def index
    end
    
    def new
    end

  def create
    @user = User.new user_params
    if @user.save
      session[:current_user_id]= @user.id
      redirect_to "/songs"
    else
      flash[:errors]= @user.errors.full_messages
      redirect_to '/users'
    end
  end

    def login
    @user = User.find_by_email(params[:email]).try(:authenticate,params[:password])

    if @user
      session[:current_user_id] = @user.id
      redirect_to '/songs'
    else
      flash[:errors] = ["Invalid email or password"]
      redirect_to '/users'
    end
end

  def logout
    session.clear
    redirect_to '/users'
  end

  def show
  @user = User.find(params[:id])
  end

  private
    def user_params
      params.require(:user).permit(:first_name, :last_name, :email, :password, :password_confirmation)
    end



end
