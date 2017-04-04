info = {}
info["name"] = "Ted Mitka"
info["age"] = "25"
info["country"] = "USA"
info["language"] = "english"

#for key,data in info.iteritems():
#    print key, "=", data

def dictionary_info(dictionary):
    for item in dictionary:
        print "My {} is {}".format(item, dictionary[item])

dictionary_info(info)