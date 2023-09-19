print("Please enter the following:\n")
adjective = input("adjective:")
animal = input("animal:")
verb0 = input("verb:")
exclamation = input("exclamation:")
verb1 = input ("verb:")
verb2 = input ("verb:")
a_an = "a"
print()
 
x = animal[0] 
if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
    a_an = "an" 
    

print("Your story is:\n")
print("Within a secluded forest, a " + adjective + " figure, \
cloaked in baggy attire, " + verb0 + " toward a \
concealed box. It was "+ a_an +' '+ animal +  " and " +verb2 +" off \
through the door. \"" + exclamation + "!\" I yelled. With a " + adjective + " grin,\
they " + verb1 + " through, setting off on an extraordinary \
journey across time and space.")