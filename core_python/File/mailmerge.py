# Python program to mainl merger
# Names are in thee file names.txt
# Body  of the mail is in body.txt

# Open names.txt for reading

with open("body.txt",'r',encoding='utf-8') as body_file:

	# Open body.txt for reading
	with open("body.txt",'r',encoding='utf-8') as body_file:

		#read entire content of the body
		body=body_file.read()

		# iterate over names
		for name in names_file:
			main="Hello"+name+body

			#write the mails to individual files
			with open(name.strip()+".txt",'w',encoding='utf-8') as mail_file:
				mail_file.write(mail)