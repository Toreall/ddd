name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %r." % name
print "He's %0.2f cm tall." % (height * 2.5)
print "He's (%r.*3) pounds heavy." % height
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
     age, height, weight, age + height + weight)