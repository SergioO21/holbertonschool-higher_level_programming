#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: Singly linked list.
 *
 * Return: (0) if it is not a palindrome, (1) if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *list = *head;
	int i;

	if (*head)
	{
		for (i = 0; list != NULL; i++)
			list = list->next;

		int inverse[i];

		list = *head;

		for (i = 0; list != NULL; i++)
		{
			inverse[i] = list->n;
			list = list->next;
		}

		list = *head;

		for (i = i - 1; i >= 0; i--)
		{
			if (list->n != inverse[i])
				return (0);

			list = list->next;
		}
	}
	return (1);
}
