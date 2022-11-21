#!/usr/bin/env python3
import db
import models

# Make these settings match your Makefile
user="notes"
password="swordfish"
dbname="notes"
port="3334"


def menu():
    print("Welcome to the note tool")
    print("------------------------")
    print()
    print("1: Initialise Database")
    print("2: List notes")
    print("3: Add note")
    print("4: Read note")
    print("5: Delete note")
    print("6: List Categories")
    print("7: New Category")
    print("8: Notes by category")
    print("0: Quit")
    print()
    return int(input("Choose option: "))

if __name__=="__main__":

    session=db.connect(user,password,port,dbname)
    
    userInput=None

    while userInput!=0:
        userInput=menu()
        print()
        if userInput==1:            
            db.create_db(user,password,port,dbname)

        elif userInput==2:            
            notes=session.query(models.Note).all()
            for note in notes:
                print(f"{note.id}: [{note.category.name}] {note.title}")
                
        elif userInput==3:
            catNum=int(input("Enter category number: "))
            cat = session.query(models.Category).filter_by(id=catNum).first()
            if cat==None:
                print("No category exists with that number")
            else:
                title=input("Enter new note title: ")
                content=input("Enter new note content: ")
                newNote = models.Note(title=title,content=content, category=cat)
                session.add(newNote)    
                session.commit()

        elif userInput==4:
            noteNum=int(input("Enter note number: "))
            note = session.query(models.Note).filter_by(id=noteNum).first()
            if note==None:
                print("There is no note with that number")
            else:
                print(note.title)
                print("-"*len(note.title))
                print(note.content)

        elif userInput==5:
            noteNum=int(input("Enter note number: "))
            note = session.query(models.Note).filter_by(id=noteNum)
            if note==None:
                print("There is no note with that number")
            else:
                note.delete()
                session.commit()
                
        elif userInput==6:
            cats=session.query(models.Category).all()
            for cat in cats:
                print(f"{cat.id}: {cat.name}")
                
        elif userInput==7:
            name=input("Enter new category: ")
            newCat = models.Category(name=name)
            session.add(newCat)    
            session.commit()
            
        elif userInput==8:
            catNum=int(input("Enter category number: "))
            cat = session.query(models.Category).filter_by(id=catNum).first()
            if cat==None:
                print("No category exists with that number")
            else:
                notes=session.query(models.Note).filter_by(category=cat).all()
                for note in notes:
                    print(f"{note.id}: {note.title}")
                
            
        print()
