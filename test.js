function generatePassword(length) {
  let characters = string.ascii_letters + string.digits + string.punctuation;
  characters += string.ascii_lowercase + string.ascii_uppercase;
  let password = "";

  for (let i = 0; i < length; i++) {
    password += characters.charAt(
      Math.floor(Math.random() * characters.length)
    );
  }

  return password;
}
let password = generatePassword(8);
console.log(password);
