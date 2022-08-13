#include <iostream>	
#include <cmath>

bool isCardano ( int, int, int ) ;

int main( ) 
{
	int count = 0 ;

	for ( int a = 1 ; a < 100 ; a++ ) 
	{
		for ( int b = 1 ; b < 100-a ; b++ ) 
		{
			for ( int c = 1 ; c < 100-a-b ; c++ ) 
			{
				if ( a + b + c <= 100 ) 
				{
					if ( isCardano ( a, b, c ) ) 
					{
						count++ ;
						std :: cout << "Cardano Triplet " << count << ": " 
							   << a << ", " << b << ", " << c << std :: endl ;
					}
				}				
			}
		}
	}

	std :: cout << "Total number of Cardano triplets = " << count << std :: endl ;
	return 0 ;
}

bool isCardano ( int a, int b, int c ) 
{
	float brc = b * sqrt ( c ) ;
	float num = cbrt ( a + brc ) + cbrt ( a - brc ) ;

	if ( num < 1.000001 && num > 0.999999 ) 
		return true ;
	else
		return false ;
}
