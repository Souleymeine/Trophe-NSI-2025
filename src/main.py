#!/usr/bin/python

#Projet : pyscape
#Auteurs : Rabta Souleymeine

import os
import sys
import asyncio
from TUI_elements.box import Box
from TUI_elements.text_area import TextArea
from data_types import RGB, Alignment, Anchor, HorizontalAlignment, Coord, VerticalAlignment
from escape_sequences import gohome, goto, ANSI_Styles
from terminal import*


async def main():
	init_term()

	# De https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
	notice_path = os.path.join(os.path.dirname(__file__), "../notice_aux_eleves.txt")
	with open(notice_path, "r", encoding="utf-8") as file:
		data = file.read()

	notice_text_area = TextArea(data, ANSI_Styles.BOLD,
						  Alignment(HorizontalAlignment.CENTER, VerticalAlignment.MIDDLE),
						  Box(Anchor.TOP_LEFT, Coord(1, 1), Coord(125, 35), True, RGB(255, 100, 0), True))
	
	termsize = os.get_terminal_size()

	for _ in range(termsize.columns - notice_text_area.box.dimentions.x):
		notice_text_area.box.dimentions.x += 1
		notice_text_area.draw()
		await asyncio.sleep(0.05)
		gohome()
		sys.stdout.write("\x1b[2J")

	notice_text_area.draw()

	goto(Coord(1, termsize.lines))
	input("Appuie sur 'Entrer' pour quitter.")

	reset_term()

if __name__ == '__main__': 
	asyncio.run(main())
	# try:
	# 	asyncio.run(main())
	# except KeyboardInterrupt:
	# 	exit_gracefully()

def exit_gracefully():
	reset_term()
	sys.exit(0)

