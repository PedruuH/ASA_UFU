import express, { Request, Response } from "express";
import * as flightCtrl from "../controllers/FlightCtrl";
import * as users from "../db/users";
import { buyTicket } from "../controllers/SellingCtrl";

const TicketsRouter = express.Router();

// rota 1
TicketsRouter.post("/buy", (req: Request, res: Response) => {
  const user = req.body.user;
  const flight = req.body.flight;
  if (!flightCtrl.findByCode(flight))
    res.status(400).send("Voo não encontrado");

  if (!users.findUser(user)) res.status(400).send("Usuário não encontrado");
  const ticketCode = buyTicket(user, flight)?.code;
  res.status(200).json({ ticketCode: ticketCode });
});

export { TicketsRouter };
