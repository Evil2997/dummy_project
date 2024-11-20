// Потенциально уязвимое регулярное выражение для ReDoS
const pattern = /(a+)+/;
const testString = "aaaaaaaaaaaaaaaaaaaaaaaa!";
pattern.test(testString);
