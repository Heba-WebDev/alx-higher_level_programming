#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 0 if it is a palindrome and 1 if otherwise
 */


int is_palindrome(listint_t **head)
{

char str[] = malloc(sizeof(char) * 1000);
int i = 0;
listint_t *node = *head;

while (node)
{
str[i] = (char)node->n;
i++;
node = node->next;
}

if (strcmp(str, strrev(str)) == 0)
{
return (0);
}
free(str);
return (1);
}
