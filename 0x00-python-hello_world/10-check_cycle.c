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
	const listint_t *l = list->next->next;

	while (list && l)
	{
		if (list == l)
			return (1);

		l = l->next->next;
		list = list->next;
	}
	return (0);
}
