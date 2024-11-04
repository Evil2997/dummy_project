// Потенциально уязвимое регулярное выражение для ReDoS
const pattern = /(a+)+/;
const testString = "aaaaaaaaaaaaaaaaaaaaaaaa!";
pattern.test(testString);

// config.js
const apiServer = "192.168.1.6"; // IP for API server
var dbHost = "10.0.0.6"; // Database IP
// Another IP for backup server: 172.16.0.6

