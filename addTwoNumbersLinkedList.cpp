/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    int getNumberOfNodes(struct ListNode *head)
    {
        int count = 0;
        struct ListNode *current = head;

        while (current != NULL)
        {
            count++;
            current = current->next;
        }
        return count;
    }
    int getNodeValue(struct ListNode *head, int index)
    {
        struct ListNode *current = head;
        int count = 0;
        int value;
        while (current != NULL)
        {
            if (count == index)
                int value = current->val;
            count++;
            current = current->next;
        }
        return value;
    }

    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        int listOneCount = getNumberOfNodes(l1);
        int listTwoCount = getNumberOfNodes(l2);
        bool element1Okay;
        bool element2Okay;
        struct ListNode *sumList = NULL;

        for (int i = 0; i < listOneCount; i++)
        {
            int val = getNodeValue(l1, i);
            if ((val >= 0) && (val <= 9))
            {
                element1Okay = true;
            }
            else
            {
                element1Okay = false;
            }
        }
        for (int i = 0; i < listTwoCount; i++)
        {
            int val = getNodeValue(l2, i);
            if ((val >= 0) && (val <= 9))
            {
                element2Okay = true;
            }
            else
            {
                element2Okay = false;
            }
        }
        if ((listOneCount >= 1) && (listOneCount <= 100) && (listTwoCount >= 1) && (listTwoCount <= 100) && (element1Okay) && (element2Okay))
        {
            int large;
            if (listOneCount < listTwoCount)
            {
                large = listTwoCount;
            }
            else
            {
                large = listOneCount;
            }

            for (int i = 0; i < large; i++)
            {
                int sum = 0;
                int add = getNodeValue(l1, i) + getNodeValue(l2, i);
                int mod = (sum + add) % 10;
                sum += (sum + add) / 10;
                
                if(i == 0){
                    sumList = new ListNode(mod);
                }else{
                    struct ListNode *newNode = new ListNode(mod);
                    newNode->next = sumList;
                    sumList = newNode;
                }
                
            }
        }
        else
        {
            std::cout << "Invalid linked list!" << std::endl;
        }

        return sumList;
    }
};


// Solution
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* curr = dummyHead;
        int carry = 0;
        while (l1 != NULL || l2 != NULL || carry != 0) {
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        return dummyHead->next;
    }
};