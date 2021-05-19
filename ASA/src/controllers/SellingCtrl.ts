import { findByCode } from "../db/flights";
import { findUser } from "../db/users";
import { Eticket } from "../models/eticket";
import { Flight } from "../models/flight";

const soldTickets: Eticket[] = [];
//
const buyTicket = (username: string, voo: Flight["code"]): Eticket | null => {
  const user = findUser(username);
  if (!user) return null;

  const flight = findByCode(voo);
  if (!flight) return null;

  const newTicket = {
    user,
    flight,
    code: `${flight.code}:${Date.now()}`,
  };
  soldTickets.push(newTicket);

  return newTicket;
};

export { buyTicket };
