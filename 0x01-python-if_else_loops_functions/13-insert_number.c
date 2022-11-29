#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

listint_t *insert_node(listint_t **head, int number)
{
	int i;
	listint_t *hold = malloc(sizeof(listint_t));
	listint_t *insrt = malloc(sizeof(listint_t));

	if (hold == NULL)
	{
		free(hold);
		return(*head);
	}
	hold = *head;

	if (insrt == NULL)
	{
		free(insrt);
		return(hold);
	}
	insrt->n = number;

	if (hold->n >= number)
	{
		insrt->next = hold;
		return(hold);
	}


	for (i = 0; ; i++)
	{
		if (hold->next->n <= number)
		{
			hold = hold->next;
		}
		else if (hold->next->n >= number)
		{
			break;
		}
		else if (hold->next->n == NULL)
			break;
	}
	insrt->next = hold->next;
	hold->next = insrt;
	return(hold);


}
