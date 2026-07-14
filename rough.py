lst = [1,2,3]
my_str = "rahul"
my_int = 123

from oops_project import ChatBook



user1 = ChatBook()
print(user1.id)
#using static method directly from class rather than object
chatBook.set_id(10)
user2 = ChatBook()
print(user2.id)
print(user1.get_name()) #getter method
user1.set_name("Rahul") #setter method
print(user1.get_name()) #getter method