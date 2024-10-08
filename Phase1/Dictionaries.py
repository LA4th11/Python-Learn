""" Exercise 1: Basic Dictionary Operations
Create a dictionary to store information about a book, with the following keys: title, author, year, and genre.

Task:

Add at least 3 entries to the dictionary.
Print the value associated with the author key.
Update the year key to a new value.
Remove the genre key from the dictionary.

Exercise 2: Looping Through a Dictionary
Create a dictionary of students where the key is the student name and the value is their grade.

Task:

Add at least 5 student names with their grades.
Write a loop to print each student's name along with their grade.
Write a condition inside the loop to print only students who have a grade above 85.

Exercise 3: Nested Dictionary
Create a dictionary representing a phonebook, where each key is a person's name, and the value is another dictionary with details like phone_number and email.

Task:

Add at least 3 people to the phonebook with their contact details.
Access and print the phone number of a specific person.
Add a new key, address, to one of the people in the dictionary. """

#-------------------------------------#

#Exercise 1: Basic Dictionary Operations
""" class Dictionary:
  books = {
    "book1":{
      "title":"1984",
      "author":"George Orwell",
      "year":1949,
      "genre":"Dystopian"
      },
    "book2":{
      "title":"Brave New World",
      "author":"Aldous Huxley",
      "year":1932,
      "genre":"Dystopian"
    },
    "book3":{
      "title":"Fahrenheit 451",
      "author":"Ray Bradbury",
      "year":1953,
      "genre":"Dystopian"
    }
  }
  
  def books_author():
    books = Dictionary.books
    
    counter = 1
    
    for books_key in books:
      author = books[books_key]["author"]
      
      print(F"Author {counter}: {author}")
      
      counter += 1
    
    print()
  
  def books_year():
    books = Dictionary.books

    books["book1"].update({"year":2000})
    books["book2"].update({"year":2001})
    books["book3"].update({"year":2002})
    
    counter = 1
    
    for books_key in books:
      year = books[books_key]["year"]
      
      print(F"Year {counter}: {year}")
      
      counter += 1
    
  def books_remove():
    books = Dictionary.books
    
    for books_key in books:
      books[books_key].pop("genre")
      
      print(books[books_key].keys())
    
    

if __name__ == "__main__":
  Dictionary.books_author()
  Dictionary.books_year()
  Dictionary.books_remove() """

#Exercise 2: Looping Through a Dictionary
""" class Classroom:
  students = {
    "Alice":90,
    "Bob":75,
    "Charlie":88,
    "Diana":92,
    "Eve":81
  }
  
  def student_info():
    student_infos = Classroom.students
    
    for student_names, student_grades in student_infos.items():
      print(F"Name: {student_names} --> Grade: {student_grades}")

    print()
    
  def students_pass():
    student_infos = Classroom.students
    
    for student_name, student_grade in student_infos.items():
      if student_grade >= 85:
        print(F"Name: {student_name} --> Grade: {student_grade}")
  
if __name__ == "__main__":
  Classroom.student_info()
  Classroom.students_pass() """
  
#Exercise 3: Nested Dictionary
""" class Phonebook:
  phonebook = {
    "John":{
      "phone_number":"123-456-7890",
      "email":"john@example.com"
    },
    "Jane":{
      "phone_number": "987-654-3210", 
      "email": "jane@example.com"
      },
    "Sam":{
      "phone_number": "555-666-7777", 
      "email": "sam@example.com"
      }
  }
  
  def phonebook_add(self, added_info):
    phonebook_info = Phonebook.phonebook
    phonebook_info.update(added_info)
    
    for phonebook_name, contact_info in phonebook_info.items():
      print(F"Name: {phonebook_name}\nPhone Number: {contact_info["phone_number"]}\nEmail: {contact_info["email"]}\n")

  
  
if __name__ == "__main__":
  phonebook_instance = Phonebook()
  
  phonebook_added = {
    "Lorenzo":{
      "phone_number":"090-090-09090",
      "email":"lorenzo@example.com"
    },
    "Micaella":{
      "phone_number":"101-012-0000",
      "email":"micaella@example.com"
    }
  }
  phonebook_instance.phonebook_add(phonebook_added) """