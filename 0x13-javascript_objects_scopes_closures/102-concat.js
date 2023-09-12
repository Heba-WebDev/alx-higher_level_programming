#!/usr/bin/node
const fs = require('fs');

const argOne = fs.readFileSync(process.argv[2]).toString();
const argTwo = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], argOne + argTwo);
