#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(parseInt(arg))) {
  console.log(1);
} else {
  function fact (a) {
    if (a === 0 || a === 1) {
      return 1;
    } else {
      return a * fact(a - 1);
    }
  }
  console.log(fact(arg));
}
