# -*- coding: utf-8 -*-

def remColon( chapterVerse ):
	return chapterVerse.replace(":","_")

# ########################################################
# HOW TO CALL THESE FROM OTHER FILE
# def blah():
# 	print "------> I am randomly printing this <------"
# Call this in main_js_python.py as follows
# ########################
# import main_js_functions
# main_js_functions.blah()
# ########################
# ########################################################

#####################################
#Functions used in html
#####################################
switchL_funcName1 	= "switch_Heb_Translit_"
switchL_funcName2   = "switch_Eng_AHL_"
L1 = "L1"
L2 = "L2"

######################################
# Arguments
######################################
#div order
# index = "1"
# chapter_verse = "1_7"
# line = "1"
# lang1_or_lang2 = "L1"

# orig_word = "bê'rey'shit"
# replacement_word = "בְּרֵאשִׁית"

######################################
#switch_Heb_Translit function calls
######################################
def switch_func_comment( write_file ):
	write_file.write("""//functionName_cahpter_verse_line""" + "\n")

def switch_Heb_Translit_header( write_file, chapter_verse, line):
	write_file.write( "function "+switchL_funcName1+chapter_verse+"_"+line+"""(idElement){"""+"\n")

def dwr_comment_HT( write_file ):
	write_file.write("\n"+"""	//1_Transliteration-->Heb 2_Heb_Transliteration""" + "\n")

def dynamic_word_replace( write_file, orig_word, replacement_word, index, chapter_verse, line, lang1_or_lang2):
	write_file.write("""    if( idElement == """+index+"""  &&  document.getElementById('divNum_"""+index+"_"+chapter_verse+"_"+lang1_or_lang2+"_"+line+"""').innerHTML == """+'"'+orig_word+'"'+"""){
      document.getElementById('divNum_"""+index+"_"+chapter_verse+"_"+lang1_or_lang2+"_"+line+"""').innerHTML ="""+'"'+replacement_word+'"'+""";
      return false;}""" + "\n")

def end_switch_Heb_Translit( write_file, chapter_verse, line):
	write_file.write("\n"+"""} //End of """+switchL_funcName1+chapter_verse+"_"+line+"""function\n\n""")

######################################
# switch_Eng_AHL function calls
######################################

# I already wrote switch function comment function <-- GOES HERE

def switch_Eng_AHL_header( write_file, chapter_verse, line):
	write_file.write( "function "+switchL_funcName2+chapter_verse+"_"+line+"""(idElement){"""+"\n")

def dwr_comment_EA( write_file ):
	write_file.write("\n"+"""	//1_AHL-->ENG 2_ENG_AHL""" + "\n")

# I alread wrote dynamic_word_replace  <-- GOES HERE

def end_switch_Eng_AHL( write_file, chapter_verse, line):
	write_file.write("\n"+"""} //End of """+switchL_funcName2+chapter_verse+"_"+line+"""function\n\n""")

######################################
# changeChapterLang function calls
######################################
def changeChapterLang_comment( write_file ):
	write_file.write("""//Change entire text to either Heb_&_Eng or Translit_&_Eng""" + "\n")

def changeChapterLang_header( write_file ):
	write_file.write("""function changeChapterLang(idElement){
  //switch between Heb and Eng or Transliteration and Eng"""+"\n\n")

def changeChapterLang_condition1( write_file ):  
    write_file.write("""	//Change all text to Hebrew and English
  if( idElement == 1){"""+"\n")

#####################
# Heb <--> Translit..
# Eng <--> AHL
####################
#first 3 parameters are ID NUM
def change_word( write_file, index, chapter_verse, line, lang1_or_lang2, replacement_word ):
	write_file.write("""      document.getElementById('divNum_"""+index+"_"+chapter_verse+"_"+lang1_or_lang2+"_"+line+"""').innerHTML ="""+'"'+replacement_word+"""";"""+"\n")

def changeChapterLang_condition1n2_end( write_file ):  
    write_file.write("""	return false;}"""+"\n\n")

def changeChapterLang_condition2( write_file ):  
    write_file.write("""	//Change all text to Transliteration and English
  if( idElement == 2){"""+"\n")

 # GOES HERE --> changeword(..) <-- GOES HERE

def changeChapterLang_condition1n2_end( write_file ):  
    write_file.write("""	return false;}"""+"\n")

def changeChapterLang_end( write_file ):
 	write_file.write("\n" + "}//endchangeChapterLang""" + "\n\n")


######################################
# execute code
######################################

# I had to put write_file as parameter for all of these

# ###################
# #changeChapterLang#
# ###################
# changeChapterLang_comment()
# changeChapterLang_header()
#
#	HEB_ENG
# changeChapterLang_condition1()
# change_word( index, chapter_verse, line, lang1_or_lang2, replacement_word )
# change_word( index, chapter_verse, line, lang1_or_lang2, replacement_word )
# change_word( index, chapter_verse, line, lang1_or_lang2, replacement_word )
# changeChapterLang_condition1n2_end()
#
#	TRANSLIT_ENG
# changeChapterLang_condition2()
# change_word( index, chapter_verse, line, lang1_or_lang2, replacement_word )
# change_word( index, chapter_verse, line, lang1_or_lang2, replacement_word )
# change_word( index, chapter_verse, line, lang1_or_lang2, replacement_word )
# changeChapterLang_condition1n2_end()
#
# changeChapterLang_end()
#############################################################################

# #####################
# #switch_Heb_Translit#
# #####################
# switch_func_comment()
# switch_Heb_Translit_header(chapter_verse, line)
# dwr_comment_HT()
# dynamic_word_replace( orig_word, replacement_word, index, chapter_verse, line, lang1_or_lang2 )
# dynamic_word_replace( orig_word, replacement_word, index, chapter_verse, line, lang1_or_lang2 )
# end_switch_Heb_Translit(chapter_verse, line)

# ################
# #switch_Eng_AHL#
# ################
# switch_func_comment()
# switch_Eng_AHL_header(chapter_verse, line)
# dwr_comment_EA()
# dynamic_word_replace( orig_word, replacement_word, index, chapter_verse, line, lang1_or_lang2 )
# dynamic_word_replace( orig_word, replacement_word, index, chapter_verse, line, lang1_or_lang2 )
# end_switch_Eng_AHL(chapter_verse, line)

