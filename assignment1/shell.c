#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <readline/readline.h>

#define MAX_COMMAND_LENGTH 1000 // Max number of characters for a command

// Clearing the shell using escape sequences
#define clear() printf("\033[H\033[J")

// function prototypes
void printWelcome();
int getUserInput(char *str);
void printWorkingDir();


// print a start up message
void printWelcome()
{
    printf("******************************************\n"); // 42 stars
    printf("*                                        *\n");
    printf("*      ****Welcome to my shell!****      *\n");
    printf("*                                        *\n");
    printf("******************************************\n");
}

// get user input
int getUserInput(char *str)
{
    printWorkingDir();
    printf("$ ");

    char buf[MAX_COMMAND_LENGTH];
    fgets(buf, MAX_COMMAND_LENGTH, stdin);

    if (strlen(buf) != 0)
    {
        strcpy(str, buf);
        return 1;
    }
    else
    {
        return 0;
    }
}

// print Current Working Directory.
void printWorkingDir()
{
    char cwd[1024];
    getcwd(cwd, sizeof(cwd));
    printf("%s", cwd);
}


int main()
{
    char inputString[MAX_COMMAND_LENGTH] = "";
    printWelcome();

    while (1)
    {
        if (!getUserInput(inputString))
        {
            continue;
        }
        else
        {
            printf("You typed: %s", inputString);
            if (strcmp(inputString, "exit\n") == 0)
            {
                printf("Goodbye!\n");
                exit(0);
            }
        }
    }

    return 0;
}
