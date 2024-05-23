from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from add_informatin import Student
class DeleteStudentMark:

    def __init__(self, root):
        self.root = root
        self.root.title('Delete Student Mark')
        self.root.geometry('1350x750+0+0')
        
        self.Myanmar = StringVar()
        self.English = StringVar()
        self.Math = StringVar()
        self.Physics = StringVar()
        self.Chemistry = StringVar()
        self.Biology = StringVar()
        self.RollNo = StringVar()
        self.Name = StringVar()

        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "project"
        )

        self.mycursor = self.mydb.cursor()

        ##########################Frame...........
        self.MainFrame = Frame(self.root)
        self.MainFrame.grid()

        ####Title
        self.rollsearch = Label(self.MainFrame, font=('Arial',20,'bold'), text='Student Record Form', padx=2, pady=2, bg='Ghost White')
        self.rollsearch.grid(row=0, column=0, sticky='w')
        

        ##########################Widget...........
        self.rollS = Label(self.MainFrame, font=('Arial', 14, 'bold'), text=' Enter Roll No That You Want To Add Mark', padx=2, pady=2)
        self.rollS.grid(row=2, column=0, sticky='w')
        self.txtSearchroll = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.RollNo, width=28)
        self.txtSearchroll.grid(row=2, column=1)

        self.lbName = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Name', padx=2, pady=2)
        self.lbName.grid(row=3, column=0, sticky='w')
        self.txtName = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Name, width=28)
        self.txtName.grid(row=3, column=1)

        #row 1
        self.lbMyanmar = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Myanmar', padx=2, pady=2)
        self.lbMyanmar.grid(row=4, column=0, sticky='w')
        self.txtMyanmar = Label(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Myanmar, width=28)
        self.txtMyanmar.grid(row=4, column=1)

        #row 2
        self.lbEnglish = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='English', padx=2, pady=2)
        self.lbEnglish.grid(row=5, column=0, sticky='w')
        self.txtEnglish = Label(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.English, width=28)
        self.txtEnglish.grid(row=5, column=1)

        #row 3
        self.lbMath = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Math ', padx=2, pady=2)
        self.lbMath.grid(row=6, column=0, sticky='w')
        self.txtMath = Label(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Math, width=28)
        self.txtMath.grid(row=6, column=1)

        #row 4
        self.lbPhysics = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Physics', padx=2, pady=2)
        self.lbPhysics.grid(row=7, column=0, sticky='w')
        self.txtPhysics = Label(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Physics, width=28)
        self.txtPhysics.grid(row=7, column=1)

        #row 5
        self.lblChemistry = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Chemistry', padx=2, pady=2)
        self.lblChemistry.grid(row=8, column=0, sticky='w')
        self.txtChemistry = Label(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Chemistry, width=28)
        self.txtChemistry.grid(row=8, column=1)

        #row 6
        self.lblBiology = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Biology', padx=2, pady=2)
        self.lblBiology.grid(row=9, column=0, sticky='w')
        self.txtBiology = Label(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Biology, width=28)
        self.txtBiology.grid(row=9, column=1)
        self.txtBiology.grid(row=9, column=1)

        ##button
        self.btnSearch = Button(self.MainFrame, text='Search Student Mark', font=('Arial',12,'bold'), height=1, width=16,bd=2, padx=13, command=self.search_student)
        self.btnSearch.grid(row=13, column=0)

        self.btnDelete = Button(self.MainFrame, text='Delete Student Mark', font=('Arial',12,'bold'), height=1, width=16,bd=2, padx=13, command=self.delete_student)
        self.btnDelete.grid(row=15, column=0)

        self.btnHome = Button(self.MainFrame, text='Home', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, command=self.Home)
        self.btnHome.grid(row=17, column=0)

        self.btnExit = Button(self.MainFrame, text='Exit', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, command=self.Exit)
        self.btnExit.grid(row=19, column=0)

        

    def search_student(self):
         # Get the roll number entered by the user for searching
        roll_to_search = self.RollNo.get()
        name_to_search=self.Name.get()
        # Write your SQL query to fetch student details based on the roll number
        query = "SELECT * FROM Student_Mark WHERE RollNo = %s and Name= %s"
        self.mycursor.execute(query, (roll_to_search,name_to_search))
        studentMark = self.mycursor.fetchone()

        # Populate the Entry fields with the fetched student details
        if studentMark:
            # Display the roll number
            self.RollNo.set(studentMark[0])
            self.Name.set(studentMark[1])
            # Set the fetched student details to the respective variables or directly to Entry widgets
            self.Myanmar.set(studentMark[2])
            self.English.set(studentMark[3])
            self.Math.set(studentMark[4])
            self.Physics.set(studentMark[5])
            self.Chemistry.set(studentMark[6])
            self.Biology.set(studentMark[7])
            
        else:
            messagebox.showerror("Error", "Student not found")


    def Exit(self):
        # Implement logic to go back to the home page or close the window
        # For example:
        self.root.destroy()

    def Home(self):
        from AddMark_Student_page import AddMark
        AddWindow = Toplevel(self.root)
        AddMark(AddWindow)
    
    def delete_student(self):
        roll_to_delete = self.RollNo.get()

        # Check if the roll number is provided
        if not roll_to_delete:
            messagebox.showerror("Error", "Please enter a Roll Number to delete")
            return

        # Ask for confirmation before deleting the record
        confirmation = messagebox.askyesno("Delete", "Are you sure you want to delete this student?")
        if confirmation:
            try:
                # Write your SQL query to delete student details based on the roll number
                query = "DELETE FROM Student_Mark WHERE RollNo = %s"
                self.mycursor.execute(query, (roll_to_delete,))
                self.mydb.commit()  # Commit the transaction

                # Clear the fields after deletion
                self.clear_fields()

                messagebox.showinfo("Success", "Student record deleted successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error deleting student: {err}")

    def clear_fields(self):
        self.RollNo.set("")
        self.Name.set("")
        self.Myanmar.set("")
        self.English.set("")
        self.Math.set("")
        self.Physics.set("")
        self.Chemistry.set("")
        self.Biology.set("")


if __name__ == '__main__':
    root = Tk()
    application = DeleteStudentMark(root)
    root.mainloop()

