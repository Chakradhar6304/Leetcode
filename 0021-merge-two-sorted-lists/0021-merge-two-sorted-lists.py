# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Creating a dummy node to start the merged list
        dummy = ListNode()
        current = dummy
        
        # Iterating through both lists
        while list1 and list2:
            # Comparing the values of the current nodes of list1 and list2
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Appending the remaining elements of list1 or list2 to the merged list
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Returning the merged list, excluding the dummy node
        return dummy.next
