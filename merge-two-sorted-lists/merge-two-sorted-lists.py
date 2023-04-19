# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Input: Heads of two sorted LinkedLists
    Output: Head of the merged LinkedList

    Algorithm...
    - Create a dummy node 
    - Iterate through list nodes using two pointers
    - Add node with minimum value to the merged list, until we reach end of list
    - If lists are different lengths, add remaining nodes of the longer list
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedDummy = ListNode()
        mergedTail = mergedDummy

        while (list1 and list2):
            if (list1.val <= list2.val):
                mergedTail.next = list1
                list1 = list1.next
            else:
                mergedTail.next = list2
                list2 = list2.next
            
            mergedTail = mergedTail.next
        
        if ((not list1) and list2):
            mergedTail.next = list2
        elif (list1 and (not list2)):
            mergedTail.next = list1
        
        mergedHead = mergedDummy.next
        return mergedHead 
        