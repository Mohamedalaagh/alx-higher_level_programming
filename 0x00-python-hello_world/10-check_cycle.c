#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *po2;
	listint_t *pre;

	po2 = list;
	pre = list;
	while (list && po2 && po2->next)
	{
		list = list->next;
		po2 = po2->next->next;

		if (list == po2)
		{
			list = pre;
			pre =  po2;
			while (1)
			{
				po2 = pre;
				while (po2->next != list && po2->next != pre)
				{
					po2 = po2->next;
				}
				if (po2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}

