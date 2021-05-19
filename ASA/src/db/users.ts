import { User } from "../models/user";

const users = [
  {
    username: "admin",
    password: "admin",
  },
  {
    username: "Roberto",
    password: "123456",
  },
];

export function findUser(searchUser: string): User | null {
  const user = users.filter((user) => {
    if (user.username === searchUser) return user;
  });
  return user[0] || null;
}
