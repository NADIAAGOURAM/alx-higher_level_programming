#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - insert a node inside a sorted list
 * @head: head of the list
 * @number: the number to add within a list
 * Return: the new Node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;


	return (new);
}

