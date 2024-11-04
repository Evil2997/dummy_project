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


namespace Config
{
    class Program
    {
        static void Main()
        {
            string apiServer = "192.168.1.3"; // IP for API server
            string dbHost = "10.0.0.3"; // Database IP
            // Another IP for backup server: 172.16.0.3
        }
    }
}

