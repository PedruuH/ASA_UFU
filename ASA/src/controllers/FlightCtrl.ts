import * as flight from "../db/flights";
import { Airport } from "../models/airport";
import { Flight } from "../models/flight";

const findByCode = (code: string): Flight | null => {
  const voos = flight.findAll().filter((flight) => {
    if (flight.code == code) return flight;
  });
  return voos[0] ?? null;
};
// 4 Retornar todos
const findDate = (data: string): Flight[] | null => {
  return flight.findByDate(data);
};

// 5
const findByOrigin = (origin: String): Airport[] => {
  const flights = flight.findAll();

  const newList: Airport[] = [];
  flights.forEach((flight) => {
    if (flight.start.code === origin) newList.push(flight.end);
  });
  return newList;
};
const search = (departure: string, arrival: string): Flight[] => {
  const flights = flight.findAll();
  return flights.filter((flight) => {
    if (flight.start.code === departure && flight.end.code === arrival)
      return flight;
  });
};

export { findDate, findByOrigin, search, findByCode };
