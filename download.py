from tkinter import*
from pytube import YouTube
root=Tk()
#Tai xuong video va xu ly khi link loi
def down():
	label_status.config(text="Đang tải , vui lòng chờ vài phút")
	link=entry_link.get()
	yt=YouTube(link)
	stream=yt.streams.get_highest_resolution()
	try:
		stream.download()
		label_status.config(text="Tải xuống thành công")
	except:
		label_status.config(text="Link lỗi")
		
#Tieu de
label_title=Label(root,text="DOWNLOAD VIDEO YOUTUBE",font=("Times New Roman",12,"bold"),bg="red",fg="black",width=35)
label_title.pack()
#Nhap link video va tao nut xac nhan
lbl_link=Label(root,text="Nhập link đến video: ",font=("Arial",8,"bold"),bg="white")
lbl_link.place(x=3,y=250)
entry_link=Entry(root,width=26)
entry_link.place(x=290,y=250)
but_submit=Button(root,text="Xác nhận",command=down)
but_submit.place(x=200,y=590)
label_status=Label(root,text="")
label_status.place(x=150,y=450)
root.mainloop()