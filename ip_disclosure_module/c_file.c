#include <stdio.h>
#include <string.h>

// IP for API server
const char* apiServer = "192.168.1.6";
char dbHost[] = "10.0.0.6"; // Database IP
// Another IP for backup server: 172.16.0.6

const char* MyapiServer = "My 192.168.1.6"; // IP for API server
const char* apiServerIP = "192.168.1.6 Server"; // IP for API server
const char* MyapiServerIP = "My 192.168.1.6 Server"; // IP for API server

const char* apiServerWithPort = "% 192.168.1.2 123"; // IP for API server
char dbHostWithPort[] = ": 123 10.0.0.2"; // Database IP
// Backup server IP: 172.16.0.2

struct Host {
    const char* key;
    const char* value;
};

// Define array of hosts
struct Host hosts[] = {
    {"database_host", "192.168.1.1"}, // This is the database server IP
    {"app_host", "10.0.0.1"},
    // Another server IP is 172.16.0.1
    {"app_host_2", "host 2 by // ip: 114.15.0.1"},
    {"app_host_4", "10.0.4.1 host 2 by ip"},
    {"app_host_3", ": 10.2.0.12"},
    {"app_host_41", ": 11.0.0.172 host 2 by ip"}
};