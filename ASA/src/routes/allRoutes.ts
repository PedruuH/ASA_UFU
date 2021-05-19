import express from "express";
import { FlightsRouter } from "./flights";
import { LoginRouter } from "./login";
import { AirportRouter } from "./airports";
import { TicketsRouter } from "./tickets";

const allRoutes = express.Router({ caseSensitive: true });

allRoutes.get("/", (req, res) => res.status(200).json({ message: "ok" }));

allRoutes.use("/auth", LoginRouter);
allRoutes.use("/airports", AirportRouter);
allRoutes.use("/flights", FlightsRouter);
allRoutes.use("/tickets", TicketsRouter);

export { allRoutes };
