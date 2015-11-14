# -*- coding: utf-8 -*-

import main_js_functions

#main_js_python.py#
#################################Part 1###############################################
######################################################################################
# This should set up Heb Eng of changeChapterLanguage porition of js
######################################################################################
#open the file
ch = "2"
filePath = "/Users/carlosgarzon/Desktop/DynamicBible/ch_data/"+"bereshitCh"+ch+"/"
readFile = "ch"+ch+"_bereshit.txt"
writeFile = "ch"+ch+".js"
input_file = open( filePath+readFile, "r")

#read file into a list of lines
lines_list = input_file.read().splitlines()

# Close the File stream handler
input_file.close()

# The OPEN function returns a file object
write_file = open(filePath+writeFile,"w")

#I need to declare this for first iteration of for loop or to make my code a bit clearer
num_words = 0
chapter_verse = "1_1"
line = 0
L1 = main_js_functions.L1	#HebTransliteration if word%4 = 3 or 4
L2 = main_js_functions.L2	#EngAHL				if word%4 = 1 or 2
language = L1

#write comment, header for changeChapterLanguage
main_js_functions.changeChapterLang_comment(write_file)
main_js_functions.changeChapterLang_header(write_file)
# This loop will iterate condition 1
main_js_functions.changeChapterLang_condition1(write_file)

######################################################################################
# At this point there should NOT be bad data "But there was I add condition for this"
# out_main_js should be formated
# this loop should write Heb Eng of changeChapterLanguage porition of js
######################################################################################
for index, var_list in enumerate(lines_list): 
	#tric for splitin a string to a list of words
	word_list = var_list.split()

	num_words = len(word_list) - 1
	num_heb_words = num_words/4
	num_lines = num_heb_words/8
	num_hebWords_on_lastLine = num_heb_words%8

	if num_hebWords_on_lastLine > 0 and num_words > 8:
		num_lines = num_lines + 1

	line = 0
	# Parse a single line at a time
	for index, word in enumerate(word_list):
		#Break if we find bad data
		if word.isdigit():
			if int(word) < 8 and index%4 != 2:	# AHL on 2 bad data would be on 1
				break
		#we found a new verse
		if ':' in word:
			chapter_verse = main_js_functions.remColon( word )
		# line number
		if index%32 == 0:
			line = line + 1
		# language
		if index%4 == 3: #Hebrew
			language = L1
			main_js_functions.change_word( write_file, str(index), chapter_verse, str(line), language, word )
		if index%4 == 1: #English
			language = L2 								#weWant Heb indx
			main_js_functions.change_word( write_file, str(index), chapter_verse, str(line), language, word )
	#exit inner for loop		

#Finished writing condition1 for ChangChapterLang close it 
main_js_functions.changeChapterLang_condition1n2_end( write_file )

# Close the FILE object in PYTHON
write_file.close

#################################Part 2###############################################
######################################################################################
# this should set up Translit Eng portion of changeChapterLanguage porition of js
# At this point option 1 Heb/Eng should be written we should be on option 2 Translit Eng
# We are also appending to the file at this point and will continue doing so from here on out
######################################################################################
#open the file
input_file = open( filePath+readFile, "r")

#read file into a list of lines
lines_list = input_file.read().splitlines()

# Close the File stream handler
input_file.close()

# The OPEN function returns a file object
write_file = open(filePath+writeFile,"a")

#I need to declare this for first iteration of for loop or to make my code a bit clearer
num_words = 0
chapter_verse = "1_1"
line = 0
L1 = main_js_functions.L1	#HebTransliteration if word%4 = 3 or 4
L2 = main_js_functions.L2	#EngAHL				if word%4 = 1 or 2
language = L1

# This loop will iterate condition 2
main_js_functions.changeChapterLang_condition2(write_file)

######################################################################################
# this loop should write Translit Eng of changeChapterLanguage porition of js
######################################################################################
for index, var_list in enumerate(lines_list): 
	#tric for splitin a string to a list of words
	word_list = var_list.split()

	line = 0
	# Parse a single line at a time
	for index, word in enumerate(word_list):
		#Break if we find bad data
		if word.isdigit():
			if int(word) < 8 and index%4 != 2:	# AHL on 2 bad data would be on 1
				break
		#we found a new verse
		if ':' in word:
			chapter_verse = main_js_functions.remColon( word )
		# line number
		if index%32 == 0:
			line = line + 1
		# language
		if index%4 == 0: #Hebrew
			heb_Index = index - 1
			if heb_Index < 0:
				heb_Index = 0
			language = L1 								
			main_js_functions.change_word( write_file, str(heb_Index), chapter_verse, str(line), language, word )
		if index%4 == 1: #English
			language = L2
			main_js_functions
			main_js_functions.change_word( write_file, str(index), chapter_verse, str(line), language, word )
	#exit inner for loop		

#Finished writing condition1 for ChangChapterLang close it 
main_js_functions.changeChapterLang_condition1n2_end( write_file )

#Done with both conditions close the changeChapterLang function
main_js_functions.changeChapterLang_end( write_file )

# Close the FILE object in PYTHON
write_file.close

#################################Part 3###############################################
######################################################################################
# At this point option 1 and 2 Heb/Eng, Tranlit/Eng is written 
# This writes switch_Heb_Translit
######################################################################################
#open the file
input_file = open( filePath+readFile, "r")

#read file into a list of lines
lines_list = input_file.read().splitlines()

# Close the File stream handler
input_file.close()

# The OPEN function returns a file object
write_file = open(filePath+writeFile,"a")

