#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include <time.h>

#define WIDTH 80 
#define HEIGHT 30 

void move_pos(int x, int y)
{
	HANDLE hOut;
	hOut = GetStdHandle(STD_OUTPUT_HANDLE);
	COORD pos = { x, y };
	SetConsoleCursorPosition(hOut, pos);
}

int main()
{
	FILE* fp = fopen("out_data.txt", "r");
	char buffer[WIDTH + 2] = {};
	int line = 0;

	if (!fp)
	{
		printf("Open file failed.");
		return 0;
	}

	while (fread(buffer, WIDTH + 2, 1, fp) > 0)
	{
		buffer[WIDTH] = 0;
		puts(buffer);
		line++;
		if (line % HEIGHT == 0)
		{
			fread(buffer, 2, 1, fp);
			move_pos(0, 0);
			Sleep(100);
		}
	}

	fclose(fp);
	return 0;
}