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
	const listint_t *l = list;
	int n2;
	listint_t *initial_next;

	n2 = l->n;
	initial_next = l->next;

	l = l->next;

	while (l != NULL)
	{
		if (l->n == n2 && l->next == initial_next)
			return (1);

		l = l->next;
	}
	return (0);
}
