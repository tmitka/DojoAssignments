# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def list_to_tuple(dictionary):
    new_list = []
    for key, value in dictionary.iteritems():
        new_list.append((key))
        new_list.append((value))
    new_list = tuple(new_list)
    print new_list

list_to_tuple(my_dict)