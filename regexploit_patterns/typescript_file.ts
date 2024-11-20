// Потенциально уязвимое регулярное выражение для ReDoS
const pattern: RegExp = /(a+)+/;
const testString: string = "aaaaaaaaaaaaaaaaaaaaaaaa!";
pattern.test(testString);
