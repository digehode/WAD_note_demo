#!/usr/bin/env python3
import db
import models

# Make these settings match your Makefile
user="demodb"
password="swordfish"
dbname="demodb"
port="3333"

if __name__=="__main__":

    # This is all just demo code you can base your own demo code off it
    # It also demonstrates how to initialise the DB, add items, query, etc
    
    create_yn=input("Create DB? Enter Y to create, anything else to skip: ")
    if create_yn=="Y":
        db.create_db(user,password,port,dbname)

    # A session object is our DB connection
    session=db.connect(user,password,port,dbname)

    #Create a new note
    title=input("Enter new note title: ")
    content=input("Enter new note content: ")
    newNote = models.Note(title=title,content=content)

    #Add it to the DB
    session.add(newNote)    
    session.commit()


    notes=session.query(models.Note).all()

    print()
    for note in notes:

        title=f"{note.title} ({note.id})"
        print(title)
        print("-"*len(title))
        print(note.content)
        print()
