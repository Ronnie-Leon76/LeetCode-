
#include <iostream>
#include <cstdarg>


int findmax ( int, ...) ;

int main( )
{
	int  max ;

	max = findmax ( 5, 23, 15, 1, 92, 50 ) ;
	std :: cout << "maximum = " << max << std :: endl ;
	
	max = findmax ( 3, 100, 300, 29 ) ;
	std :: cout << "maximum = " << max << std :: endl ;
	return 0 ;
}

int findmax ( int count, ... )
{
	int  max, i, num ;

	va_list  ptr ;

	va_start ( ptr, count ) ;
	max = va_arg ( ptr, int ) ;

	for ( i = 1 ; i < count ; i++ )
	{
		num = va_arg ( ptr, int ) ;
		if ( num > max )
			max = num ;
	}

	return ( max ) ;
}
