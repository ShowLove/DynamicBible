# -*- coding: utf-8 -*-

#####################################
#   """+'"'+t_word1+""""
#####################################
#####################################
#Functions that will be called in JS
#####################################
switchL_funcName1 	= "switch_Heb_Translit_"
switchL_funcName2   = "switch_Eng_AHL_"
L1 = "L1"
L2 = "L2"
######################################
#Classes that are referenced in css
######################################
dynamicButton  = "change_verse_state"	# buttons to change entire text
eight_w_verses = "Heb_Transliteration"  # heb to transliteration
eight_w_verses_newV	    = "lang1_newVerse"	# the bold bereshit
eight_w_verses_newV2	= "lang2_newVerse"	# the bold bereshit
eight_w_verses2= "English_AHL"			# the eng and ahl numbers
######################################

def remColon( chapterVerse ):
	return chapterVerse.replace(":","_")

######################################
# Arguments
######################################
#div order
# index = "1"
# chapter_verse = "1_7"
# line = "1"

# orig_word = "bê'rey'shit"
# replacement_word = "בְּרֵאשִׁית"
# word = "בְּרֵאשִׁית"
# lang1_or_lang2 = "L1"

def header( write_file ):
	write_file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
<HEAD>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<TITLE>
		בְּרֵאשִׁית
	</TITLE>
</HEAD>
<BODY bgcolor = "black">

	<div class="""+'"'+dynamicButton+"""" style="width:100%; float:right; color:red">
		<div onclick="javascript:changeChapterLang(1); return false;">   ( איפוס עברית )/( ENG RESET )</div>
	</div>

	<H1 ALIGN="CENTER" style="color:red">בְּרֵאשִׁית</H1>

""")

#####################################
# Language 1 div wrapper
#####################################
def lang1_header( write_file ):
	write_file.write("""	<div class="""+'"'+eight_w_verses+"""" style="width:100%; float:right;">""" +"\n")

def lang1_newVerse( write_file, chapter_verse ):
	write_file.write("""		<div class="""+'"'+eight_w_verses_newV+"""" style="font-size:165%">{"""+chapter_verse+"""}</div>"""+"\n")

def changeWord( write_file, index, chapter_verse, line, lang1_or_lang2, word):
	write_file.write("""		<div id="divNum_"""+index+"_"+chapter_verse+"_"+lang1_or_lang2+"_"+line+""""
			onclick="javascript:"""+switchL_funcName1+chapter_verse+"_"+line+"""("""+str(index)+"""); return false;">"""+word+"""</div>"""+"\n")

def end_lang1_2_divWrapper( write_file ):
	write_file.write("""	</div>""" + "\n\n")

#####################################
# Language 2 div wrapper
#####################################
def lang2_header( write_file ):
	write_file.write("""	<div class="""+'"'+eight_w_verses2+"""" style="width:100%; float:right;">""" +"\n")

def lang2_newVerse( write_file, chapter_verse ):
	write_file.write("""		<div class="""+'"'+eight_w_verses_newV2+""""></div>"""+"\n")

def changeWord2( write_file, index, chapter_verse, line, lang1_or_lang2, word):
	write_file.write("""		<div id="divNum_"""+index+"_"+chapter_verse+"_"+lang1_or_lang2+"_"+line+""""
			onclick="javascript:"""+switchL_funcName2+chapter_verse+"_"+line+"""("""+str(index)+"""); return false;">"""+word+"""</div>"""+"\n")

def w_tail( write_file ):
	write_file.write("""\n\n	<A NAME="32"> </A>

	</BODY>
</HTML>""")


#####################################
# execute dode
#####################################
# header()
# # language 1 div wrap # #
# lang1_header()
# lang1_newVerse() # only use on a new verse
# changeWord(index, chapter_verse, line, lang1_or_lang2, word)
# changeWord(index, chapter_verse, line, lang1_or_lang2, word)
# end_lang1_2_divWrapper()
#
# # language 2 div wrap # #
# lang2_header()
# lang2_newVerse()
# lang1_or_lang2 = "L2"   #this is just so output looks nice
# changeWord2(index, chapter_verse, line, lang1_or_lang2, word)
# changeWord2(index, chapter_verse, line, lang1_or_lang2, word)
# end_lang1_2_divWrapper()
# # tail of code
# w_tail()
#####################################
#
#####################################