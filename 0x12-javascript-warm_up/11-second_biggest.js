#!/usr/bin/node

const sizeArg = process.argv.length;

if (sizeArg <= 3) {
  console.log(0);
} else {
  const size = process.argv.map(Number);
  size.slice(2, sizeArg);
  size.sort((a, b) => a - b);
  console.log(size[size.length - 2]);
}
