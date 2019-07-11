age = 20
name = 'Swaroop'
# numbers (indexes) for variables inside {} are optional
print '{} was {} years old when he wrote this book'.format(name, age)
print 'Why is {} playing with that python?'.format(name)

# decimal (.) precision of 3 for float '0.333'
print '{0:.3f}'.format(1.0/3)
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print '{0:_^11}'.format('hello')
# keyword-based 'Swaroop wrote A Byte of Python'
print '{name} wrote {book}'.format(name='Swaroop',
book='A Byte of Python')

# comma to prevent newline (\n) after print
print "a",
print "b"

print '''This is a triple-quoted
string print in Python'''

print 'This is the first line\nThis is the second line'

print 'This is the first line\tThis is the second line after a tab'

print "This is the first sentence. \
This is the second sentence."

# raw strings, prefix r or R
print r"Newlines are indicated by \n"