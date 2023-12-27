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
int main() {
    // Creating first number: 2 -> 4 -> 3 (represents 342)
    ListNode *l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);

    // Creating second number: 5 -> 6 -> 4 (represents 465)
    ListNode *l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);

    Solution solution;
    ListNode *result = solution.addTwoNumbers(l1, l2);

    // Printing the result: 7 -> 0 -> 8 (represents 807)
    while (result != nullptr) {
        cout << result->val << " -> ";
        result = result->next;
    }
    cout << "null" << endl;

    return 0;
}

