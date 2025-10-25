class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        # цикл while поки списки не пусті
        while list1 != None and list2 != None:            
            # Порівнюєм значення вузлів і приєднюєм перше число, якщо воно менше ніж у другого
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            # За допомогою next приєднюєм по одному символу до dummy(temp)
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        # Приєднюєм те що залишилось
        temp.next = list1 or list2
        # Повертаєм список без самого dummy
        return dummy.next
