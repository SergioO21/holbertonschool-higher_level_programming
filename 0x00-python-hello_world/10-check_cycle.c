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
	listint_t *l = list;
	
	while (list)
	{
		list = list->next;

		if (list == l)
			return (1);
	}
	return (0);
}
