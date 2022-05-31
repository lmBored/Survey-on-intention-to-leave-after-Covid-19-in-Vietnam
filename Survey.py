from tkinter import *
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt  
# import filedialog module
from tkinter import filedialog
def chart1():
    x = ['Hoàn toàn không đồng ý','Không đồng ý','Phân vân', 'Đồng ý', 'Hoàn toàn đồng ý']
    y = [17,25,37,27,13]
    fig = plt.figure(figsize=(10, 2))
    ax = fig.add_subplot(111)
    ax.bar(x, y, edgecolor = 'black')
    plt.title('Bảng khảo sát về dự định rời đi')
    plt.show()
def chart2(): 
    x = ['Hoàn toàn không đồng ý','Không đồng ý','Phân vân', 'Đồng ý', 'Hoàn toàn đồng ý']
    y = [20,119,90,60,10]
    fig = plt.figure(figsize=(10, 2))
    ax = fig.add_subplot(111)
    ax.bar(x, y, edgecolor = 'black')
    plt.title('Bảng khảo sát về số lượng giáo viên được khích lệ bởi cộng đồng')
    plt.show()
def chart3():
    # fig = plt.figure(figsize=(10, 5))
    plotdata = pd.DataFrame({
    "Công lập":[4,9,19,13,7],
    "Tư thục":[5,65,75,65,19],
    "Trung tâm khác":[4,9,19,13,6]
    }, 
    index=['Hoàn toàn không đồng ý','Không đồng ý','Phân vân', 'Đồng ý', 'Hoàn toàn đồng ý'])
    plotdata.plot(kind="bar")
    plt.title("Bảng khảo sát về số lượng  giáo viên nước ngoài đối với chính sách và hỗ trợ của nhà trường")
    plt.xlabel("Mức độ đồng ý")
    plt.ylabel("Số lượng")
    plt.show()
def chart4():    
    y = np.array([15,30,55])
    mylabels = ["15%","30%","55%"]
    plt.title("Khó khăn trong lịch thi học kỳ")
    plt.pie(y, labels = mylabels, startangle = 90)
    plt.show()                                                                                                  
window = Tk()
  
window.title('You have been rickrolled')
  
window.geometry("1000x500")
  
window.config(background = "white")
  
button_exit = Button(window,
                     text = " Exit ",
                     command = exit)
button_chart = Button(window,
                     text = " Bảng khảo sát về dự định rời đi ",
                     command = chart1)
button_chart2 = Button(window,
                     text = " Bảng khảo sát về số lượng giáo viên được khích lệ bởi cộng đồng ",
                     command = chart2)  
button_chart3 = Button(window,
                     text = " Bảng khảo sát về số lượng  giáo viên nước ngoài đối với chính sách và hỗ trợ của nhà trường ",
                     command = chart3)  
button_chart4 = Button(window,
                     text =  "Khó khăn trong lịch thi học kỳ ",
                     command = chart4)  


button_chart.grid(column = 1, row = 3, sticky=W)
button_chart2.grid(column = 1, row = 6, sticky=W)  
button_chart3.grid(column = 1, row = 9, sticky=W)  
button_chart4.grid(column = 1, row = 12, sticky=W)  
button_exit.grid(column = 1, row = 15, sticky=W)
  
window.mainloop()