import express, { Request, Response } from "express";
import { login, validateToken } from "../controllers/LoginCtrl";

const LoginRouter = express.Router();
let tokenBlacklist: string[] = [];

// rota 1
LoginRouter.post("/login", (req: Request, res: Response) => {
  const result = login(req.body);
  if (result == "") return res.status(400).send("Falha ao Logar");
  res.status(200).json({ token: result });
});

// rota 2
LoginRouter.post("/logout", (req: Request, res: Response) => {
  const token = req.headers.authorization?.split(" ")[0];
  if (token) tokenBlacklist.push(token);

  res.status(200).json({});
});

// rota 3
LoginRouter.post("/validate", (req: Request, res: Response) => {
  const token = req.headers.authorization?.split(" ")[0];
  if (!token) res.status(400).send("Envie o Token");
  if (token) {
    if (tokenBlacklist.includes(token))
      return res.status(401).send("Token Invalido");

    const status = validateToken(token);
    res.status(200).json(status);
  }
});

export { LoginRouter };
