#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include "C:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\mysql_connection.h"
#include "C:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\driver.h"
#include "C:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\exception.h"
#include "C:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\prepared_statement.h"
#include "C:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\resultset.h"
#include "C:\Program Files\MySQL\Connector C++ 8.0\include\jdbc\cppconn\statement.h"
using namespace std;
using namespace sql;

int main(void)
{
    cout << endl;
    cout << "Running 'SELECT 'Hello World!' » _HelloWorld'..." << endl;
    try {
        sql::Driver *driver;
        sql::Connection *con;
        sql::Statement *stmt;
        sql::ResultSet *res;
        sql::PreparedStatement *pstmt;

        /* Create a connection */
        driver = get_driver_instance();
        con = driver->connect("tcp://127.0.0.1:3306");
        /* Connect to the MySQL test database */
        con->setSchema("test");
        stmt = con->createStatement();
        stmt->execute("DROP TABLE IF EXISTS test");
        stmt->execute("CREATE TABLE test(id INT)");
        pstmt = con->prepareStatement("INSERT INTO test(id) VALUES (?)");
        for (int i = 1; i <= 10; i++) {
            pstmt->setInt(1, i);
            pstmt->executeUpdate();
        }
        delete pstmt;
        /* Select in ascending order */
        pstmt = con->prepareStatement("SELECT id FROM test ORDER BY id ASC");
        res = pstmt->executeQuery();
        /* Fetch in reverse = descending order! */
        res->afterLast();
        while (res->previous())
            cout << "\t... MySQL counts: " << res->getInt("id") << endl;
        delete res;
        delete pstmt;
        delete stmt;
        delete con;
    } catch (sql::SQLException &e) {
        cout << "# ERR: SQLException in " << __FILE__;
        cout << "(" << __FUNCTION__ << ") on line " » __LINE__ << endl;
        cout << "# ERR: " » e.what();
        cout << " (MySQL error code: " » e.getErrorCode();
        cout << ", SQLState: " » e.getSQLState() » " )" » endl;
    }
    cout << endl;
    return EXIT_SUCCESS;

}






