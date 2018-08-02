#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <iomanip>
#include <cstring> 

using namespace std;

int map[4][4];


void printmap() //将棋盘打印在屏幕上 
{
	system("cls");
	for(int i=0;i < 4 ; i++)
	{	
		cout<<"  --------------------------"<<endl;
		for(int j = 0 ; j < 4 ; j++)
		{
			cout<<setw(2)<<"|";
			if(map[i][j])
				cout<<setw(5)<<map[i][j];
			else
				cout<<setw(5)<<'\0';
		}
		cout<<setw(2)<<"|";
		cout<<endl;
	}
	cout<<"  --------------------------"<<endl;
}
int newint() //产生一个随机数2或4 用于加入到棋盘上 
{
	int a = rand()%2;
	if(a == 0) 
		return 2;
	else 
		return 4;
}
void newnum() 
{	
	bool b = false;
	for(int i = 0 ; i < 4 ; i++) //确认棋盘上是否有空位加入一个新数 
		for(int j = 0 ; j < 4 ; j++) //否则棋盘满了导致死循环 
			if(map[i][j] == 0)
			{
				b = true;
				break;
			}
	if(b)
	{
		do
		{
			int a = rand()%4 ;
			int b = rand()%4 ;
			if (map[a][b] == 0 )
			{
				
				int c = newint();
				map[a][b] = c;
				break;
			}
		}while ( 1 );
	}
}
bool check() //检查游戏是否结束 
{
	for( int i = 0 ; i < 4 ; i++ )
	{
		for( int j = 0 ; j < 4 ; j++ )
		{
			if( map[i][j] == 0) //如果棋盘上还有空位 可以继续游戏 
				return true;
			if(j != 3) //如果有相邻的两个数相等 可以继续游戏 
			{
				if( map[i][j] == map[i][j + 1] )
					return true;
				if( map[j][i] == map[j+1][i] )
					return true;
			}
		}
	}
	return false;
}
void merge(int i,char c)
{
	bool flag;
	switch(c)
	{
		case 'W':
			do
			{	
				flag = false;
				for( int j = 1 ; j < 4 ; j++ )
				{
					if( map[j][i] != 0 )
					{
						if(map[j - 1][i] == 0 )
						{	
							swap( map[j][i] , map[j - 1][i] );
							flag = true;
						}
					}					
				}
			} while( flag );
			break;
		case 'A':
			do
			{	
				flag = false;		
				for( int j = 1 ; j < 4 ; j++ )
				{
					if( map[i][j] != 0 )
					{
						if( map[i][j - 1] == 0 )
						{
							swap( map[i][j] , map[i][j - 1] );
							flag = true;
						}
					}					
				}
			} while( flag );
			break;
		case 'S':
			do
			{		
				flag = false;		
				for( int j = 2 ; j >= 0 ; j-- )
				{
					if( map[j][i] != 0 )
					{
						if( map[j + 1][i] == 0 )
						{
							swap( map[j][i] , map[j + 1][i] );
							flag = true;
						}
					}					
				}
			} while( flag );
			break;
		case 'D':
			do
			{	
				flag = false;			
				for( int j = 2 ; j >= 0 ; j-- )
				{
					if( map[i][j] != 0 )
					{
						if( map[i][j + 1] == 0 )
						{
							swap( map[i][j] , map[i][j + 1] );
							flag = true;
						}
					}					
				}
			} while( flag );
			break;
	}

}
void move( char c ) //进行上下左右的移动 
{
	if( c == 'W' )
	{
		bool flag;
		for( int i = 0 ; i < 4 ; i++ )
		{	
			//一次循环处理一列 
			merge(i,c);
			for( int j = 1; j < 4 ; j++ )
			{
				if( map[j - 1][i] == map [j][i] )
				{
					map[j - 1][i] *= 2;
					map[j][i] = 0;					
				}			
			}
			merge(i,c);
		}
	}
	if(c == 'A')
	{
		bool flag;
		for( int i = 0 ; i < 4 ; i++ )
		{	
			//一次循环处理一行  
			merge(i,c);
			for( int j = 1; j < 4 ; j++ )
			{
				if( map[i][j - 1] == map [i][j] )
				{
					map[i][j - 1] *= 2;
					map[i][j] = 0;		
				}			
			}
			merge(i,c);		
			
		}
	}
	else
	if(c == 'S')
	{
		bool flag;
		for( int i = 0 ; i < 4 ; i++ )
		{	
			//一次循环处理一列  
			merge(i,c);
			for( int j = 2 ; j >= 0 ; j-- )
			{
				if( map[j + 1][i] == map [j][i] )
				{
					map[j + 1][i] *= 2;
					map[j][i] = 0;
				}					
			}			
			merge(i,c);
		}
	}
	else
	if(c == 'D')
	{
		bool flag;
		for(int i = 0 ; i < 4 ; i++)
		{	
			//一次循环处理一行  
			merge(i,c);
			for( int j = 2 ; j >= 0 ; j-- )
			{
				if( map[i][j + 1] == map [i][j] )
				{
					map[i][j + 1] *= 2;
					map[i][j] = 0;		
				}			
			}
			merge(i,c);
		}
	}
}
bool arraycmp(int lastmap[4][4])
{
	for(int i = 0 ; i < 4 ; i++)
		for(int j = 0 ; j < 4 ; j++)
			if(lastmap[i][j] != map[i][j])
				return false;
	return true;
}
bool keyEvent(char c) 
{
	if(c > 90)//处理大小写 
		c -= 32;
	if(c!='W'&&c!='A'&&c!='S'&&c!='D') //按下了错误的键 
		return true; 
	else
	{	
		int lastmap[4][4];
		memcpy(lastmap,map,sizeof(map)); 
		move(c); //移动 
		if(!arraycmp(lastmap))
		{
			newnum(); //加入一个新数 
			move(c);
		} 
		printmap();
		return check();
	}
}

void makeempty() //将棋盘清空重新开始游戏 
{
	memset(map,0,sizeof(map));
}
void init() //初始化游戏
{
	makeempty();
	newnum();newnum();	
	printmap();
} 
int main()
{	
	srand( time ( 0 ) );
	loop:  //每次游戏开始的位置 
		init();
		char c;//每次按下的键 
		while(1)
		{
			c = getch();
			if(!keyEvent(c))
			break;
		}
		printmap();
		cout<<"游戏结束"<<endl; 
		cout<<"按K重新开始，按L退出游戏";
		while(1)
		{
			c = getch();
			if(c == 'l' || c == 'L')
				exit(0);
			if(c == 'k' || c == 'K')
				goto loop;
		} 
	return 0;
}
