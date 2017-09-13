import tkinter as tk
# ttk is for styling, similar to css
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation 
from matplotlib import style 
import json
import urllib
import pandas as pd
import numpy as np
#https://www.youtube.com/playlist?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk
# on part 7
print('test')
# phone book example - http://www.openbookproject.net/py4fun/gui/tkPhone.py
# lofin resource = https://www.youtube.com/watch?v=iCK8adSeG7A
# long tkinter intro https://www.youtube.com/watch?v=6isuF_bBiXs 

LARGE_FONT = ('Verdana', 12)
style.use('ggplot')
# this is for the animate method 
f = Figure(figsize=(5,5), dpi=100)
a= f.add_subplot(111)


def animate(interval):
	pullData= open('sampleData.txt', 'r').read()
	# .split('\n') means split at new line
	dataList = pullData.split('\n')
	xList = []
	yList = []
	for eachline in dataList:
		if len(eachline) > 1:
			x,y = eachline.split(',')
			xList.append(int(x))
			yList.append(int(y))
	# you dont have to clear but if you dont clear it will keep draw over and 
	# over shfitng the graph creating a messm also will take more ram
	a.clear()
	a.plot(xList, yList)



class TkinterExample(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		# fill makes it go to allocated space, expand fills limit beyond set
		container.pack(side='top', fill='both', expand=True)
		# 0 is minimum weight is priority
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frames = {}
		for F in (StartPage, PageOne, PageTwo, PageThree):
			frame = F(container, self)
			self.frames[F] = frame
			# sticky is north, south etc, coordinates
			frame.grid(row=0, column = 0, sticky='nsew')
		self.show_frame(StartPage)

	# cont is container/controller it is being thrown in frame
	def show_frame(self, cont):
		frame = self.frames[cont]
		# tk,raise is then run thru class pulling to raise frame
		frame.tkraise()

def qf(stringtoprint):
	print(stringtoprint)

# this is formula for each new page
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# tkinter code
		label = tk.Label(self, text='Start Page', font=LARGE_FONT)
		#padx and pady = padding
		label.pack(pady=10, padx=10)
		# add button to go to another page
		# command rus function on load
		# but work around is lambda to run on click
		button1 = ttk.Button(self, text='visit page 1', 
			command=lambda: controller.show_frame(PageOne))
		button1.pack()
		button2 = ttk.Button(self, text='visit page 2', 
			command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text='Graph Page', 
			command=lambda: controller.show_frame(PageThree))
		button3.pack()

class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Page One', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self, text='back to home', 
			command=lambda: controller.show_frame(StartPage))
		button1.pack()
		button2 = ttk.Button(self, text='visit page 2', 
			command=lambda: controller.show_frame(PageTwo))
		button2.pack()
		L1 = tk.Label(self, text='input').pack()
		E1 = tk.Entry(self, bd=5).pack()
		# actually get text
		var1 = tk.StringVar(self)
		Lwork = tk.Label(self, text='this should work below').pack()
		Ework = tk.Entry(self, textvariable=var1).pack()
		click_button = ttk.Button(self, text='click to execute',
			command=lambda: print(var1.get())).pack()


	def show_var(self):
		text = self.var.get()
		print(text)

class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Page Two', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self, text='back to home', 
			command=lambda: controller.show_frame(StartPage))
		button1.pack()
		button2 = ttk.Button(self, text='visit page 1', 
			command=lambda: controller.show_frame(PageOne))
		button2.pack()
		# inserting text 
		# getting text from user 
		L1 = tk.Label(self, text='user name')
		L1.pack()
		E1 = tk.Entry(self, bd=5)
		E1.pack()
		text = tk.Text(self, width=40, height=20)
		text.insert('1.0', 'enter story below')
		text.pack()
		# dont know hoe to get text yet, bottomis not doing anything
		user_text = text.get('1.0', 'end')
		if user_text == 'mike':
			print('got text')
		#user_text.pack()
		

class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Graph Page', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self, text='back to home', 
			command=lambda: controller.show_frame(StartPage))
		button1.pack()

		"""
		# this is blocked out due to new animation added
		f = Figure(figsize=(5,5), dpi=100)
		a= f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8], [5,4,3,8,5,3,9,7])
		"""
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = TkinterExample()
# for animation, animate is the animate method, 1000 is in ms so 
# this is one second, f is the figure 
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()

"""
Guis research 
1. list of different guis - http://insights.dice.com/2017/08/07/7-top-python-gui-frameworks-for-2017-2/
2. more on kivy - http://opensourceforu.com/2016/02/developing-python-based-android-apps-using-kivy/
3. kivy apps on google play https://github.com/kivy/kivy/wiki/List-of-Kivy-Projects
pyqt also cross platform - https://riverbankcomputing.com/software/pyqt/intro
pyside also cross platform - https://wiki.qt.io/PySide_Tutorials
course on kivy - https://www.udemy.com/develop-android-apps-using-python-kivy/
"""