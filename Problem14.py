def tagadder(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(tagadder('strong', 'JavaScript'))
print(tagadder('p', 'Js Tutorial'))