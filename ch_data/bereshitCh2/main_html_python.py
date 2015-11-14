# -*- coding: utf-8 -*-

import main_html_functions
import sys	#for command line arguments

#main_html_python.py#http://showlove.github.io/DynamicBible/ch_data/bereshitCh2/ch2.html#
#################################Part 1###############################################
######################################################################################
# This should set up Heb Eng of changeChapterLanguage porition of js
######################################################################################
 
# Get the total number of args passed
num_arguments = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)
 
# Print it
print ("The total numbers of args passed to the script: %d " % num_arguments)
print ("Args list: %s " % cmdargs)

# str(sys.argv[0])	name of file you are compiling
# str(sys.argv[1])	chapter
# str(sys.argv[2])	filePath not including ber..ch folder
# Python main_html_python.py  2 /Users/carlosgarzon/Desktop/DynamicBible/ch_data/
# Python main_js_python.py  2 /Users/carlosgarzon/Desktop/DynamicBible/ch_data/

ch = sys.argv[1]
filePath = sys.argv[2]+"bereshitCh"+ch+"/"
readFile = "ch"+ch+"_bereshit.txt"
writeFile = "ch"+ch+".html"
input_file = open( filePath+readFile, "r")
#read file into a list of lines
lines_list = input_file.read().splitlines()

# Close the File stream handler
input_file.close()

# The OPEN function returns a file object
write_file = open(filePath+writeFile,"w")

write_file.write(""" <!--div id index, chapter_vers, Language, line -->\n """)
write_file.write(""" <!--http://showlove.github.io/DynamicBible/ch_data/bereshitCh2/ch2.html -->\n """)

#Writess the top portion of html code
main_html_functions.header( write_file )

L1 = main_html_functions.L1	#HebTransliteration if word%4 = 3 or 4
L2 = main_html_functions.L2	#EngAHL				if word%4 = 1 or 2

######################################################################################
# this loop should write Heb/Transliteration div wrap And the ENG AHL div wrap 
######################################################################################
for index, var_list in enumerate(lines_list): 
	#tric for splitin a string to a list of words
	word_list = var_list.split()

	#Double list: row( new line ) column( words 1-8 )
	verse_chunks =[word_list[x:x+32] for x in xrange(0, len(word_list), 32)]

	#Finds last word in verse
	num_lines_in_verse = len(verse_chunks)									#number of chunks								
	num_w_last_chunk = len(verse_chunks[num_lines_in_verse - 1])			#size of chunk
	#print verse_chunks[ num_lines_in_verse - 1][ num_w_last_chunk - 1]		#DEBUG

	#Print verse in lines of 8, HEB then ENG.
	for lineIndex in range(num_lines_in_verse):

		#setup code
		chapter_verse = main_html_functions.remColon( verse_chunks[0][0] )
		language = L1

		#beginning of hebrew divs
		main_html_functions.lang1_header( write_file )

		#Hebrew for loop
		for chunksIndex in range( len(verse_chunks[lineIndex]) ):

			language = L1

			word = verse_chunks[lineIndex][chunksIndex]

			#Break if we find bad data
			if word.isdigit():								#DEBUG ERROR! CHANGE in~him 0000...
				if int(word) < 8 and chunksIndex%4 != 2:	# AHL on 2 bad data would be on 1
					break

			#We want to highlight the first verse
			if chunksIndex == 0  and lineIndex == 0:
				main_html_functions.lang1_newVerse( write_file, verse_chunks[0][0] )

			#write divs
			if chunksIndex%4 == 3 and chunksIndex != 0: #Print hebrew words
				main_html_functions.changeWord( write_file, str(lineIndex*32 + chunksIndex), chapter_verse, str(lineIndex + 1), language, word)
				#print verse_chunks[lineIndex][chunksIndex] + ",",	#DEBUG

		#end of heb divs
		main_html_functions.end_lang1_2_divWrapper( write_file )

		#print "\n\n",	#DEBUG########################################################

		#beginning of hebrew divs
		main_html_functions.lang2_header( write_file )

		#English for loop
		for chunksIndex in range( len(verse_chunks[lineIndex]) ):

			language = L2

			word = verse_chunks[lineIndex][chunksIndex]

			#Break if we find bad data
			if word.isdigit():								#DEBUG ERROR! CHANGE in~him 0000...
				if int(word) < 8 and chunksIndex%4 != 2:	# AHL on 2 bad data would be on 1
					break

			#We want to highlight the first verse
			if chunksIndex == 0  and lineIndex == 0:
				main_html_functions.lang2_newVerse( write_file, verse_chunks[0][0] )

			#write divs
			if chunksIndex%4 == 1 and chunksIndex != 0: #Print Eng words
				main_html_functions.changeWord2( write_file, str(lineIndex*32 + chunksIndex), chapter_verse, str(lineIndex + 1), language, word)
				#print verse_chunks[lineIndex][chunksIndex] + ",",	#DEBUG

		#end of heb divs
		main_html_functions.end_lang1_2_divWrapper( write_file )

		#print "\n\n",	#DEBUG



# Close the FILE object in PYTHON
write_file.close

main_html_functions.w_tail( write_file )