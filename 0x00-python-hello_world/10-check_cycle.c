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
	listint_t *l1, *l2;

	l1 = l2 = list;

	while (l1 && l2->next)
	{
		l1 = l1->next;
		l2 = l2->next->next;

		if (l1 == l2)
			return (1);
	}
	return (0);
}
