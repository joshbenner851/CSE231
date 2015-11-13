	static int move = 0;
	public static void main(String[] args) {
			
			board [][]
			 wins = 0;
			 losses =0;
			 ties = 0;
                         gameCount = 0;
			while (gameCount < 10000)
			{ 
				gameCount++;
				System.out.println("##### Game "+ gameCount + " #####");
				move=0;
			boolean playerWin = false;
			boolean computerWin = false;
			boolean catsGame = false;
			initializeBoard(ttt);
			//play game until winner or tie
			while(!playerWin||!catsGame||!computerWin)
			{
				playerMove(ttt);
				if(checkPlayerWin(ttt))
				{
					wins++;
				//gameCount=10000;  //I used this to exit the loop to test when the computer lost
					break;
				}	
				if(checkCatsGame(ttt))
				{
					ties++;
					break;
				}
				computerMove(ttt);
				move++;
				if(checkComputerWin(ttt))
				{
					losses++;
					break;
				}
				
			}
		
				}
			outputResults(wins, losses, ties);
		}
	public static void initializeBoard( char [] [] board)
	{
		for (int y = 0; y < 3; y++)
		{
			for (int x = 0; x < 3; x++)
			{
				board[x][y] = ' ';
			}
		}
	}
	public static void playerMove(char [] []  board)
	{
		System.out.println("Now the player's turn...\n");
		boolean legalMove = false;
		while(!legalMove)
			{
				int x = (int)(Math.random() * 3);
				int y = (int)(Math.random() * 3);
				if (board[x][y] == ' ')
				{
					board[x][y] = 'X';
					legalMove = true;
				}
			}
		outputBoard(board);
	}
	public static boolean checkPlayerWin(char[][] board)
	{
		boolean winner = false;  //determines if player wins
		//check horizontal wins
		for(int y = 0; y < 3; y++)
		{
			winner = true;
			for(int x = 0; x <3; x++)
			{
				if (board[x][y] != 'X') winner = false;
			}
			if (winner)	return true;
		}
		//check vertical wins
		for(int x = 0; x <3; x++)
		{
			winner = true;
			for(int y = 0; y < 3; y++)
			{
				if (board[x][y] !='X') winner = false;
			}
			if (winner)	return true;
		}
		//check diagonals
		if (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X')winner = true;
		if (board[2][0] == 'X' && board[1][1] == 'X' && board[0][2] == 'X') winner = true;
		if (winner)
		{
		System.out.println("Oh no!  Player wins!");
		return true;
		}
		return false;
	}
	public static void outputBoard(char [] [] board)
	{
		//System.out.println("-------------------");
		for (int y = 0; y < 3; y++)
		{
			for (int x = 0; x < 3; x++)
			{
				if (x!=1)System.out.print("  " + board[x][y]+ "  ");
				else System.out.print("|  " + board[x][y]+ "  |");
			}
			if (y!=2) System.out.println("\n-----------------");
		}
		System.out.println();
		System.out.println();
	}
	public static boolean checkCatsGame(char [] [] board)
	{
		for (int y = 0; y < 3; y++)
		{
			for (int x = 0; x < 3; x++)
			{
				if (board[x][y]==' ') return false; //if there's a space that's not filled in, it's not a cat's game
			}
		}
		System.out.println("Cat's game.  It's a tie.");
		return true;
	}
	public static void computerMove(char [] []  board)
	{
		System.out.println("Now the computer's turn...\n");
                                if(tryToWin(board));
				else if(tryToBlock(board));
				else if(blockexception(board));
				else if (pickCorner(board));
				else {
					random(board);
				}
				outputBoard(board);
				}
	def checkComputerWin(char [] [] board)
	{
		boolean winner = false;  //determines if player wins
		//check horizontal wins
		for(int y = 0; y < 3; y++)
		{
			winner = true;
			for(int x = 0; x <3; x++)
			{
				if (board[x][y] != 'O') winner = false;
			}
			if (winner)	return true;
		}
		//check vertical wins
		for(int x = 0; x <3; x++)
		{
			winner = true;
			for(int y = 0; y < 3; y++)
			{
				if (board[x][y] !='O') winner = false;
			}
			if (winner)	return true;
		}
		//check diagonals
		if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O')winner = true;
		if (board[2][0] == 'O' && board[1][1] == 'O' && board[0][2] == 'O') winner = true;
		if (winner)
		{
		System.out.println("Computer Wins!");
		return true;
		}
		return false;
	}
	public static boolean again()
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Would you like to play again? (y/n)");
		String answer = s.next();
		if (answer.equals("y")) return true;
		else 
			{
				System.out.println("See ya");
				return false;
			}
		}
	public static void outputResults(int w, int l, int t)
	{
		double winpercent = (double) w / (w+l+t) * 100;
		double pcpercent = (double)	l/(w+l+t)*100;
		double catpercent = (double)t/(w+t+l)*100;
		System.out.println();
		System.out.println("Results so far....");
		System.out.println("Games played = " + (w+l+t));
		System.out.println("Player wins = " + w);
		System.out.println("Computer wins = " + l);
		System.out.println("Cat's Games (Ties) = " + t );
		System.out.printf("Player win percentage = %.2f%%", winpercent);System.out.println();
		System.out.printf("Computer win percentage = %.2f%%", pcpercent);System.out.println();
		System.out.printf("Cats game percentage = %.2f%%", catpercent);
		System.out.println();
	}
	public static boolean tryToWin(char [] [] board)
	{
		
	if(board[1][1]==' ')
	{
		board[1][1]='O';
		return true;
	}


	//horizontal win take 
	
		for(int a=0;a<3;a++)
	{
			if (board[a][0]=='O' && board[a][1]=='O' && board[a][2]==' ')
			{
				board[a][2] = 'O';
				return true;
			}
			else if (board[a][1]=='O' && board[a][2]=='O' && board[a][0]==' ')
			{
				board[a][0] = 'O';
				return true;
			}
			else if (board[a][0]=='O' && board[a][2]=='O' && board[a][1]==' ')
			{
				board[a][1] = 'O';
				return true;
				
			}
			
	}
	
	//vertical win take
	
		for(int a=0;a<2;a++)
	
	{
			if (board[0][a]=='O' && board[1][a]=='O'&& board[2][a]==' ')
			{
				
				board[2][a] = 'O';

				return true;
			}
			else if (board[1][a]=='O' && board[2][a]=='O'&& board[0][a]==' ')
			{
				
				board[0][a] = 'O';
		
				
				return true;
			}
			else if (board[0][a]=='O' && board[2][a]=='O' && board[1][a]==' ')
			{
				board[1][a] = 'O';
		
				
				return true;
			}
			
		
	}

	//diagonals
	if (board[0][0]=='O' && board[1][1]=='O' && board[2][2]==' ')
	{
		board[2][2]='O';
		return true;
		
		
	}
	if (board[2][2]=='O' && board[1][1]=='O' && board[0][0]==' ')
	{
		board[0][0]='O';
		return true;
		
	
	}
	if(board[0][0]=='O' && board[2][2]=='O' && board[1][1]==' ')
	{
		board[1][1]='O';
		return true;
	}
	if (board[2][0]=='O' && board[1][1]=='O' && board[0][2]==' ')
	{
		board[0][2]='O';
		return true;
		
		
	}
	if (board[0][2]=='O' && board[1][1]=='O' && board[2][0]==' ')
	{
		board[2][0]='O';
		return true;
		
		
	}
	if (board[0][2]=='O' && board[2][0]=='O' && board[1][1]==' ')
	{
		board[1][1]='O';
	
		return true;
		
	}
	return false;
	}

	public static boolean tryToBlock(char [] [] board)
	{	
	
	//horizontal win take 
	
		for(int a=0;a<3;a++)
	{
			if (board[a][0]=='X' && board[a][1]=='X' && board[a][2]==' ')
			{
				board[a][2] = 'O';
			
				
				return true;
			}
			else if (board[a][1]=='X' && board[a][2]=='X' && board[a][0]==' ')
			{
				board[a][0] = 'O';
			
				
				return true;
			}
			else if (board[a][0]=='X' && board[a][2]=='X' && board[a][1]==' ')
			{
				board[a][1] = 'O';
				return true;	
			}
		
	}
	
	//vertical win take
	
		for(int a=0;a<2;a++)
	
	{
			if (board[0][a]=='X' && board[1][a]=='X'&& board[2][a]==' ')
			{
				
				board[2][a] = 'O';
			
				
				return true;
			}
			else if (board[1][a]=='X' && board[2][a]=='X'&& board[0][a]==' ')
			{
				
				board[0][a] = 'O';
			
				
				return true;
			}
			else if (board[0][a]=='X' && board[2][a]=='X' && board[1][a]==' ')
			{
				board[1][a] = 'O';
			
				
				return true;
			}
			
		return false;
	}

	#diagonals
	if (board[0][0]=='X' && board[1][1]=='X' && board[2][2]==' ')
	{
		board[2][2]='O';
		
		return true;
		
	}
	if (board[2][2]=='X' && board[1][1]=='X' && board[0][0]==' ')
	{
		board[0][0]='O';
		
		return true;
	
	}
	if(board[0][0]=='X' && board[2][2]=='X' && board[1][1]==' ')
	{
		board[1][1]='O';
		
		return true;
	}
	if (board[2][0]=='X' && board[1][1]=='X' && board[0][2]==' ')
	{
		board[0][2]='O';
	
		return true;
	
	}
	if (board[0][2]=='X' && board[1][1]=='X' && board[2][0]==' ')
	{
		board[2][0]='O';
		
	
		return true;
	}
	if (board[0][2]=='X' && board[2][0]=='X' && board[1][1]==' ')
	{
		board[1][1]='O';
		
		return true;
	
	}
	return false;
	}
	public static boolean pickCorner(char [] []  board)

	{
	
		if(board[0][0]==' ')
		{
			board[0][0]='O';
			return true;
		}
		else if (board[0][2]==' '){
			board[0][2]='O';
			return true;
		}
		else if (board[2][0]==' '){
			board[2][0]='O';
			return true;
		}
		else if(board[2][2]==' '){
			board[2][2]='O';
			return true;
		}
			return false;
	}
	public static boolean blockexception(char [][]board)
	{
	
		if(board[0][0]=='X' && board[2][2]=='X'&& board[1][0]==' '){
			board[1][0]='O';
		return true;
		}
		else if(board[2][0]=='X' && board[0][2]=='X'&& board[1][0]==' '){
			board[1][0]='O';
			return true;
		}
		return false;
	}
	public static void random(char[][]board)
	{
	while(true)
	{
		int x = (int)(Math.random() * 3);
		int y = (int)(Math.random() * 3);
		if (board[x][y] == ' ')
		{
			board[x][y] = 'O';
			break;
		}}
	
	}
	}
