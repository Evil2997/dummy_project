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

// IP for API server
const string apiServer = "192.168.1.6";
string dbHost = "10.0.0.6"; // Database IP
// Another IP for backup server: 172.16.0.6

const string MyapiServer = "My 192.168.1.6"; // IP for API server
const string apiServerIP = "192.168.1.6 Server"; // IP for API server
const string MyapiServerIP = "My 192.168.1.6 Server"; // IP for API server
// config.ts
const string apiServerWithPort = "% 192.168.1.2 123"; // IP for API server
string dbHostWithPort = ": 123 10.0.0.2"; // Database IP
// Backup server IP: 172.16.0.2
var hosts = new Dictionary<string, string>
{
    { "database_host", "192.168.1.1" }, // This is the database server IP
    { "app_host", "10.0.0.1" },
    // Another server IP is 172.16.0.1
    { "app_host_2", "host 2 by // ip: 114.15.0.1" },
    { "app_host_4", "10.0.4.1 host 2 by ip" },
    { "app_host_3", ": 10.2.0.12" },
    { "app_host_41", ": 11.0.0.172 host 2 by ip" }
};
