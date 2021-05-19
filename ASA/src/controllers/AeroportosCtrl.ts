import { getAllAirports } from "../db/airports";
import { Airport } from "../models/airport";

// 4 Retornar todos
const findAll = (): Airport[] => {
  return getAllAirports();
};

// 5 Aeroporto por origem
const findByOrigin = (origin: String): Airport[] => {
  const airports = getAllAirports();
  const newList = airports.filter((airport) => {
    if (airport.location == origin) return airport;
  });
  return newList;
};

export { findAll, findByOrigin };
