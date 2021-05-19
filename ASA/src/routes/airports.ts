import express, { Request, Response } from "express";
import { findAll } from "../controllers/AeroportosCtrl";
import * as flightCtrl from "../controllers/FlightCtrl";

const AirportRouter = express.Router();
// rota 4
AirportRouter.get("/all", (req: Request, res: Response) => {
  const result = findAll();
  res.status(200).json(result);
});

// rota 5
AirportRouter.get("/departure/:airportCode", (req: Request, res: Response) => {
  if (!req.params.airportCode) res.status(400).json("Origem não informada");
  const result = flightCtrl.findByOrigin(req.params.airportCode);
  res.status(200).json(result);
});

export { AirportRouter };
