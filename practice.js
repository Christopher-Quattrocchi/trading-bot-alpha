// Input: {0, 1, 2, 0, 1, 2}


function sortInput(inputArray) {
  let outputArray = [...inputArray];
  for (i = 0; i < inputArray.length; i++) {
    for (j = 0; j < inputArray.length - 1; j++) {
      if (inputArray[j] > inputArray[j + 1]) {
        let temp = outputArray[j]
        outputArray[j] = outputArray[j + 1];
        outputArray[j + 1] = temp;
      }
    }
  }
  return outputArray
}

// Input: arr = [1, 2, 3, 4, 6], N = 6
// Output: 5 // The missing number

function findMissingNumber(arrArray) {
  let missingNumber;
  for (i = 0; i < arrArray.length; i++) {
    if (arrArray[i] + 1 !== arrArray[i + 1]) {
      return arrArray[i] + 1;
    }
  }
  return arrArray[arrArray.length - 1] + 1;
}

// Example 1:
// Input: “ABCDEFGABEF”
// Output: 7
// Explanation: The longest substring without repeating characters are “ABCDEFG”, “BCDEFGA”, and “CDEFGAB” with lengths of 7

function longestSubString(string) {
  let maxLength = 0;
  let start = 0;
  let charSet = new Set();

  for (let end = 0; end < string.length; end++) {
    while (charSet.has(string[end])) {
      charSet.delete(string[start]);
      start++
    }
    charSet.add(string[end]);
    maxLength = Math.max(maxLength, end - start + 1);
  }
  return maxLength;
}