# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def printlist(self,head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next


    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # define two pointers 
        dummy = ListNode(0,head)
        l,r = dummy,dummy
        while r.next:
            l = l.next
            if r.next == None:
                r = r.next
            else:
                r = r.next.next
            if r == None:
                break
        r_head = l.next
        l.next = None
        # reverse the right linklist 
        prev = None
        curr = r_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        left = head
        right = prev
        new_node = ListNode(0)
        curr = new_node
        while  right or left :
            if left == None and right == None:
                break
            if left:
                    curr.next = left
                    left = left.next
                    curr = curr.next
                    curr.next = None

            if right:
                    curr.next = right
                    right = right.next
                    curr = curr.next
                    curr.next = None
        return new_node.next
