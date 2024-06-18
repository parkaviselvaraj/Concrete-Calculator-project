import tkinter as tk
from tkinter import ttk

def concretecalculator():
    try:
        length=int(entry1.get())
        breadth=int(entry2.get())
        height=float(entry3.get())
        grade=dropdown.get()
        if grade=="M20":
            volume=length*breadth*height
            dryvolume=volume*1.54
            cement=(1/5.5)*dryvolume
            cementbag=cement//1.25
            sand=(1.5/5.5)*dryvolume
            aggregate=(3/5.5)*dryvolume
            result_str = f"Cementbag: {cementbag}\nSand in cft: {sand}cft\nAggregate in cft: {aggregate}cft"
            result.set(result_str)
        elif(grade=="M15"):
            volume=length*breadth*height
            dryvolume=volume*1.54
            cement=(1/7)*dryvolume
            cementbag=cement//1.25
            sand=(2/7)*dryvolume
            aggregate=(4/7)*dryvolume
            result_str = f"Cementbag: {cementbag}\nSand in cft: {sand}cft\nAggregate in cft: {aggregate}cft"
            result.set(result_str)
        elif(grade=="M25"):
            volume=length*breadth*height
            dryvolume=volume*1.54
            cement=(1/4)*dryvolume
            cementbag=cement//1.25
            sand=(1/4)*dryvolume
            aggregate=(2/4)*dryvolume
            result_str = f"Cementbag: {cementbag}\nSand in cft: {sand}cft\nAggregate in cft: {aggregate}cft"
            result.set(result_str)
        elif(grade=="M30"):
            volume=length*breadth*height
            dryvolume=volume*1.54
            cement=(1/3.25)*dryvolume
            cementbag=cement//1.25
            sand=(0.75/3.25)*dryvolume
            aggregate=(1.5/3.25)*dryvolume
            result_str = f"Cementbag: {cementbag}\nSand in cft: {sand}cft\nAggregate in cft: {aggregate}cft"
            result.set(result_str)
        elif(grade=="M35"):
            volume=length*breadth*height
            dryvolume=volume*1.54
            cement=(1/2.5)*dryvolume
            cementbag=cement//1.25
            sand=(0.5/2.5)*dryvolume
            aggregate=(1/2.5)*dryvolume
            result_str = f"Cementbag: {cementbag}\nSand in cft: {sand}cft\nAggregate in cft: {aggregate}cft"
            result.set(result_str)
        elif(grade=="M40"):
            volume=length*breadth*height
            dryvolume=volume*1.54
            cement=(1/1.75)*dryvolume
            cementbag=cement//1.25
            sand=(0.25/1.75)*dryvolume
            aggregate=(0.5/1.75)*dryvolume
            result_str = f"Cementbag: {cementbag}\nSand in cft: {sand}cft\nAggregate in cft: {aggregate}cft"
            result.set(result_str)
            
    except:
        result.set("Invalid input")
root=tk.Tk()
root.title("Concrete Calculator")
label1=tk.Label(root,text="Enter length in ft:")
label1.grid(row=0,column=0,padx=15,pady=15,sticky="w")
entry1=tk.Entry(root)
entry1.grid(row=0,column=1,padx=15,pady=15)
label2=tk.Label(root,text="Enter breadth in ft:")
label2.grid(row=1,column=0,padx=15,pady=15,sticky="w")
entry2=tk.Entry(root)
entry2.grid(row=1,column=1,padx=15,pady=15)
label3=tk.Label(root,text="Enter height in ft:")
label3.grid(row=2,column=0,padx=15,pady=15,sticky="w")
entry3=tk.Entry(root)
entry3.grid(row=2,column=1,padx=15,pady=15)

grade=["M15","M20","M25","M30","M35","M40"]
dropdown=ttk.Combobox(root,values=grade)
dropdown.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
dropdown.current(0)

concretecalculator_button = tk.Button(root, text="Calculate", command=concretecalculator)
concretecalculator_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

