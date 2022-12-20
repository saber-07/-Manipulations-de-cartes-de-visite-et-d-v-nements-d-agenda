import tkinter
from tkinter import filedialog
from tkinter import ttk
import vobject
from convert import vcarComponent
from convert import v2h

root = tkinter.Tk()
root.title('Vcard app')
root.iconbitmap('../rsc/logo_vcard_bco.ico')
root.geometry("500x450")


class Main:
    def __init__(self, master):
        rootFrame = tkinter.Frame(master)
        rootFrame.pack()

        self.open_button = tkinter.Button(master, text="Open Vcard File", command=self.open_file)
        self.open_button.pack(pady=20)

        self.submit_button = tkinter.Button(master, text="Submit Vcard File", command=self.submit_file)
        self.submit_button.pack(pady=20)

        self.modify_button = tkinter.Button(master, text="Modify Vcard File", command=self.modify_file)
        self.modify_button.pack(pady=20)

        self.entry_doc = tkinter.Entry(master)
        self.entry_doc.pack()

        self.convert_button = tkinter.Button(master, text="Convert Vcard File", command=self.html_convert)
        self.convert_button.pack(pady=20)

        """self.save_button = tkinter.Button(master, text="save csv File", command=self.save_file)
        self.save_button.pack(pady=20)"""

    def open_file(self):
        global inputPath
        inputPath = filedialog.askopenfilename(initialdir="../rsc", title='select a file',
                                               filetypes=(("vcf files", "*.vcf"), ("ics files", "*.ics")))
        self.entry_doc.insert(0, inputPath)

    def submit_file(self):
        global content
        s = open(inputPath, 'r')
        v = vobject.readOne(s)
        odc = vcarComponent.get_info_list(v, inputPath)
        content = ''
        for key, value in odc.items():
            content = content + str(key) + ':\t' + str(value) + '\n'

        top = tkinter.Toplevel()
        top.title('Vcard viewer')
        top.geometry("500x450")

        my_text = tkinter.Label(top, text=content)
        my_text.pack(pady=20)

    def modify_file(self):
        top = tkinter.Toplevel()
        top.title('Vcard modifier')
        top.geometry("500x450")

        firstname_text = tkinter.Label(top, text="First name :")
        firstname_text.place(x=15, y=75)

        lastname_text = tkinter.Label(top, text="Last name :")
        lastname_text.place(x=15, y=125)

        company_text = tkinter.Label(top, text="Company :")
        company_text.place(x=15, y=175)

        mail_text = tkinter.Label(top, text="Mail address")
        mail_text.place(x=15, y=225)

        cell_phone_text = tkinter.Label(top, text="Cell phone")
        cell_phone_text.place(x=15, y=275)

        work_phone_text = tkinter.Label(top, text="Work phone")
        work_phone_text.place(x=175, y=275)

        home_phone_text = tkinter.Label(top, text="Home phone")
        home_phone_text.place(x=315, y=275)

        note_text = tkinter.Label(top, text="Note")
        note_text.place(x=15, y=315)

        firstname = tkinter.StringVar()
        firstname_entry = tkinter.Entry(top, textvariable=firstname, width=30)
        firstname_entry.place(x=15, y=100)

        lastname = tkinter.StringVar()
        lastname_entry = tkinter.Entry(top, textvariable=lastname, width=30)
        lastname_entry.place(x=15, y=150)

        company = tkinter.StringVar()
        company_entry = tkinter.Entry(top, textvariable=company, width=30)
        company_entry.place(x=15, y=200)

        mail = tkinter.StringVar()
        mail_entry = tkinter.Entry(top, textvariable=mail, width=30)
        mail_entry.place(x=15, y=250)

        cellphone = tkinter.StringVar()
        cellphone_entry = tkinter.Entry(top, textvariable=cellphone, width=30)
        cellphone_entry.place(x=15, y=300)

        workphone = tkinter.StringVar()
        workphone_entry = tkinter.Entry(top, textvariable=workphone, width=30)
        workphone_entry.place(x=175, y=300)

        homephone = tkinter.StringVar()
        homephone_entry = tkinter.Entry(top, textvariable=homephone, width=30)
        homephone_entry.place(x=315, y=300)

        note = tkinter.StringVar()
        note_entry = tkinter.Entry(top, textvariable=note, width=30)
        note_entry.place(x=15, y=350)

        def save_info():
            vcard = vobject.vCard()
            vcard.add('n')
            vcard.n.value = vobject.vcard.Name(family=lastname.get(), given=firstname.get())
            vcard.add('fn')
            vcard.fn.value = firstname.get() + ' ' + lastname.get()
            vcard.add('org')
            vcard.org.value = [company.get()]
            vcard.add('email')
            vcard.email.value = mail.get()
            vcard.add('tel')
            vcard.tel.value = cellphone.get()
            vcard.tel.type_param = 'CELL'
            vcard.tel_list.append(vobject.base.ContentLine('TEL', [['TYPE', 'WORK']], workphone.get()))
            vcard.tel_list.append(vobject.base.ContentLine('TEL', [['TYPE', 'HOME']], homephone.get()))
            vcard.add('note')
            vcard.note.value = note.get()
            with open(root.filename, 'w') as f:
                vcard = vcard.serialize()
                f.write(vcard.strip().replace('\n', ''))

        register = tkinter.Button(top, text="Register", width=10, height=1, command=save_info, bg="grey")
        register.place(x=0, y=400)

    def html_convert(self):
        inputFile = inputPath
        outputFile = inputFile + ".html"
        v2h.vcard2html(inputFile, outputFile)

        progress = tkinter.Tk()
        progress.title("progress....")
        progress.geometry("400x90+4900+400")
        progress.resizable(False, False)

        progress_bar = ttk.Progressbar(progress, length=365, orient='horizontal', mode="determinate")
        progress_bar.pack()

        """progress_label = tkinter.Label(progress, text="Converting...", font=("Arial", 10), fg="Black")
        progress_label.pack()

        tasks = 10
        x=0
        while x<tasks:
            time.sleep(1)
            progress_bar ["value"] += 10
            x += 1
            progress.update_idletasks()
            progress.destroy()

            messagebox.showinfo("Info", "DOC File Converted to csv sucssefully")"""

    """def save_file(self):
        global inputPath, outputPath
        inputPath = tkinter.filedialog.asksaveasfile(title="save the file",
                                                     filetypes=(("csv Files", "*.csv"), ("html files", "*.html")))

        outputFile = ".html"
        outputPath.write(outputFile)
        outputPath.close()"""


main = Main(root)
root.mainloop()
