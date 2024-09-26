import tkinter as tk
from fileDownloader import download_file



root = tk.Tk()
root.title("File Downloader")
root.geometry('600x250')

# Create a label widget
label = tk.Label(root, text='Enter the URL of the file to download:')
label.grid(row=0, column=0)


# Create an entry widget
URLWidget = tk.Entry(root, width=50)
URLWidget.grid(row=0, column=1)

# create a label widget
fileNameWidget = tk.Entry(root, text="Enter the name of the file to save:")
fileNameWidget.grid(row=1, column=1)

#create a button widget
def download():
    url = URLWidget.get()
    file_name = fileNameWidget.get()
    download_file(url, file_name)
    
    
# Create a download button
download_button = tk.Button(root, text="Download", command=download)
download_button.grid(row=2, column=1)

root.mainloop()