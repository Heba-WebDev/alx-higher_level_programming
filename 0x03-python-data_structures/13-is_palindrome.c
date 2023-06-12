#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * reverse_string - reverses a string in place
 * @s: string to reverse
 */
void reverse_string(char *s)
{
int len = strlen(s);
int i;
char temp;

for (i = 0; i < len / 2; i++)
{
temp = s[i];
s[i] = s[len - i - 1];
s[len - i - 1] = temp;
}
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 1 if it is a palindrome and 0 if otherwise
 */

int is_palindrome(listint_t **head)
{
char *str;
int i = 0;
listint_t *node = *head;

str = malloc(sizeof(char) * 1000);

while (node)
{
str[i] = (char)node->n;
i++;
node = node->next;
}
str[i] = '\0';

reverse_string(str);

node = *head;
i = 0;
while (node)
{
if (str[i] != (char)node->n)
{
free(str);
return (0);
}
i++;
node = node->next;
}

free(str);
return (1);
}
