#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 *
 * @list: Linked List.
 *
 * Return: Returns (0) if there is no cycle,
 *         Returns (1) if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	const listint_t *l1, *l2;
	
	l1 = list;
	l2 = list->next->next;

	while (l1 && l2)
	{
		if (l1 == l2)
			return (1);

		l1 = l1->next;
		l2 = l2->next->next;
	}
	return (0);
}
