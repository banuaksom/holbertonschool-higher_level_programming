#include "lists.h"
/**
 * insert_node - inserts  number into list
 * @head: pointer
 * @number: number to initialise node member
 * Return: pointer to new address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new;
	int flag = 0;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	if (!tmp && !head)
		return (NULL);
	else if (!*head)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}
	else if (number < tmp->n)
		flag = 1;
	while (tmp->next && number > tmp->next->n && !flag)
		tmp = tmp->next;
	if (flag)
	{
		new->next = tmp->next;
		tmp->next = new;
	}
	else
	{
		new->next = tmp;
		*head = new;
	}
	new->n = number;
	return (new);
}
