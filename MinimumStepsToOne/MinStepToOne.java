
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class MinStepToOne
{
	public static int minToOne(int n , int[] dp)
	{
		
		
		
		for(int i=2 ;i<=n;i++)
		{
		dp[i] = 1 + dp[i-1];
       if(i%2 == 0)
        dp[i] = Math.min(dp[i], 1 + dp[i/2]);
       if(i%3 == 0)		
		dp[i] = Math.min(dp[i], 1 + dp[i/3]);
		}		
		return dp[n];
	}
	
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		
		int dp[]=new int[n+1];
		for(int j=0;j<=n;j++)
		dp[j]=0;
		dp[1]=0;
		
		
		System.out.println(minToOne(n,dp));
		
	}
}