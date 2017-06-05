class EventsController < ApplicationController
  def index
    @state_events = Event.where(state: current_user.state)
    @not_state_events = Event.where.not(state: current_user.state)
  end

  def create
    @event = Event.new event_params
    @event.user = current_user
    unless @event.save
      flash[:errors]= @event.errors.full_messages
    end
    redirect_to '/events'
  end

  def show
    @event = Event.includes(:user, :attending_users).find(params[:event_id])
    @messages = Message.includes(:user).where(event: @event)
  end

  def destroy
    @event = Event.find(params[:event_id])
    @event.destroy
    redirect_to '/events'
  end

  def join
    @event = Event.find(params[:event_id])
    @event.attending_userscount
    redirect_to '/events'

  end

  def leave
    @event = Event.find(params[:event_id])
    @attending = Attending.find_by(user:current_user, event:@event)
    @attending.destroy
    redirect_to '/events'
  end

  private
    def event_params
      params.require(:event).permit(:name, :location, :state, :date)
    end
end
