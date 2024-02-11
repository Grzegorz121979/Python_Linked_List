from LinkedList import LinkedList

lList = LinkedList()

lList.insertAtBegin(2)
lList.insertAtEnd(1)
lList.insertAtBegin(3)

lList.printLL()
print()

lList.remove_first_node()
lList.updateNode(7, 1)

lList.printLL()
