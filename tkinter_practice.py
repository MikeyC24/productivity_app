import tkinter as tk
# ttk is for styling, similar to css
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
#https://www.youtube.com/playlist?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk
# on part 7
print('test')

LARGE_FONT = ('Verdana', 12)

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

class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Graph Page', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self, text='back to home', 
			command=lambda: controller.show_frame(StartPage))
		button1.pack()

		f = Figure(figsize=(5,5), dpi=100)
		a= f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8], [5,4,3,8,5,3,9,7])
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = TkinterExample()
app.mainloop()