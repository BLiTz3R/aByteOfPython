shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
print 'Character 0 is', name[0]

# Slicing on a list #
print 'Items 1 to 3 is', shoplist[1:3]
print 'Items 2 to end is', shoplist[2:]
print 'Items 1 to -1 is', shoplist[1:-1]
print 'Items start to end is', shoplist[:]

# You can also provide a third argument for the slice, which is the step for the slicing (by
# default, the step size is 1):
print 'Items with step 1 are', shoplist[::1]
print 'Items with step 2 are', shoplist[::2]
print 'Items with step 3 are', shoplist[::3]
print 'Items with step -1 are', shoplist[::-1]


