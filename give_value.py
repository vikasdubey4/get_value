#python program to return values when object as a key value pair dictionary is passed.


def give_value(object=0 , key=0):
    a = dict(object)
    b = list(key)
    for x in a.keys():
	    return a.values()
    else :
        print("no value passed in object")
		
		


#Below are some sample test inputs to test the value return.
#Run the above code in python shell and pass function name along with the arguments as mentioned below.		
#give_value({"s":"r"} , "s")
#give_value({"hj":"cv"} , "hj")

#Below are sample output
 
#>>> give_value({"h":"l"},"h")
#dict_values(['l'])
#>>> 
#>>> give_value({"hj":"cv"} , "hj")
#dict_values(['cv'])
#>>>
