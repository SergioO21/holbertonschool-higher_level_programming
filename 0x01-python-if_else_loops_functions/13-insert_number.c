#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Linked list.
 * @number: New value.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new_node, *previous_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	list = previous_node = *head;
	new_node->n = number;
	new_node->next = *head;

	while (list != NULL)
	{
		if (list->n > number)
		{
			previous_node->next = new_node;
			new_node->next = list;
			break;
		}

		if (list->n < number)
		{
			new_node->next = list->next;

			if (list->next != NULL)
			{
				previous_node = list;
				list = list->next;
			}

			else
			{
				list->next = new_node;
				new_node->next = NULL;
				break;
			}
		}
	}
	return (list);
}
