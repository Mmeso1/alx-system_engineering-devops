#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - ...
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the entry point
 * Return: 0 on success
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t pid = fork();

		if (pid == -1)
		{
			infinite_while();
		}

		if (pid == 0) {
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

	return 0;
}

