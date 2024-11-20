using System;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        // Потенциально уязвимое регулярное выражение для ReDoS
        string pattern = "(a+)+";
        Regex.IsMatch("aaaaaaaaaaaaaaaaaaaaaaaa!", pattern);
    }
}
