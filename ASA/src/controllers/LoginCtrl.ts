import { findUser } from "../db/users";
import { User } from "../models/user";
const jwt = require("jsonwebtoken");
const KEY = "9SY&VHeyvAz*RVt@p8vt";
// 1 Login
export function login(user: User): String {
  const userFound = findUser(user.username);
  if (userFound && userFound?.password === user.password) {
    //token é valido por 1 minuto
    const token = jwt.sign({ _id: user.username }, KEY, { expiresIn: 60 });
    return `bearer ${token}`;
  }
  return "";
}

export function validateToken(token: string) {
  try {
    jwt.verify(token, KEY);
    return "Token OK";
  } catch (err) {
    return "Token Expirado";
  }
}
