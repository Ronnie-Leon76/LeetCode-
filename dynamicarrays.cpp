#include <iostream>
#include <cstdio>
#include <cstdlib>

int main( )
{
	// C Style
	int size ;
	scanf ( "%d", &size ) ;

	if ( size > 0 )
	{
		int *arr, *p, i ;
		arr =  ( int* ) malloc ( sizeof ( int ) * size ) ;
		p = arr ;

		for ( i = 0 ; i < size ; i++ )
		{
			scanf ( "%d", p ) ;
			p++ ;
		}
		p = arr ; 

		printf ( "Array Elements using C Style: \n" ) ;
		for ( i = 0 ; i < size ; i++ )
		{
			printf ( "%d\t", *p ) ;
			p++ ;
		}
		free ( arr ) ;
	}
	else
		printf ( "Invalid Input: Array size must be a +ve integer\n" ) ;

	// C++ Style
	int cppSize ;
	std :: cin >> cppSize ;

	if ( cppSize > 0 )
	{
		int *cppArr, *cppP ;
		cppArr = new int[ cppSize ] ;
		cppP = cppArr ;

		for ( int i = 0 ; i < cppSize ; i++ )
		{
			std :: cin >> *cppP ;
			cppP++ ;
		}

		cppP = cppArr ;

		std :: cout << "\nArray Elements using C++ Style: " << std :: endl ;
		for ( int i = 0 ; i < cppSize ; i++ )
		{
			std :: cout << *cppP << "\t" ;
			cppP++ ;
		}
		delete [ ] cppArr ;
	}
	else
		std :: cout << "Invalid Input: Array size must be a +ve integer" << std :: endl ;

	return 0 ;
}
