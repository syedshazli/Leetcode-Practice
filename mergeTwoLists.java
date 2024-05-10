/**
*Notes
  * Return the head of the merged list, merged list in ascending order
  * So we need to make a dummy node that points to the first value
  * Create another ListNode 'current' that points to dummy
  * All we have to do is "rewire" the 'current' ListNode so it merges the lists in ascending order
  * While list1 is not null and list2 is not null
  *  Check which list's node is greater
  *    'Current' listNode then equals the list with the smaller node 
  *     list1/list2 = list1/list2.next
  *   Obviously have an else for list 1 and list 2 whichever one isn't greater
  *  outside of if/else, current = current.next
  *  outside of while loop:
  *  if list1/list 2 is not null, current.next = list1/list2. This is because after we went through the lists, one of them was outstandingly greater/smaller. so we just append what's left onto current
  * return dummy.next, since dummy is just the first value of current
  
  */







/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //am I supposed to use merge sort or something?
        //update, we want to rewire the linkedlist to point t
        ListNode dummy = new ListNode(0); //make sure we don't run into null issues
        ListNode current = dummy;


        while(list1 != null && list2 != null){
            if(list1.val<list2.val){ //in ascending order, so smaller value will be next
                current.next = list1;
                list1 = list1.next;
            }
            else{ //list 1 is bigger/equal than list 2 val, so list 2 val next
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next; //rewire the new current node

        }

            if(list1!= null){ //list is not empty after iterating, append list 1 to current
                current.next = list1;
            }
            else{
                current.next = list2;
            }

        return dummy.next;

        
    }
}
