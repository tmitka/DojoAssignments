class Call(object):
    def __init__(self, id, name, number, time_of_call, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time_of_call = time_of_call
        self.reason = reason

    def display_call_info(self):
        print self.id
        print self.name
        print self.time_of_call
        print self.reason

call1 = Call(1, "Ted", "708-555-5555", "7:00PM", "Ordering food")
call2 = Call(2, "Mike", "708-666-6666", "8:00PM", "Calling to reserve a cab")
call3 = Call(3, "Nick", "708-777-7777", "11:00PM", "Thinking about his ex")
call4 = Call(4, "Stark", "708-888-8888", "6:00AM", "Calling in sick to work")


class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.call_queue = len(self.calls)

    def add_call(self, call):
        self.calls.append(call)

center = CallCenter([call1])
center.add_call(call1)
