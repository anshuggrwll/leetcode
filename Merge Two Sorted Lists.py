# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list=list1.extend(list2)
        print(new_list)

        return("Anshu")


if __name__=="__main()":
    list1 = [1,2,4]
    list2 = [1,3,4]
    a=Solution.mergeTwoLists()
    output=a(list1,list2)
    print(output)