#I need to declare this for first iteration of for loop or to make my code a bit clearer
num_words = 0
chapter_verse = "1_1"
line = 0
L1 = main_js_functions.L1	#HebTransliteration if word%4 = 3 or 4
L2 = main_js_functions.L2	#EngAHL				if word%4 = 1 or 2
language = L1

######################################################################################
# this loop should write Heb/Translit of switch_Heb_Translit func of js: 
######################################################################################
for index, var_list in enumerate(lines_list): 
	#tric for splitin a string to a list of words
	word_list = var_list.split()

	line = 0
	language = L1

	#print "\n\n---------------->switch_Heb_Translit LOOP<-------------------\n"	#DEBUG

	##################################################################################
	# One function per line. Each for loop writes functions for an entire verse
	# This For loop should be doing switch_Heb_Translit
	#################################################################################
	for index, word in enumerate(word_list):
		#Break if we find bad data
		if word.isdigit():
			if int(word) < 8 and index%4 != 2:	# AHL on 2 bad data would be on 1
				#print "(break)",	#DEBUG
				break
		#we found a new verse
		if ':' in word:
			chapter_verse = main_js_functions.remColon( word )
		# 	print "_" + word + "_" 	#DEBUG
		# else:						#DEBUG
		# 	print "->"+word+",index("+str(index)+")<--",	#DEBUG

		#Write the word replace if statments inside the function
		if index%4 == 0 and index != 0:# Hebrew: --> index + 1 = Translit 		#4				  #32  #(indx-1) so that we match js
			main_js_functions.dynamic_word_replace( write_file, word_list[index], word_list[index-1], str(index - 1), chapter_verse, str(line), language )
																#3					#4
			main_js_functions.dynamic_word_replace( write_file, word_list[index-1], word_list[index], str(index - 1), chapter_verse, str(line), language )
			#print "(replace:"+word_list[index]+","+word_list[index-1]+")",	#DEBUG

		# line number: Lines should start at 1
		# We are on a new line
		if index%32 == 0:
			line = line + 1
			#print "(addLine: "+str(line)+")",	#DEBUG

			# If !firstLine write end to previous line 
			if index != 0:
				main_js_functions.end_switch_Heb_Translit(write_file, chapter_verse, str(line) )
				#print "(end_Heb_Translit_func)",	#DEBUG

			#If we have no words left theres no use in writing headers
			#index starts at 0 but len !zero_index
			if (index+1) < len(word_list):
				main_js_functions.switch_func_comment( write_file )
				main_js_functions.switch_Heb_Translit_header(write_file, chapter_verse, str(line) )
				main_js_functions.dwr_comment_HT( write_file )
				#print "[printedHeaders:Index()"+str(index)+")wl_len("+str(len(word_list))+")]",	#DEBUG

		#print "--(END_ITERATION)--\n",	#DEBUG

	#exit inner for loop
	#Last line did NOT have exactly 8 words
	if index%32 != 0:
		main_js_functions.end_switch_Heb_Translit(write_file, chapter_verse, str(line) )
		#print "(Last_L_!8_words)",	#DEBUG

# Close the FILE object in PYTHON
write_file.close

#################################Part 4###############################################
######################################################################################
# At this point option 1 and 2 Heb/Eng, Tranlit/Eng is written 
######################################################################################
#open the file
input_file = open( filePath+readFile, "r")

#read file into a list of lines
lines_list = input_file.read().splitlines()

# Close the File stream handler
input_file.close()

# The OPEN function returns a file object
write_file = open(filePath+writeFile,"a")

#I need to declare this for first iteration of for loop or to make my code a bit clearer
num_words = 0
chapter_verse = "1_1"
line = 0
L1 = main_js_functions.L1	#HebTransliteration if word%4 = 3 or 4
L2 = main_js_functions.L2	#EngAHL				if word%4 = 1 or 2
language = L1

######################################################################################
# this loop should write ENG/AHL of switch_Eng_AHL func of js: 
######################################################################################
for index, var_list in enumerate(lines_list): 
	#tric for splitin a string to a list of words
	word_list = var_list.split()

	line = 0
	language = L2

	##################################################################################
	# One function per line. Each for loop writes functions for an entire verse
	# This For loop should be doing switch_Eng_AHL
	#################################################################################
	for index, word in enumerate(word_list):
		#Break if we find bad data
		if word.isdigit():
			if int(word) < 8 and index%4 != 2:	# AHL on 2 bad data would be on 1
				break
		#we found a new verse
		if ':' in word:
			chapter_verse = main_js_functions.remColon( word )

		#Write the word replace if statments, inside the function
		if index%4 == 2 and index != 0:# Hebrew: --> index + 1 = Translit 		#2				  #1
			main_js_functions.dynamic_word_replace( write_file, word_list[index], word_list[index-1], str(index - 1), chapter_verse, str(line), language )
																#1					#2
			main_js_functions.dynamic_word_replace( write_file, word_list[index-1], word_list[index], str(index - 1), chapter_verse, str(line), language )

		# line number: Lines should start at 1
		# We are on a new line
		if index%32 == 0:
			line = line + 1
			# If !firstLine write end to previous line 
			if index != 0:
				main_js_functions.end_switch_Eng_AHL(write_file, chapter_verse, str(line) )

			#If we have no words left theres no use in writing headers
			#index starts at 0 but len !zero_index
			if (index+1) < len(word_list):
				main_js_functions.switch_func_comment( write_file )
				main_js_functions.switch_Eng_AHL_header(write_file, chapter_verse, str(line) )
				main_js_functions.dwr_comment_EA( write_file )

	#exit inner for loop
	#Last line did NOT have exactly 8 words
	if index%32 != 0:
		main_js_functions.end_switch_Eng_AHL(write_file, chapter_verse, str(line) )

# Close the FILE object in PYTHON
write_file.close