import glob
import main_html_functions

input_file = open( "/Users/carlosgarzon/Desktop/DynamicBible/Bereshit_Data_Parsed.txt", "r")

#read file into a list of lines
lines_list = input_file.read().splitlines()

# Close the File stream handler
input_file.close()

# The OPEN function returns a file object
write_file = open("/Users/carlosgarzon/Desktop/DynamicBible/ch_data/ch1_bereshit.txt","w")

prev_chapter = "0"
current_chapter = "1"
valid_verse = False
new_chapter = False

#This parses the entire verse: Verse Loop
for index, var_list in enumerate(lines_list):

	#setup code
	word_list = var_list.split()
	#Double list: row( new line ) column( words 1-8 )
	verse_chunks =[word_list[x:x+32] for x in xrange(0, len(word_list), 32)]
	num_lines_in_verse = len(verse_chunks)									#number of chunks								
	num_w_last_chunk = len(verse_chunks[num_lines_in_verse - 1])

	#if the first word does not contain collon we do not have a valid loop
	word = verse_chunks[0][0]

	if ":" in word:
		valid_verse = True

	if valid_verse == True:
		chapter_verse = main_html_functions.replaceColon_Space( verse_chunks[0][0] )
		chapter_verse = chapter_verse.split()
		current_chapter = chapter_verse[0]
		main_html_functions.gen_write(write_file, "\n")
		print "\n",

		if current_chapter > prev_chapter:
			# The OPEN function returns a file object
			new_write_file = "ch" + current_chapter + "_bereshit.txt"
			write_file = open("/Users/carlosgarzon/Desktop/DynamicBible/ch_data/"+new_write_file,"w")
			new_chapter = True

		#Lines Loop
		for lineIndex in range(num_lines_in_verse):

			#Chunks Loop
			for chunksIndex in range( len(verse_chunks[lineIndex]) ):

				word = verse_chunks[lineIndex][chunksIndex]

				main_html_functions.gen_write(write_file, word)
				main_html_functions.gen_write(write_file, " ")
				print word + " ",

		prev_chapter = current_chapter

	new_chapter = False
	valid_verse = False