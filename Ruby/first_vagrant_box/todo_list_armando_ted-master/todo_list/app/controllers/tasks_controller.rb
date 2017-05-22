class TasksController < ApplicationController
  def index
    if session[:id]   
      @user = User.find(session[:id])
      # @tasks = Task.where(user_id: @user)  # Use model helpers
      @tasks = @user.tasks  # available because `has_many :tasks`
    else
      redirect_to '/login/index'
    end
  
  
  end

  def new
  end

  def create
    
    user = User.find(session[:id])
    # Task.create(name:params['name'], status:false, user:user)
    user.tasks.create(name: params[:name], status: false)  # using the `has_many` helper
    redirect_to '/'
  end

  def edit

    task = Task.find(params[:id])
    # if task_id.status == true  # ?? Is it an id, or is it a task?
    #   task_id.status = false
    # else
    #   task_id.status = true
    # end
    task.status = !task.status
    task.save
    redirect_to '/'

  end
end
