import express, { Request, Response } from "express";
import * as flightCtrl from "../controllers/FlightCtrl";
import { Flight } from "../models/flight";
const FlightsRouter = express.Router();

FlightsRouter.get("/data", (req: Request, res: Response) => {
  let data = req.query.data ?? "";
  if (data === "")
    res.status(400).send("Data deve ser fornecida no formado '2021-12-31'");
  data = String(data);

  res.status(200).send(flightCtrl.findDate(data));
});

FlightsRouter.get("/search", (req: Request, res: Response) => {
  const departure = String(req.query.saida);
  const arrival = String(req.query.chegada);
  if (!departure || !arrival)
    res
      .status(400)
      .send("Codigo do Aeroporto de Origem e Destino devem ser informada");

  res
    .status(200)
    .send(
      flightCtrl
        .search(departure, arrival)
        .sort((a: Flight, b: Flight) => a.tax - b.tax)
    );
});

export { FlightsRouter };
