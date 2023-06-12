#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 1 if it is a palindrome and 0 if otherwise
 */

int is_palindrome(listint_t **head)
{
char str[500];
int len, j, i = 0;
listint_t *node = *head;

while (node)
{
str[i] = (char)node->n;
i++;
node = node->next;
}

if (i % 2 == 0)
{
len = i / 2;
}
else
{
len = floor(i / 2);
}

for (j = 0; j < len; j++)
{
if (str[j] != str[i - j - 1])
{
return (0);
}
}

return (1);
}
