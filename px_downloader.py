# coding: utf-8

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


class PXdownloader(object):
    def __init__(self):
        self.create_widget()

    def create_widget(self):

        # top-level window
        self.win = Tk()
        self.win.title("500PX Pic Downloader")
        self.win.geometry('500x200+400+400')
        self.win.maxsize(500, 200)
        self.win.minsize(500, 200)

        # main Frame
        content = LabelFrame(self.win, text="Save Settings", padding=(3, 3, 12, 12))
        content.grid(padx=10, pady=(15, 0), sticky=(N, S, E, W))

        fr_url = Frame(content)
        url_label = Label(fr_url, width=10, text="Pic url:")
        self.url_entry = Entry(fr_url, width=50)  # used to get url for pic
        fr_url.grid(padx=(0, 5), pady=10)
        url_label.grid(row=0, column=0)
        self.url_entry.grid(row=0, column=1)

        fr_savepath = Frame(content)
        savepath_label = Label(fr_savepath, width=10, text="File Path:")
        self.savepath_entry = Entry(fr_savepath, width=46)   # used to get save path 
        btn_setpath = Button(fr_savepath, text="...", width=2, command=self.setpath)
        fr_savepath.grid(padx=(0, 5), pady=10)
        savepath_label.grid(row=0, column=0)
        self.savepath_entry.grid(row=0, column=1)
        btn_setpath.grid(row=0, column=2)

        fr_btns = Frame(content)
        btn_download = Button(fr_btns, text="Download", command=self.download)
        btn_quit = Button(fr_btns, text="Quit", command=self.quit)
        btn_download.grid(row=0, column=0)
        btn_quit.grid(row=0, column=1)
        fr_btns.grid()

        v = StringVar()  # from Tkinter
        self._label = v
        status = Label(self.win, textvariable=self._label)
        status.grid()

        self.win.mainloop()

    def setpath(self):
        self.savepath_entry.delete(0, END)
        self.savepath_entry.insert(0, filedialog.askdirectory()+'/')

    def quit(self):
        self.win.destroy()

    def download(self):
        # reference from github https://github.com/figengungor/500px, it's an easy one
        import urllib.request
        import urllib.parse
        import urllib.error
        link = self.url_entry.get().strip()
        name = self.savepath_entry.get().strip()

        if link and name:
            try:
                f = urllib.request.urlopen(link)
                pageResource = f.read().decode()
                pattern = "{\"size\":2048,\"url\":"
                start = pageResource.find(pattern)+20
                end = pageResource.find("\"", start+2)
                imgLink = pageResource[start:end]
                imgLink = imgLink.replace("\\", "")
                urllib.request.urlretrieve(imgLink, name + '.jpg')
                self._label.set("photo downloaded on: {0}".format(name))
            except Exception as e:
                self._label.set("download fail! {0}".format(e))
        else:
            self._label.set('please input url and save path')


if __name__ == '__main__':
    app = PXdownloader()
