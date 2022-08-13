#include <iostream>

int numSundaysFirst();
bool isLeap(int);

enum month
{
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC
};

enum day
{
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN
};

int main()
{
    std ::cout << numSundaysFirst();
    return 0;
}

int numSundaysFirst()
{
    int sundaycount;
    int firstday, lastday;

    firstday = MON; // January 1st, 1900 is given to be a Monday

    // setting the last day of 1900, i.e. 31st December, 1900
    if (isLeap(1900))
        lastday = TUE;
    else
        lastday = MON;

    sundaycount = 0;
    for (int year = 1901; year <= 2000; year++)
    {
        for (int month = JAN; month <= DEC; month++)
        {
            firstday = (lastday + 1) % 7;

            if (firstday == SUN)
                sundaycount++;

            switch (month)
            {
            case JAN:
            case MAR:
            case MAY:
            case JUL:
            case AUG:
            case OCT:
            case DEC:
                lastday = (firstday + 2) % 7;
                break;

            case APR:
            case JUN:
            case SEP:
            case NOV:
                lastday = (firstday + 1) % 7;
                break;

            case FEB:
                if (isLeap(year))
                    lastday = firstday;
                else
                    lastday = (firstday + 6) % 7;
                break;
            }
        }
    }

    return sundaycount;
}

bool isLeap(int year)
{
    if ((year % 100 != 0) && (year % 4 == 0) || (year % 400 == 0))
        return true;
    else
        return false;
}
