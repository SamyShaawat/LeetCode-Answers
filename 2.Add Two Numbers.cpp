// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#include <iostream>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode head = 0;
    ListNode *current = &head;
    int carry = 0;
    while (l1 != NULL || l2 != NULL || carry != 0) {
      int sum = carry;
      if (l1 != NULL) {
        sum = sum + l1->val;
        l1 = l1->next;
      }
      if (l2 != NULL) {
        sum += l2->val;
        l2 = l2->next;
      }
      if (sum >= 10) {
        carry = 1;
        sum -= 10;

      } else {
        carry = 0;
      }
      current->next = new ListNode(sum);
      current = current->next;
    }
    return head.next;
  }
};
int main() { return 0; }
