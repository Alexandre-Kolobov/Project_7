Project:
Find the best solution using algorithms

Project Description:
These programms were created to help the company AlgoInvest&Trade to find best investment solution

How to run these programs:

	1)Place your command line in /YOUR_FOLDER and then "git clone https://github.com/Alexandre-Kolobov/Project_7.git"
	
	2)In the folder make "pip install -r requirements.txt" to set up the right configuration
	
	3)Now you are ready to execute the program.
	
How to use it:
	There are two programs bruteforce.py and optimized.py:
	
		1) bruteforce.py tests all solution and find the best one. It works with csv files.
			It is precise but execution time is long.
			To launch in your command line "python bruteforce.py /YOUR_CSV_FILE"
		
		2) optimized.py uses gluton algorithm to find the near the best solution . It works with csv files.
			It is near precise but execution time is fast.
			To launch in your command line "python optimized.py /YOUR_CSV_FILE"