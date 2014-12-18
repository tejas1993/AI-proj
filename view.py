import Tkinter as tk 
import tkMessageBox

#top = tk.Tk()
#frame = tk.Frame(top)
#frame.grid()
nameList = ["AXP","BA","CAT","CSCO","CVX","DD","DIS","GE","GS","HD","IBM","INTC","JNJ",\
"JPM","KO","MCD","MMM","MRK","MSFT","NKE","PFE","PG","T","TRV","UNH","UTX","V","VZ","WMT","XOM"]

day_num = [0,31,28,31,30,31,30,31,31,30,31,30,31]

top = tk.Tk()
frame = tk.Frame(top)
frame.grid()	

def make_images():
	photo_list = []
	for s in nameList:
		p = tk.PhotoImage(file = "logos\\" + s + ".gif")
		photo_list.append(p)
	return photo_list

def predict(n):

	new_top = tk.Tk()

	label1 = tk.Label(new_top, text = "Date: mm/dd/yyyy")
	ent1 = tk.Entry(new_top, width = 2)
	label2 = tk.Label(new_top, text = "/")
	ent2 = tk.Entry(new_top, width = 2)
	label3 = tk.Label(new_top, text = "/") 
	ent3 = tk.Entry(new_top, width = 4)
	b = tk.Button(new_top, text = "Predict!", command = lambda: callback(n, [ent1,ent2,ent3], [label1,label2,label3], new_top))

	label1.pack(side = tk.LEFT)
	ent1.pack(side = tk.LEFT)
	label2.pack(side = tk.LEFT)
	ent2.pack(side = tk.LEFT)
	label3.pack(side = tk.LEFT)
	ent3.pack(side = tk.LEFT)
	b.pack(side = tk.BOTTOM)

	new_top.wm_title("Prediction for: " + n)

	new_top.mainloop()

def callback(n, t, l, nt):
	#do some prediction shit
	m = int(t[0].get())
	d = int(t[1].get())
	y = int(t[2].get())
	#assertions
	assert(m>0 and m <= 12)
	assert(d>0 and d<= day_num[m])


	#get rid of stuff.
	for i in range(3):
		t[i].destroy()
		l[i].destroy()

	#Predictions
	#a = [] the prediction
	label1 = tk.Label(nt, text = "Actual Value: ")
	label2 = tk.Label(nt, text = "xx.xx")
	label3 = tk.Label(nt, text = "Predicted Value: ")
	label4 = tk.Label(nt, text = "xx.xx")

	label1.pack(side = tk.LEFT)
	label2.pack(side = tk.LEFT)
	label3.pack(side = tk.LEFT)
	label4.pack(side = tk.LEFT)

	print("predict "+n+" for "+str(m)+"/"+str(d)+"/"+str(y))

def predict_AXP():
	predict("AXP")
def predict_BA():
	predict("BA")
def predict_CAT():
	predict("CAT")
def predict_CSCO():
	predict("CSCO")
def predict_CVX():
	predict("CVX")
def predict_DD():
	predict("DD")
def predict_DIS():
	predict("DIS")
def predict_GE():
	predict("GE")
def predict_GS():
	predict("GS")
def predict_HD():
	predict("HD")
def predict_IBM():
	predict("IBM")
def predict_INTC():
	predict("INTC")
def predict_JNJ():
	predict("JNJ")
def predict_JPM():
	predict("JPM")
def predict_KO():
	predict("KO")
def predict_MCD():
	predict("MCD")
def predict_MMM():
	predict("MMM")
def predict_MRK():
	predict("MRK")
def predict_MSFT():
	predict("MSFT")
def predict_NKE():
	predict("NKE")
def predict_PFE():
	predict("PFE")
def predict_PG():
	predict("PG")
def predict_T():
	predict("T")
def predict_TRV():
	predict("TRV")
def predict_UNH():
	predict("UNH")
def predict_UTX():
	predict("UTX")
def predict_V():
	predict("V")
def predict_VZ():
	predict("VZ")
def predict_WMT():
	predict("WMT")
def predict_XOM():
	predict("XOM")

function_list = [predict_AXP,predict_BA,predict_CAT,predict_CSCO,predict_CVX,predict_DD,predict_DIS,predict_GE,predict_GS,predict_HD,predict_IBM,predict_INTC,predict_JNJ,predict_JPM,predict_KO,predict_MCD,predict_MMM,predict_MRK,predict_MSFT,predict_NKE,predict_PFE,predict_PG,predict_T,predict_TRV,predict_UNH,predict_UTX,predict_V,predict_VZ,predict_WMT,predict_XOM]

def run():

	#top = tk.Tk()
	#frame = tk.Frame(top)
	#frame.grid()	
	top.wm_title("Dow Jones Financial Predictor")
	r = 0
	c = 0 
	
	photo_list = make_images()
	for i in range(30):
		b = tk.Button(frame, image = photo_list[i], height = 70, width = 70, command = function_list[i])
		b.grid(row = r, column = c)
		r = r+1
		if r == 5:
			r = 0
			c = c+1

	top.mainloop()

run()