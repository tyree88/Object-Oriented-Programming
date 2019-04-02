class Stack:
	'''
	Simple stack class created by Bill Bulko that uses the native Python list object
	'''
	
	# initiate the stack with no elements
	def __init__(self):
		self.items = []
		
	# check if the stack is empty or not
	def isEmpty(self):
		return self.items == []
	
	def size(self):
		return len(self.items)
	
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[-1]
	
	def __str__(self):
		return str(self.items)



def getTags(line):
	'''
	get all of the tags in a single line and return them in a list
	'''
   
	# list to hold the tags found
	tags = []
	
	# itterate through the line to find all the tags
	for i in range(len(line)):
		# "<" character marks the start of a tag, retrieve the name of the tag
		if line[i] == "<":
			tag = ""
			i += 1
			# continue itterating through the string until you reach the end of
			# the tag. This loop assumes that all tags close, the i <= len(line)
			# is there only to insure that the code does not fail when it runs out
			# of characters
			while (line[i] != ">" and line[i] != " ") and i <= len(line):
				tag += line[i]
				i += 1
			tags.append(tag)
			
	# return all the tags found
	print(tags)
	return tags



def checkTags(tags):
	'''
	Iterates through a list of tags (in the order they appeared) and
	validates whether or not all of the tags have both an opening and
	closing tag
	'''
	
	# these are the known exceptions that do not need a closing tag
	exceptions = ['meta', 'br', 'hr']
	# validTags will hold the unique tags found
	validTags = []
	
	# create a stack to help with checking
	s = Stack()
	
	# itterate through all the tags
	print()
	for tag in tags:
		
		# check if tag is an exception
		if tag in exceptions:
			print("Tag %s does not need to match:  stack is still %s" % (tag, s))
			continue
			
		# if opening tag, add to stack
		if tag[0] != "/":
			
			# if tag is new, let the user know and add to validTags
			if tag not in validTags:
				validTags.append(tag)
				print("New tag %s found and added to list of valid tags" % (tag))
			
			# add tag to the stack
			s.push(tag)
			print("Tag %s pushed:  stack is now %s" % (tag, s))
				  
		
			
		# if closing tag, check stack
		else:
			
			# if the stack is empty, let the user know and abort
			if s.isEmpty():
				print("Error:  tag is %s but the stack is empty" % (tag, lastTag))
				return
			print(s)
			# pop the last tag, this tag should be equal to the current tag
			lastTag = s.pop()
			
			# if the closing tag matches the last tag, let the user know and continue
			if ("/" + lastTag) == tag:
				print("Tag %s matches top of stack:  stack is now %s" % (tag, s))
				continue
			# if it does match, let the user know and abort
			else:
				print("Error:  tag is %s but top of stack is %s" % (tag, lastTag))
				endMessage(exceptions, validTags)
				return
	print()
		
	# once all tags have been itterated through, print out the results
	
	# if there are no tags left 
	if s.isEmpty():
		print("Processing complete.  No mismatches found.")
	# if there were tags left
	else:
		print("Processing complete.  Unmatched tags remain on stack:  %s" % (s))
		
	# print the sorted exceptions and valid tags
	#endMessage(exceptions, validTags)


def main():
	'''
	Parse through an html file (in the form of a .txt file) and makes
	sure all opening tags have closing tags if a closing tag is needed
	'''
	
	# assuming that htmlfile.txt is the file we want to read
	# open the file
	inFile = open("HTML.txt", "r")
	# gather all of the tags from the file
	tags = []
	for line in inFile:
		tags = tags + getTags(line)
	# close the file
	inFile.close()

	# print the tags found
	print()
	print("Tags Found:")
	print(tags)
	print()
	
	# check if all of the tags have closing tags
	checkTags(tags)
main()
