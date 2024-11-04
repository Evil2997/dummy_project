// Потенциально уязвимое регулярное выражение для ReDoS
const pattern: RegExp = /(a+)+/;
const testString: string = "aaaaaaaaaaaaaaaaaaaaaaaa!";
pattern.test(testString);

// config.ts
const apiServer = "192.168.1.2"; // IP for API server
let dbHost = "10.0.0.2"; // Database IP
// Backup server IP: 172.16.0.2

