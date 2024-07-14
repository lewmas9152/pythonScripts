class Node ():

    # construtor for initialising a node(it contains, the data element and a pointer to the next node)

    def __init__(self,data):
        self.data = data
        self.next = None


class linked_list():

    # initialize the list(set the head to none ---> there is no element in the list)
    def __init__(self):
        self.head = None


    def insert_at_beginning(self,new_data):
        #create a node containing the data entered
        new_data = Node(new_data)

        #move the current head to the next node
        new_data.next = self.head

        # make the current new_data occupy the head
        self.head = new_data

    def print_list(self):
        # Print the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    llist = linked_list()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(51)
    llist.insert_at_beginning(52)
    llist.insert_at_beginning(35)
    llist.insert_at_beginning(65)

    llist.print_list()
    

